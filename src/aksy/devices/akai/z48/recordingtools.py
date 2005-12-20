
""" Python equivalent of akai section recordingtools

Methods to facilitate recording
"""

__author__ =  'Walco van Loon'
__version__=  '0.1'

import aksy.devices.akai.sysex,aksy.devices.akai.sysex_types

class Recordingtools:
    def __init__(self, z48):
        self.z48 = z48
        self.get_status_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x01', 'get_status', (), None)
        self.get_progress_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x02', 'get_progress', (), None)
        self.get_max_rec_time_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x03', 'get_max_rec_time', (), None)
        self.arm_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x10', 'arm', (), None)
        self.start_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x11', 'start', (), None)
        self.stop_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x12', 'stop', (), None)
        self.cancel_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x13', 'cancel', (), None)
        self.start_playing_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x20', 'start_playing', (), None)
        self.stop_playing_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x21', 'stop_playing', (), None)
        self.keep_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x22', 'keep', (), None)
        self.delete_cmd = aksy.devices.akai.sysex.Command('_', '\x30\x23', 'delete', (), None)
        self.set_input_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x01', 'set_input', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_mode_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x02', 'set_mode', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.enable_monitor_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x03', 'enable_monitor', (aksy.devices.akai.sysex_types.BOOL,), None)
        self.set_rec_time_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x04', 'set_rec_time', (aksy.devices.akai.sysex_types.DWORD,), None)
        self.set_orig_pitch_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x05', 'set_orig_pitch', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_threshold_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x06', 'set_threshold', (aksy.devices.akai.sysex_types.SBYTE,), None)
        self.set_trigger_src_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x07', 'set_trigger_src', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_bit_depth_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x08', 'set_bit_depth', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_prerec_time_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x09', 'set_prerec_time', (aksy.devices.akai.sysex_types.WORD,), None)
        self.set_dest_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x0A', 'set_dest', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_name_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x10', 'set_name', (aksy.devices.akai.sysex_types.STRING,), None)
        self.set_name_seed_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x11', 'set_name_seed', (aksy.devices.akai.sysex_types.STRING,), None)
        self.set_autorec_mode_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x12', 'set_autorec_mode', (aksy.devices.akai.sysex_types.BOOL,), None)
        self.set_autonormalize_cmd = aksy.devices.akai.sysex.Command('_', '\x32\x13', 'set_autonormalize', (aksy.devices.akai.sysex_types.BOOL,), None)
        self.get_input_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x01', 'get_input', (), None)
        self.get_mode_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x02', 'get_mode', (), None)
        self.get_monitor_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x03', 'get_monitor', (), None)
        self.get_rec_time_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x04', 'get_rec_time', (), None)
        self.get_pitch_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x05', 'get_pitch', (), None)
        self.get_threshold_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x06', 'get_threshold', (), None)
        self.get_trigger_src_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x07', 'get_trigger_src', (), None)
        self.get_bit_depth_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x08', 'get_bit_depth', (), None)
        self.get_prerec_time_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x09', 'get_prerec_time', (), None)
        self.get_dest_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x0A', 'get_dest', (), None)
        self.get_name_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x10', 'get_name', (), None)
        self.get_name_seed_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x11', 'get_name_seed', (), None)
        self.get_autorec_mode_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x12', 'get_autorec_mode', (), None)
        self.get_autonormalize_cmd = aksy.devices.akai.sysex.Command('_', '\x33\x13', 'get_autonormalize', (), None)

    def get_status(self):
        """Get Record Status

        Returns:
            aksy.devices.akai.sysex_types.BYTE
        """
        return self.z48.execute(self.get_status_cmd, ())

    def get_progress(self):
        """Get Record Progress

        Returns:
            aksy.devices.akai.sysex_types.DWORD
        """
        return self.z48.execute(self.get_progress_cmd, ())

    def get_max_rec_time(self):
        """Get Maximum Record Time

        Returns:
            aksy.devices.akai.sysex_types.DWORD
        """
        return self.z48.execute(self.get_max_rec_time_cmd, ())

    def arm(self):
        """Arm Recording
        """
        return self.z48.execute(self.arm_cmd, ())

    def start(self):
        """Start Recording
        """
        return self.z48.execute(self.start_cmd, ())

    def stop(self):
        """Stop Recording
        """
        return self.z48.execute(self.stop_cmd, ())

    def cancel(self):
        """Cancel Recording
        """
        return self.z48.execute(self.cancel_cmd, ())

    def start_playing(self):
        """Play Recorded Sample Start
        """
        return self.z48.execute(self.start_playing_cmd, ())

    def stop_playing(self):
        """Play Recorded Sample Stop
        """
        return self.z48.execute(self.stop_playing_cmd, ())

    def keep(self):
        """Keep Recorded Sample. Sample with name assigned above, is added to the list of available samples.
        """
        return self.z48.execute(self.keep_cmd, ())

    def delete(self):
        """Delete Recorded Sample
        """
        return self.z48.execute(self.delete_cmd, ())

    def set_input(self, arg0):
        """Set Input <Data1> = (0=ANALOGUE, 1=DIGITAL, 2=MAIN OUT 3=ADAT1/2, 4=ADAT3/4, 5=ADAT5/6, 6=ADAT7/8)
        """
        return self.z48.execute(self.set_input_cmd, (arg0, ))

    def set_mode(self, arg0):
        """Set Record Mode <Data1> = (0=STEREO, 1=MONO L, 2=MONO R, 3=L/R MIX)
        """
        return self.z48.execute(self.set_mode_cmd, (arg0, ))

    def enable_monitor(self, arg0):
        """Set Record Monitor
        """
        return self.z48.execute(self.enable_monitor_cmd, (arg0, ))

    def set_rec_time(self, arg0):
        """Set Record Time <Data1> = time in seconds. If <Data1> = 0, MANUAL mode is enabled.
        """
        return self.z48.execute(self.set_rec_time_cmd, (arg0, ))

    def set_orig_pitch(self, arg0):
        """Set Original Pitch 
        """
        return self.z48.execute(self.set_orig_pitch_cmd, (arg0, ))

    def set_threshold(self, arg0):
        """Set Threshold <Data1> = threshold in dB (-63,0)
        """
        return self.z48.execute(self.set_threshold_cmd, (arg0, ))

    def set_trigger_src(self, arg0):
        """Set Trigger Source (0=OFF, 1=AUDIO, 2=MIDI)
        """
        return self.z48.execute(self.set_trigger_src_cmd, (arg0, ))

    def set_bit_depth(self, arg0):
        """Set Bit Depth <Data1> = (0=16-bit, 1=24-bit)
        """
        return self.z48.execute(self.set_bit_depth_cmd, (arg0, ))

    def set_prerec_time(self, arg0):
        """Set Pre-recording Time <Data1> = time in ms
        """
        return self.z48.execute(self.set_prerec_time_cmd, (arg0, ))

    def set_dest(self, arg0):
        """Set Recording Detination <Data1> = (0=RAM, 1=DISK)
        """
        return self.z48.execute(self.set_dest_cmd, (arg0, ))

    def set_name(self, arg0):
        """Set Record Name
        """
        return self.z48.execute(self.set_name_cmd, (arg0, ))

    def set_name_seed(self, arg0):
        """Set Record Name Seed
        """
        return self.z48.execute(self.set_name_seed_cmd, (arg0, ))

    def set_autorec_mode(self, arg0):
        """Set Auto-Record Mode <Data1> = (0=OFF, 1=ON)
        """
        return self.z48.execute(self.set_autorec_mode_cmd, (arg0, ))

    def set_autonormalize(self, arg0):
        """Set Auto-Normalise Mode <Data1> = (0=OFF, 1=ON)
        """
        return self.z48.execute(self.set_autonormalize_cmd, (arg0, ))

    def get_input(self):
        """Get Input (0=ANALOGUE, 1=DIGITAL, 2=MAIN OUT, 3=ADAT1/2, 4=ADAT3/4, 5=ADAT5/6, 6=ADAT7/8)

        Returns:
            aksy.devices.akai.sysex_types.BYTE
        """
        return self.z48.execute(self.get_input_cmd, ())

    def get_mode(self):
        """Get Record Mode (0=STEREO, 1=MONO L, 2=MONO R, 3=L/R MIX)
        """
        return self.z48.execute(self.get_mode_cmd, ())

    def get_monitor(self):
        """Get Record Monitor <Reply> = (0=OFF, 1=ON)

        Returns:
            aksy.devices.akai.sysex_types.BOOL
        """
        return self.z48.execute(self.get_monitor_cmd, ())

    def get_rec_time(self):
        """Get Record Time <Reply> = time in seconds.

        Returns:
            aksy.devices.akai.sysex_types.DWORD
        """
        return self.z48.execute(self.get_rec_time_cmd, ())

    def get_pitch(self):
        """Get Original Pitch

        Returns:
            aksy.devices.akai.sysex_types.BYTE
        """
        return self.z48.execute(self.get_pitch_cmd, ())

    def get_threshold(self):
        """Get Threshold <Reply> = threshold in dB -63,0

        Returns:
            aksy.devices.akai.sysex_types.SBYTE
        """
        return self.z48.execute(self.get_threshold_cmd, ())

    def get_trigger_src(self):
        """Get Trigger Source <Reply> = (0=OFF, 1=AUDIO, 2=MIDI)

        Returns:
            aksy.devices.akai.sysex_types.BYTE
        """
        return self.z48.execute(self.get_trigger_src_cmd, ())

    def get_bit_depth(self):
        """Get Bit Depth <Reply> = (0=16-bit, 1=24-bit)

        Returns:
            aksy.devices.akai.sysex_types.BYTE
        """
        return self.z48.execute(self.get_bit_depth_cmd, ())

    def get_prerec_time(self):
        """Get Pre-recording Time <Reply> = time in ms

        Returns:
            aksy.devices.akai.sysex_types.WORD
        """
        return self.z48.execute(self.get_prerec_time_cmd, ())

    def get_dest(self):
        """Get Recording Destination <Reply> = (0=RAM, 1=DISK)

        Returns:
            aksy.devices.akai.sysex_types.BYTE
        """
        return self.z48.execute(self.get_dest_cmd, ())

    def get_name(self):
        """Get Record Name

        Returns:
            aksy.devices.akai.sysex_types.STRING
        """
        return self.z48.execute(self.get_name_cmd, ())

    def get_name_seed(self):
        """Get Record Name Seed

        Returns:
            aksy.devices.akai.sysex_types.STRING
        """
        return self.z48.execute(self.get_name_seed_cmd, ())

    def get_autorec_mode(self):
        """Get Auto-Record Mode <Reply> = (0=OFF, 1=ON)

        Returns:
            aksy.devices.akai.sysex_types.BOOL
        """
        return self.z48.execute(self.get_autorec_mode_cmd, ())

    def get_autonormalize(self):
        """Get Auto-Normalise Mode <Reply> = (0=OFF, 1=ON)

        Returns:
            aksy.devices.akai.sysex_types.BOOL
        """
        return self.z48.execute(self.get_autonormalize_cmd, ())

