
""" Python equivalent of akai section programtools

Methods to manipulate sampler programs
"""

__author__ =  'Walco van Loon'
__version__=  '$Rev$'

from aksy.devices.akai.sysex import Command

import aksy.devices.akai.sysex_types

class Programtools:
    def __init__(self, z48):
        self.z48 = z48
        self.get_no_items_cmd = Command('_', '\x14\x01', 'get_no_items', (), None)
        self.get_handles_cmd = Command('_', '\x14\x02\x00', 'get_handles', (), None)
        self.get_names_cmd = Command('_', '\x14\x02\x01', 'get_names', (), None)
        self.get_handles_names_cmd = Command('_', '\x14\x02\x02', 'get_handles_names', (), None)
        self.get_modified_cmd = Command('_', '\x14\x02\x03', 'get_modified', (), None)
        self.set_curr_by_handle_cmd = Command('_', '\x14\x03', 'set_curr_by_handle', (aksy.devices.akai.sysex_types.DWORD,), None)
        self.set_curr_by_name_cmd = Command('_', '\x14\x04', 'set_curr_by_name', (aksy.devices.akai.sysex_types.STRING,), None)
        self.get_curr_handle_cmd = Command('_', '\x14\x05', 'get_curr_handle', (), None)
        self.get_curr_name_cmd = Command('_', '\x14\x06', 'get_curr_name', (), None)
        self.get_name_by_handle_cmd = Command('_', '\x14\x07', 'get_name_by_handle', (aksy.devices.akai.sysex_types.DWORD,), None)
        self.get_handle_by_name_cmd = Command('_', '\x14\x08', 'get_handle_by_name', (aksy.devices.akai.sysex_types.STRING,), None)
        self.delete_all_cmd = Command('_', '\x14\x09', 'delete_all', (), None)
        self.delete_curr_cmd = Command('_', '\x14\x0A', 'delete_curr', (), None)
        self.delete_by_handle_cmd = Command('_', '\x14\x0B', 'delete_by_handle', (aksy.devices.akai.sysex_types.DWORD,), None)
        self.rename_curr_cmd = Command('_', '\x14\x0C', 'rename_curr', (aksy.devices.akai.sysex_types.STRING,), None)
        self.rename_by_handle_cmd = Command('_', '\x14\x0D', 'rename_by_handle', (aksy.devices.akai.sysex_types.DWORD, aksy.devices.akai.sysex_types.STRING), None)
        self.tag_cmd = Command('_', '\x14\x0E', 'tag', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BYTE), None)
        self.get_tag_bitmap_cmd = Command('_', '\x14\x0F', 'get_tag_bitmap', (), None)
        self.get_modified_name_cmd = Command('_', '\x14\x10', 'get_modified_name', (), None)
        self.get_modified_state_cmd = Command('_', '\x14\x11', 'get_modified_state', (), None)
        self.delete_tagged_cmd = Command('_', '\x14\x18', 'delete_tagged', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.create_new_cmd = Command('_', '\x14\x40', 'create_new', (aksy.devices.akai.sysex_types.WORD, aksy.devices.akai.sysex_types.STRING), None)
        self.add_keygroups_to_current_cmd = Command('_', '\x14\x41', 'add_keygroups_to_current', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.delete_keygroup_cmd = Command('_', '\x14\x42', 'delete_keygroup', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.delete_blank_keygroups_cmd = Command('_', '\x14\x43', 'delete_blank_keygroups', (), None)
        self.arrange_keygroups_cmd = Command('_', '\x14\x44', 'arrange_keygroups', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.copy_keygroup_cmd = Command('_', '\x14\x45', 'copy_keygroup', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.copy_program_cmd = Command('_', '\x14\x48', 'copy_program', (aksy.devices.akai.sysex_types.STRING,), None)
        self.merge_programs_cmd = Command('_', '\x14\x48', 'merge_programs', (aksy.devices.akai.sysex_types.DWORD, aksy.devices.akai.sysex_types.DWORD), None)
        self.add_keygroup_sample_cmd = Command('_', '\x14\x4A', 'add_keygroup_sample', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BOOL, aksy.devices.akai.sysex_types.STRING), None)
        self.copy_temperament_to_user_cmd = Command('_', '\x14\x50', 'copy_temperament_to_user', (), None)
        self.get_no_modulation_connections_cmd = Command('_', '\x14\x54', 'get_no_modulation_connections', (), None)
        self.get_no_modulation_sources_cmd = Command('_', '\x14\x55', 'get_no_modulation_sources', (), None)
        self.no_modulation_destinations_cmd = Command('_', '\x14\x56', 'no_modulation_destinations', (), None)
        self.get_name_modulation_source_cmd = Command('_', '\x14\x57', 'get_name_modulation_source', (aksy.devices.akai.sysex_types.WORD,), None)
        self.get_name_modulation_dest_cmd = Command('_', '\x14\x58', 'get_name_modulation_dest', (aksy.devices.akai.sysex_types.WORD,), None)
        self.get_group_id_cmd = Command('_', '\x17\x01', 'get_group_id', (), None)
        self.get_type_cmd = Command('_', '\x17\x03', 'get_type', (), None)
        self.get_genre_cmd = Command('_', '\x17\x04', 'get_genre', (), None)
        self.get_program_no_cmd = Command('_', '\x17\x08', 'get_program_no', (), None)
        self.get_no_keygroups_cmd = Command('_', '\x17\x09', 'get_no_keygroups', (), None)
        self.get_keygroup_xfade_cmd = Command('_', '\x17\x0A', 'get_keygroup_xfade', (), None)
        self.get_keygroup_xfade_type_cmd = Command('_', '\x17\x0B', 'get_keygroup_xfade_type', (), None)
        self.get_level_cmd = Command('_', '\x17\x0C', 'get_level', (), None)
        self.get_polyphony_cmd = Command('_', '\x17\x10', 'get_polyphony', (), None)
        self.get_reassignment_method_cmd = Command('_', '\x17\x11', 'get_reassignment_method', (), None)
        self.get_softpedal_loudness_reduction_cmd = Command('_', '\x17\x12', 'get_softpedal_loudness_reduction', (), None)
        self.get_softpedal_attack_stretch_cmd = Command('_', '\x17\x13', 'get_softpedal_attack_stretch', (), None)
        self.get_softpedal_filter_close_cmd = Command('_', '\x17\x14', 'get_softpedal_filter_close', (), None)
        self.get_midi_transpose_cmd = Command('_', '\x17\x15', 'get_midi_transpose', (), None)
        self.get_mpc_pad_assignment_cmd = Command('_', '\x17\x18', 'get_mpc_pad_assignment', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.get_modulation_connection_cmd = Command('_', '\x17\x20', 'get_modulation_connection', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD), None)
        self.get_modulation_source_type_cmd = Command('_', '\x17\x21', 'get_modulation_source_type', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.get_modulation_destination_type_cmd = Command('_', '\x17\x22', 'get_modulation_destination_type', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.get_modulation_level_cmd = Command('_', '\x17\x23', 'get_modulation_level', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD), None)
        self.get_midi_controller_number_cmd = Command('_', '\x17\x24', 'get_midi_controller_number', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_group_id_cmd = Command('_', '\x16\x01', 'set_group_id', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_type_cmd = Command('_', '\x16\x03', 'set_type', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_genre_cmd = Command('_', '\x16\x04', 'set_genre', (aksy.devices.akai.sysex_types.STRING,), None)
        self.set_program_no_cmd = Command('_', '\x16\x08', 'set_program_no', (aksy.devices.akai.sysex_types.WORD,), None)
        self.set_no_keygroups_cmd = Command('_', '\x16\x09', 'set_no_keygroups', (aksy.devices.akai.sysex_types.WORD,), None)
        self.set_keygroup_xfade_cmd = Command('_', '\x16\x0A', 'set_keygroup_xfade', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_keygroup_xfade_type_cmd = Command('_', '\x16\x0B', 'set_keygroup_xfade_type', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_level_cmd = Command('_', '\x16\x0C', 'set_level', (aksy.devices.akai.sysex_types.SWORD,), None)
        self.set_polyphony_cmd = Command('_', '\x16\x10', 'set_polyphony', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_reassignment_method_cmd = Command('_', '\x16\x11', 'set_reassignment_method', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_softpedal_loudness_reduction_cmd = Command('_', '\x16\x12', 'set_softpedal_loudness_reduction', (), None)
        self.set_softpedal_attack_stretch_cmd = Command('_', '\x16\x13', 'set_softpedal_attack_stretch', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_softpedal_filter_close_cmd = Command('_', '\x16\x14', 'set_softpedal_filter_close', (aksy.devices.akai.sysex_types.BYTE,), None)
        self.set_midi_transpose_cmd = Command('_', '\x16\x15', 'set_midi_transpose', (aksy.devices.akai.sysex_types.SBYTE,), None)
        self.set_mpc_pad_assignment_cmd = Command('_', '\x16\x18', 'set_mpc_pad_assignment', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BYTE), None)
        self.set_modulation_conn_cmd = Command('_', '\x16\x20', 'set_modulation_conn', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD, aksy.devices.akai.sysex_types.WORD, aksy.devices.akai.sysex_types.WORD, aksy.devices.akai.sysex_types.SBYTE), None)
        self.set_modulation_src_cmd = Command('_', '\x16\x21', 'set_modulation_src', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD), None)
        self.set_modulation_dest_cmd = Command('_', '\x16\x22', 'set_modulation_dest', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD), None)
        self.set_modulation_level_cmd = Command('_', '\x16\x23', 'set_modulation_level', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD, aksy.devices.akai.sysex_types.SBYTE), None)
        self.set_midi_ctrl_no_cmd = Command('_', '\x16\x24', 'set_midi_ctrl_no', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BYTE), None)
        self.set_edit_keygroup_cmd = Command('_', '\x16\x25', 'set_edit_keygroup', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.WORD), None)
        self.set_edit_kegyroup_modulation_level_cmd = Command('_', '\x16\x26', 'set_edit_kegyroup_modulation_level', (aksy.devices.akai.sysex_types.BYTE, aksy.devices.akai.sysex_types.BYTE), None)

    def get_no_items(self):
        """Get number of items in memory
        """
        return self.z48.execute(self.get_no_items_cmd, ())

    def get_handles(self):
        """Get list of info for all items: 0=list of handles;

        Returns:
            DWORD
        """
        return self.z48.execute(self.get_handles_cmd, ())

    def get_names(self):
        """Get list of info for all items: 1=list of names

        Returns:
            STRINGARRAY
        """
        return self.z48.execute(self.get_names_cmd, ())

    def get_handles_names(self):
        """Get list of info for all items: 2=list of handle+name;

        Returns:
            HANDLENAMEARRAY
        """
        return self.z48.execute(self.get_handles_names_cmd, ())

    def get_modified(self):
        """Get list of info for all items: 3=list of handle+modified/tagged name

        Returns:
            HANDLENAMEARRAY
        """
        return self.z48.execute(self.get_modified_cmd, ())

    def set_curr_by_handle(self, arg0):
        """Select current item by handle
        """
        return self.z48.execute(self.set_curr_by_handle_cmd, (arg0, ))

    def set_curr_by_name(self, arg0):
        """Select current item by name
        """
        return self.z48.execute(self.set_curr_by_name_cmd, (arg0, ))

    def get_curr_handle(self):
        """Get handle of current item

        Returns:
            DWORD
        """
        return self.z48.execute(self.get_curr_handle_cmd, ())

    def get_curr_name(self):
        """Get name of current item

        Returns:
            STRING
        """
        return self.z48.execute(self.get_curr_name_cmd, ())

    def get_name_by_handle(self, arg0):
        """Get item name from handle

        Returns:
            STRING
        """
        return self.z48.execute(self.get_name_by_handle_cmd, (arg0, ))

    def get_handle_by_name(self, arg0):
        """Get item handle from name

        Returns:
            DWORD
        """
        return self.z48.execute(self.get_handle_by_name_cmd, (arg0, ))

    def delete_all(self):
        """Delete ALL items from memory
        """
        return self.z48.execute(self.delete_all_cmd, ())

    def delete_curr(self):
        """Delete current item from memory
        """
        return self.z48.execute(self.delete_curr_cmd, ())

    def delete_by_handle(self, arg0):
        """Delete item represented by handle <Data1>
        """
        return self.z48.execute(self.delete_by_handle_cmd, (arg0, ))

    def rename_curr(self, arg0):
        """Rename current item
        """
        return self.z48.execute(self.rename_curr_cmd, (arg0, ))

    def rename_by_handle(self, arg0, arg1):
        """Rename item represented by handle <Data1>
        """
        return self.z48.execute(self.rename_by_handle_cmd, (arg0, arg1, ))

    def tag(self, arg0, arg1):
        """Set Tag Bit <Data1> = bit to set(0-7), <Data2> = (0=OFF, 1=ON), Data3> = (0=CURRENT, 1=ALL)
        """
        return self.z48.execute(self.tag_cmd, (arg0, arg1, ))

    def get_tag_bitmap(self):
        """Get Tag Bitmap

        Returns:
            WORD
        """
        return self.z48.execute(self.get_tag_bitmap_cmd, ())

    def get_modified_name(self):
        """Get name of current item with modified/tagged info.
        """
        return self.z48.execute(self.get_modified_name_cmd, ())

    def get_modified_state(self):
        """Get modified state of current item.

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_modified_state_cmd, ())

    def delete_tagged(self, arg0):
        """Delete tagged items <Data1> = tag bit
        """
        return self.z48.execute(self.delete_tagged_cmd, (arg0, ))

    def create_new(self, arg0, arg1):
        """Create New Program <Data1> = number of keygroups;<Data2> = name.
        """
        return self.z48.execute(self.create_new_cmd, (arg0, arg1, ))

    def add_keygroups_to_current(self, arg0):
        """Add Keygroups to Program <Data1> = number of keygroups to add
        """
        return self.z48.execute(self.add_keygroups_to_current_cmd, (arg0, ))

    def delete_keygroup(self, arg0):
        """Delete Keygroup (keygroup index)
        """
        return self.z48.execute(self.delete_keygroup_cmd, (arg0, ))

    def delete_blank_keygroups(self):
        """Delete Blank Keygroups
        """
        return self.z48.execute(self.delete_blank_keygroups_cmd, ())

    def arrange_keygroups(self, arg0):
        """Arrange Keygroups (note 0:orig 1:low 2:high)
        """
        return self.z48.execute(self.arrange_keygroups_cmd, (arg0, ))

    def copy_keygroup(self, arg0):
        """Copy Keygroup (keygroup  index)
        """
        return self.z48.execute(self.copy_keygroup_cmd, (arg0, ))

    def copy_program(self, arg0):
        """Copy Program (program name)
        """
        return self.z48.execute(self.copy_program_cmd, (arg0, ))

    def merge_programs(self, arg0, arg1):
        """Merge Programs (program handle1, handle2)
        """
        return self.z48.execute(self.merge_programs_cmd, (arg0, arg1, ))

    def add_keygroup_sample(self, arg0, arg1, arg2, arg3, arg4):
        """Add Keygroup Sample (low note, high note, zone, keytrack, sample name)
        """
        return self.z48.execute(self.add_keygroup_sample_cmd, (arg0, arg1, arg2, arg3, arg4, ))

    def copy_temperament_to_user(self):
        """Copies Program Temperament to User Temperament
        """
        return self.z48.execute(self.copy_temperament_to_user_cmd, ())

    def get_no_modulation_connections(self):
        """Get number of Modulation Connections

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_no_modulation_connections_cmd, ())

    def get_no_modulation_sources(self):
        """Get number of Modulation Sources

        Returns:
            WORD
        """
        return self.z48.execute(self.get_no_modulation_sources_cmd, ())

    def no_modulation_destinations(self):
        """Get number of Modulation Destinations

        Returns:
            WORD
        """
        return self.z48.execute(self.no_modulation_destinations_cmd, ())

    def get_name_modulation_source(self, arg0):
        """Get Name of Modulation Source (source index)

        Returns:
            WORD
        """
        return self.z48.execute(self.get_name_modulation_source_cmd, (arg0, ))

    def get_name_modulation_dest(self, arg0):
        """Get Name of Modulation Destination (dest index)

        Returns:
            WORD
        """
        return self.z48.execute(self.get_name_modulation_dest_cmd, (arg0, ))

    def get_group_id(self):
        """Get Group ID

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_group_id_cmd, ())

    def get_type(self):
        """Get Program Type <Reply> = (0=KEYGROUP, 1=DRUM)

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_type_cmd, ())

    def get_genre(self):
        """Get Genre

        Returns:
            STRING
        """
        return self.z48.execute(self.get_genre_cmd, ())

    def get_program_no(self):
        """Get Program Number <Reply1> = (0=OFF, 1�128)

        Returns:
            WORD
        """
        return self.z48.execute(self.get_program_no_cmd, ())

    def get_no_keygroups(self):
        """Get Number of keygroups

        Returns:
            WORD
        """
        return self.z48.execute(self.get_no_keygroups_cmd, ())

    def get_keygroup_xfade(self):
        """Get Keygroup Crossfade <Reply1> = (0=OFF, 1=ON)

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_keygroup_xfade_cmd, ())

    def get_keygroup_xfade_type(self):
        """Get Keygroup Crossfade type <Reply1> = (0=LIN, 1=EXP, 2=LOG)

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_keygroup_xfade_type_cmd, ())

    def get_level(self):
        """Get Program Level <Reply1> = level in 10�dB

        Returns:
            SWORD
        """
        return self.z48.execute(self.get_level_cmd, ())

    def get_polyphony(self):
        """Get Polyphony

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_polyphony_cmd, ())

    def get_reassignment_method(self):
        """Get Reassignment <Reply1> = (0=QUIETEST, 1=OLDEST)

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_reassignment_method_cmd, ())

    def get_softpedal_loudness_reduction(self):
        """Soft Pedal Loudness Reduction

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_softpedal_loudness_reduction_cmd, ())

    def get_softpedal_attack_stretch(self):
        """Soft Pedal Attack Stretch

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_softpedal_attack_stretch_cmd, ())

    def get_softpedal_filter_close(self):
        """Soft Pedal Filter Close

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_softpedal_filter_close_cmd, ())

    def get_midi_transpose(self):
        """Get midi transpose

        Returns:
            SBYTE
        """
        return self.z48.execute(self.get_midi_transpose_cmd, ())

    def get_mpc_pad_assignment(self, arg0):
        """Get the midi pad assignment (pad index)

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_mpc_pad_assignment_cmd, (arg0, ))

    def get_modulation_connection(self, arg0, arg1):
        """Get the modulation connection(pin number, keygroup for level - note 0 or 'all' is not supported)

        Returns:
            WORD
            WORD
            SBYTE
        """
        return self.z48.execute(self.get_modulation_connection_cmd, (arg0, arg1, ))

    def get_modulation_source_type(self, arg0):
        """Get the modulation source type (pin number)

        Returns:
            WORD
        """
        return self.z48.execute(self.get_modulation_source_type_cmd, (arg0, ))

    def get_modulation_destination_type(self, arg0):
        """Get the modulation dest type (pin number)

        Returns:
            WORD
        """
        return self.z48.execute(self.get_modulation_destination_type_cmd, (arg0, ))

    def get_modulation_level(self, arg0, arg1):
        """Get the modulation level (pin number, keygroup number - note 0 or 'all' is not supported)

        Returns:
            SBYTE
        """
        return self.z48.execute(self.get_modulation_level_cmd, (arg0, arg1, ))

    def get_midi_controller_number(self, arg0):
        """Get the midi controller number (pin number - only available if source=CTRL)

        Returns:
            BYTE
        """
        return self.z48.execute(self.get_midi_controller_number_cmd, (arg0, ))

    def set_group_id(self, arg0):
        """Set Group ID
        """
        return self.z48.execute(self.set_group_id_cmd, (arg0, ))

    def set_type(self, arg0):
        """Set Program Type <Data1> = (0=KEYGROUP, 1=DRUM)
        """
        return self.z48.execute(self.set_type_cmd, (arg0, ))

    def set_genre(self, arg0):
        """Set Genre
        """
        return self.z48.execute(self.set_genre_cmd, (arg0, ))

    def set_program_no(self, arg0):
        """Set Program Number <Data1> = (0=OFF, 1�128)
        """
        return self.z48.execute(self.set_program_no_cmd, (arg0, ))

    def set_no_keygroups(self, arg0):
        """Set Number of keygroups
        """
        return self.z48.execute(self.set_no_keygroups_cmd, (arg0, ))

    def set_keygroup_xfade(self, arg0):
        """Set Keygroup Crossfade <Data1> = (0=OFF, 1=ON)
        """
        return self.z48.execute(self.set_keygroup_xfade_cmd, (arg0, ))

    def set_keygroup_xfade_type(self, arg0):
        """Set Keygroup Crossfade type <Data1> = (0=LIN, 1=EXP, 2=LOG)
        """
        return self.z48.execute(self.set_keygroup_xfade_type_cmd, (arg0, ))

    def set_level(self, arg0):
        """Set Program Level <Data1> = level in 10�dB (-600 � +60)
        """
        return self.z48.execute(self.set_level_cmd, (arg0, ))

    def set_polyphony(self, arg0):
        """Set Polyphony
        """
        return self.z48.execute(self.set_polyphony_cmd, (arg0, ))

    def set_reassignment_method(self, arg0):
        """Set Reassignment <Data1> = (0=QUIETEST, 1=OLDEST)
        """
        return self.z48.execute(self.set_reassignment_method_cmd, (arg0, ))

    def set_softpedal_loudness_reduction(self):
        """Soft Pedal Loudness Reduction
        """
        return self.z48.execute(self.set_softpedal_loudness_reduction_cmd, ())

    def set_softpedal_attack_stretch(self, arg0):
        """Soft Pedal Attack Stretch
        """
        return self.z48.execute(self.set_softpedal_attack_stretch_cmd, (arg0, ))

    def set_softpedal_filter_close(self, arg0):
        """Soft Pedal Filter Close
        """
        return self.z48.execute(self.set_softpedal_filter_close_cmd, (arg0, ))

    def set_midi_transpose(self, arg0):
        """Midi Transpose (-36 � +36)
        """
        return self.z48.execute(self.set_midi_transpose_cmd, (arg0, ))

    def set_mpc_pad_assignment(self, arg0, arg1):
        """MPC pad assignment <Data1> = pad, <Data2> = note
        """
        return self.z48.execute(self.set_mpc_pad_assignment_cmd, (arg0, arg1, ))

    def set_modulation_conn(self, arg0, arg1, arg2, arg3, arg4):
        """Set Modulation Connection <Data1> = connection (pin) number;<Data2> = keygroup number (0=ALL, 1�128=KEYGROUP) <Data3> = source (see Table 24); <Data4> = destination (see Table 25); <Data5> = level.  If Source or Destination is zero, the connection will be cleared.
        """
        return self.z48.execute(self.set_modulation_conn_cmd, (arg0, arg1, arg2, arg3, arg4, ))

    def set_modulation_src(self, arg0, arg1):
        """Set Modulation Source (see Table 24)
        """
        return self.z48.execute(self.set_modulation_src_cmd, (arg0, arg1, ))

    def set_modulation_dest(self, arg0, arg1):
        """Set Modulation Destination (see Table 25)
        """
        return self.z48.execute(self.set_modulation_dest_cmd, (arg0, arg1, ))

    def set_modulation_level(self, arg0, arg1, arg2):
        """Set Modulation Level <Data1> = pin number; <Data2> = (0=ALL, 1�128=KEYGROUP); <Data3> = level
        """
        return self.z48.execute(self.set_modulation_level_cmd, (arg0, arg1, arg2, ))

    def set_midi_ctrl_no(self, arg0, arg1):
        """Set MIDI controller number (only used if Source = CTRL)
        """
        return self.z48.execute(self.set_midi_ctrl_no_cmd, (arg0, arg1, ))

    def set_edit_keygroup(self, arg0, arg1):
        """Set Edit Keygroup (used to edit level) <Data2> = Edit Keygroup
        """
        return self.z48.execute(self.set_edit_keygroup_cmd, (arg0, arg1, ))

    def set_edit_kegyroup_modulation_level(self, arg0, arg1):
        """Set Modulation Level of Edit Keygroup
        """
        return self.z48.execute(self.set_edit_kegyroup_modulation_level_cmd, (arg0, arg1, ))

