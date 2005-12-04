import struct, sys, unittest
from aksy.devices.akai import sysex, sysex_types, sampler

class TestUserRef(unittest.TestCase):
    def setUp(self):
        if not hasattr(self, 'z48'):
            self.z48 = sampler.Sampler()
            self.z48.init()

    def testEncodeDecode(self):
        cmd = sysex.Command(sysex.Z48_ID, '\x20\x04', 'get_no_disks', (sysex_types.PAD, sysex_types.BYTE,),
            userref_type=sysex_types.USERREF)
        bytes = self.z48.execute(cmd, (), 0)
        length, request_id = sysex_types.USERREF.decode(bytes[3:])
        self.assertEquals(1, length)
        self.assertEquals(0, request_id)

        # this fails on Z48
        cmd = sysex.Command(sysex.Z48_ID, '\x20\x04', 'get_no_disks', (sysex_types.PAD, sysex_types.BYTE,),
            userref_type=sysex_types.USERREF)
        bytes = self.z48.execute(cmd, (), 126)
        length, request_id = sysex_types.USERREF.decode(bytes[3:])
        self.assertEquals(2, length)
        self.assertEquals(126, request_id)

        cmd = sysex.Command(sysex.S56K_ID, '\x10\x05', 'get_no_disks', (sysex_types.BYTE,),
            userref_type=sysex_types.S56K_USERREF)
        bytes = self.z48.execute(cmd, (), 16000)
        length, request_id = sysex_types.USERREF.decode(bytes[3:])
        self.assertEquals(3, length)
        self.assertEquals(16000, request_id)

    def tearDown(self):
        self.z48.close()

def test_suite():
    testloader = unittest.TestLoader()
    suite = testloader.loadTestsFromName('aksy.devices.akai.tests.test_sysex_integ')
    return suite