from aksyxusb import Z48Sampler
from sysex import Request, Reply 
import sysex
import aksysdisktools, program_main
import struct
import sys,time


class Z48(Z48Sampler):
    """Models a Z4 or Z8 sampler.

    You can use it like this:
    >>> z = Z48()
    >>> z.init()
    >>> time.sleep(1) 
    >>> #z.get_no_disks()
    1

    >>> z.get_disklist() 
    (512, 1, 2, 0, 1, 'Z48 & MPC4K')

    >>> z.select_disk(1024) 
    >>> z.set_curr_folder('') 
    >>> # z.create_subfolder('AUTOLOAD') 
    >>> z.set_curr_folder('AUTOLOAD') 

    >>> # z.get('Ride 1.wav', '/home/walco/dev/aksy' ) 
    >>> # z.put('/home/walco/dev/aksy/Ride 1.wav', 'Ride 1 copy.wav')

    # the number can differ of course...
    >>> # z.get_no_subfolders() 
    21
    >>> # z.get_filenames() 

    >>> z.get_subfolder_names() 
    ()
    >>> z.close_usb()
    """
    MEMORY = 0
    DISK = 1

    def __init__(self):
        Z48Sampler.__init__(self)
        self.disktools = aksysdisktools.DiskTools(self)
        self.program_main = program_main.ProgramMain(self)

    def init(self):
        """Initializes the connection with the sampler
        """
        Z48Sampler.init_usb(self)

        # disable checksums (not enabled per default)
        # msg = "\xf0\x47\x5f\x00\x04\x00\xf7";
        # result_bytes = self._execute('\x10' + struct.pack('B', len(msg) + '\x00' + msg)

        # disable confirmation messages
        # msg = "\xf0\x47\x5f\x00\x00\x01\x00\xf7";
        # result_bytes = self._execute('\x10' + struct.pack('B', len(msg)) + '\x00' + msg)
                                                                                                                                                           
        # disable sync
        msg = "\xf0\x47\x5f\x00\x00\x03\x00\xf7";
        result_bytes = self._execute('\x10' + struct.pack('B', len(msg)) + '\x00' + msg)
                                                                                                                                                           
    def close(self):
        """Closes the connection with the sampler
        """
        Z48Sampler.close_usb(self)

    def get(self, filename, destpath):
        """Gets a file from the sampler, overwriting it if it already exists.
        """
        # fix this call
        Z48Sampler._get(self, sysex._to_byte_string(sysex.STRING, filename), destpath + '/' + filename)

    def put(self, path, remote_name, destination=MEMORY):
        """Transfers a file to the sampler, overwriting it if it already exists.
        Default destination is memory
        """
        Z48Sampler._put(self, path, sysex._to_byte_string(sysex.STRING, remote_name), destination)

    def execute(self, command, args, z48id=None, userref=None):
        request = Request(command, args, z48id, userref)
        sys.stderr.writelines("Request: %s\n" % repr(request))
        result_bytes = self._execute('\x10' + struct.pack('B', len(request.get_bytes())) + '\x00' + request.get_bytes())
        sys.stderr.writelines("Length of reply: %i\n" % len(result_bytes))
        result = Reply(result_bytes, command.reply_spec, z48id, userref)
        sys.stderr.writelines("Reply: %s\n" % repr(result))
        return result.parse()

if __name__ == "__main__":
    import doctest, sys
    doctest.testmod(sys.modules[__name__])
