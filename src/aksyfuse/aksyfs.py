#!/usr/bin/python

import fuse

from time import time

import stat
import os
import os.path
import errno

from aksy.device import Devices
from aksy import fileutils, model
from aksy.devices.akai import sampler as samplermod

fuse.fuse_python_api = (0, 1) # TODO: migrate to 0.2

MAX_FILE_SIZE_SAMPLE = 512 * 1024 * 1024 # 512 MB
MAX_FILE_SIZE_OTHER = 16 * 1024 # 16K
EOF = '\x00'
START_TIME = time()

def stat_inode(mode, size, child_count, uid, gid, writable=False):
    info = [None] * 10
    info[stat.ST_DEV] = 0 # TODO: figure out whether required to provide unique value
    info[stat.ST_INO] = 0 # TODO: figure out whether required to provide unique value
    info[stat.ST_MODE] = mode|stat.S_IRUSR|stat.S_IRGRP
    if writable:
        info[stat.ST_MODE] = info[stat.ST_MODE]|stat.S_IWUSR
    info[stat.ST_SIZE] = size
    info[stat.ST_ATIME] = int(START_TIME)
    info[stat.ST_CTIME] = info[stat.ST_ATIME]
    info[stat.ST_MTIME] = info[stat.ST_ATIME]
    info[stat.ST_NLINK] = child_count
    info[stat.ST_UID] = uid
    info[stat.ST_GID] = gid
    return info

def stat_dir(uid, gid, child_count=1):
    return stat_inode(stat.S_IFDIR|stat.S_IWRITE|stat.S_IEXEC, 4096L, child_count, uid, gid)

# TODO: provide real values for samples (other sizes can't be determined
def stat_file(uid, gid, path):
    cache_path = _get_cache_path(path)
    if os.path.exists(cache_path):
        size = os.stat(cache_path)[stat.ST_SIZE]
    elif fileutils.is_sample(path):
        size = MAX_FILE_SIZE_SAMPLE
    else:
        size = MAX_FILE_SIZE_OTHER
    return stat_inode(stat.S_IFREG|stat.S_IWUSR, size, 0, uid, gid)

def _splitpath(path):
    return path.split('/', 2)[1:]

def _get_cache_path(path):
    return os.path.join(os.path.expanduser('~'), '.aksy/cache' + path)

def _create_cache_path(path):
    cache_path = os.path.join(os.path.expanduser('~'), '.aksy/cache' + path)
    parent_dir = os.path.dirname(cache_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    return cache_path

class FileInfo(object):
    def __init__(self, path, upload, handle=None, flags=None):
        location = _splitpath(path)[0]
        if location == "memory":
            self.location = samplermod.AkaiSampler.MEMORY
        elif location == "disks":
            self.location = samplermod.AkaiSampler.DISK
        else:
            raiseException(errno.ENOENT)
        
        self.name = os.path.basename(path)
        self.path = _create_cache_path(path)
        self.upload = upload

        if handle is None:
            self.handle = os.open(self.path, flags)
        else:
            self.handle = handle
        
    def get_name(self):
        return self.name
    
    def get_path(self):
        return self.path
    
    def get_handle(self):
        return self.handle
    
    def is_upload(self):
        return self.upload
    
    def get_location(self):
        return self.location
        
class FSRoot(object):
    def __init__(self, sampler):
        self.sampler = sampler
        self.file_cache = {} 
        
    def get_children(self):
        return [self.sampler.memory, self.sampler.disks]

    def find_child(self, path):
        store_name  = _splitpath(path)[0]
        for store in self.get_children():
            if store.get_name() == store_name:
                return store
        return None


    def get_dir(self, path):
        if path == '/':
            return self
        rel_path  = _splitpath(path)[1]
        store = self.find_child(path)
        if store is None:
            raiseException(errno.ENOENT)        
        
        if not hasattr(store, 'get_dir'):
            raiseException(errno.ENOENT)
        subdir = store.get_dir(rel_path)
        if subdir is None:
            raiseException(errno.ENOENT)
        
        return subdir
        
    def mkdir(self, path):
        store = self.find_child(path)
        if not hasattr(store, 'create_folder'):
            raiseException(errno.EINVAL)
        return store.create_folder(path)
        
    def open(self, path, flags):
        info = self.file_cache.setdefault(path, FileInfo(path, False, flags=flags|os.O_CREAT))
        if not info.is_upload():
            self.sampler.get(info.get_name(), info.get_path(), info.get_location())
        
    def close(self, path):
        info = self.file_cache.get(path, None)
        if info is not None:
            if info.is_upload():
                try:
                    self.sampler.put(info.get_path(), None, info.get_location())
                except IOError, exc:
                    # TODO: move to a method where we can raise exceptions
                    print "Exception occurred: ", repr(exc)
            os.close(info.get_handle())
            del self.file_cache[path]

    def mknod(self, path):
        self.file_cache[path] = FileInfo(path, True, flags=os.O_CREAT|os.O_RDWR)
        
    def write(self, path, buf, offset):
        handle = self.file_cache[path].get_handle()
        os.lseek(handle, offset, 0)
        return os.write(handle, buf)

    def read(self, path, length, offset):
        handle = self.file_cache[path].get_handle()
        os.lseek(handle, offset, 0)
        read = os.read(handle, length)
        if len(read) < length:
            return read + EOF
        else:
            return read
    
class AksyFS(fuse.Fuse): #IGNORE:R0904
    def __init__(self, sampler, **args):
        self.flags = 0
        self.multithreaded = 0
        self.debug = True
        fuse.Fuse.__init__(self, [], args)

        self.root = FSRoot(sampler)
        
        self.cache = {}
        self.cache['/memory'] = sampler.memory
        self.cache['/disks'] = sampler.disks
        
        stat_home = os.stat(os.path.expanduser('~'))
        self.uid = stat_home[stat.ST_UID]
        self.gid = stat_home[stat.ST_GID]

    def stat_directory(self, path):
        if self.cache.get(path) is None:
            self.cache[path] = self.root.get_dir(path)
        return stat_dir(self.uid, self.gid)

    def get_parent(self, path):
        parent = os.path.dirname(path)
        return self.cache[parent]
        
    def get_file(self, path):
        if not samplermod.Sampler.is_filetype_supported(path):
            raiseException(errno.ENOENT)

        parent_dir = self.get_parent(path)
        file_name = os.path.basename(path)
        
        for child in parent_dir.get_children():
            if child.get_name() == file_name:
                return child
        return None

    def stat_file(self, path):
        cached = self.cache.get(path, None)
        if cached is not None:
            return cached
        
        file_obj = self.get_file(path)
        if file_obj is None:
            raiseException(errno.ENOENT)
        else:
            return stat_file(self.uid, self.gid, path)

    def getattr(self, path):
        print '*** getattr', path
        if fileutils.is_dirpath(path):
            return self.stat_directory(path)
        else:
            return self.stat_file(path)

    def getdir(self, path):
        print '*** getdir', path
        folder = self.cache[path]
        list =  [(child.get_name(), 0) for child in folder.get_children()]
        print repr(list)
        return list

    def mkdir(self, path, mode):
        print '*** mkdir', path, mode
        folder = self.root.mkdir(path)
        self.cache[path] = folder

    def open(self, path, flags):
        print '*** open', path, flags
        self.root.open(path, flags)

    def read(self, path, length, offset):
        print '*** read', path, length, offset
        return self.root.read(path, length, offset)

    def release(self, path, flags):
        print '*** release', path, flags
        self.root.close(path)

    def rename(self, oldPath, newPath):
        print '*** rename', oldPath, newPath
        raiseUnsupportedOperationException()

    def rmdir(self, path):
        print '*** rmdir', path
        self.cache[path].delete()
        del self.cache[path]

    def unlink(self, path):
        print '*** unlink', path
        file_obj = self.get_file(path)
        file_obj.delete()
        self.get_parent(path).refresh()

    def mknod(self, path, mode, dev):
        print '*** mknod ', path, mode, dev
        self.cache[path] = stat_file(self.uid, self.gid, path)
        self.root.mknod(path)
        self.get_parent(path).refresh()

    def write(self, path, buf, offset):
        print '*** write', path, len(buf), offset
        return self.root.write(path, buf, offset)

    def truncate(self, path, size): #IGNORE:W0212
        print "*** truncate ", path, size
        pass

def raiseUnsupportedOperationException():
    raiseException(errno.ENOSYS)

def raiseException(err):
    raise OSError(err, 'Exception occurred')

if __name__ == '__main__':
    # z48 = Devices.get_instance('mock_z48', None)
    z48 = Devices.get_instance('z48', 'usb')
    fs = AksyFS(z48)
    fs.mountpoint = '/tmp/aksy'
    fs.main()