import re

RE_MULTI = re.compile("\.[aA][kK][mM]$")
RE_PROGRAM = re.compile("\.[aA][kK][pP]$")
RE_SAMPLE = re.compile("\.[wW][aA][vV]$")

    # TODO: move these objects to their respective 
    # modules once the generated classes become
    # stable; the passing in of section refs can
    # then be removed.
class Disk(object):
    def __init__(self, (handle, disktype, fstype, disk_id, writable, name)):
        self.handle = handle
        self.disktype = disktype
        self.fstype = fstype
        self.disk_id = disk_id
        self.writable = writable
        self.name = name

class Folder(object):
    def __init__(self, disktools, name):

        self.name = name
        self.disktools = disktools

        disktools.set_curr_folder(name)

    def get_children(self):
        """
        """
        children = [ Folder(subfolder) for subfolder in
            self.disktools.get_subfolder_names() ]
        files = [ File(disktools, name) for name in 
            disktools.get_filenames() ]

        children.extend(files)
        return children


class File(object):

    def __init__(self, disktools, name=None):
        """Initializes a file object - should not be called directly, use 
        getInstance instead.
        """
        self.disktools = disktools
        self.name = name

    def getInstance(disktools, name=None):
        """Initializes a program from a  name
        """
        if RE_MULTI.search(name) is not None:
            return Multi(disktools, name)
        elif RE_PROGRAM.search(name) is not None:
            return Program(disktools, name)
        elif RE_SAMPLE.search(name) is not None:
            return Sample(disktools, name)
        else:
            raise NotImplementedError("No support for file type: ", name) 

    def get_modified(self):
        """Returns True if this program has has been modified
        """

    def get_used_by(self):
        """Returns the parent using this file
        """

    def get_children(self):
        """
        """
        raise NotImplementedError

    def get_children(self):
        """
        """
        raise NotImplementedError

class Multi(File):
    def get_used_by(self):
        return None

    def get_children(self):
        """Returns the programs used by this multi
        """

class Program(File):
    def get_used_by(self):
        """Returns the multi(s) using this program
        """

    def get_children(self):
        """Returns the samples used by this program
        """

class Sample(File):
    def get_used_by(self):
        """Returns the pogram(s) using this file
        """

    def get_children(self):
        """Returns the samples used by this program
        """
        return None
