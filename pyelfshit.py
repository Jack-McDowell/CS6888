#-------------------------------------------------------------------------------
# elftools example: dwarf_location_info.py
#
# Examine DIE entries which have either location list values or location
# expression values and decode that information.
#
# Location information can either be completely contained within a DIE
# (using 'DW_FORM_exprloc' in DWARFv4 or 'DW_FORM_block1' in earlier
# versions) or be a reference to a location list contained within
# the .debug_loc section (using 'DW_FORM_sec_offset' in DWARFv4 or
# 'DW_FORM_data4' / 'DW_FORM_data8' in earlier versions).
#
# The LocationParser object parses the DIE attributes and handles both
# formats.
#
# The directory 'test/testfiles_for_location_info' contains test files with
# location information represented in both DWARFv4 and DWARFv2 forms.
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------------
from __future__ import print_function
import sys

# If pyelftools is not installed, the example can also run from the root or
# examples/ dir of the source distribution.
sys.path[0:0] = ['.', '..']

from elftools.common.py3compat import itervalues
from elftools.elf.elffile import ELFFile
from elftools.dwarf.descriptions import (
    describe_DWARF_expr, set_global_machine_arch)
from elftools.dwarf.locationlists import (
    LocationEntry, LocationExpr, LocationParser)
from elftools.dwarf.dwarf_expr import DWARFExprParser

def get_var_offset(filename, function_name, var_name):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)

        if not elffile.has_dwarf_info():
            print('  file has no DWARF info')
            return

        # get_dwarf_info returns a DWARFInfo context object, which is the
        # starting point for all DWARF-based processing in pyelftools.
        dwarfinfo = elffile.get_dwarf_info()

        # The location lists are extracted by DWARFInfo from the .debug_loc
        # section, and returned here as a LocationLists object.
        location_lists = dwarfinfo.location_lists()

        # This is required for the descriptions module to correctly decode
        # register names contained in DWARF expressions.
        set_global_machine_arch(elffile.get_machine_arch())

        # Create a LocationParser object that parses the DIE attributes and
        # creates objects representing the actual location information.
        loc_parser = LocationParser(location_lists)

        for CU in dwarfinfo.iter_CUs():
            # DWARFInfo allows to iterate over the compile units contained in
            # the .debug_info section. CU is a CompileUnit object, with some
            # computed attributes (such as its offset in the section) and
            # a header which conforms to the DWARF standard. The access to
            # header elements is, as usual, via item-lookup.

            # A CU provides a simple API to iterate over all the DIEs in it.
            for DIE in CU.iter_DIEs():
                # Find the function
                if DIE.tag == "DW_TAG_subprogram":
                    fname = ""
                    for attr in itervalues(DIE.attributes):
                        if attr.name == "DW_AT_name":
                            fname = attr.value
                    if fname == function_name:
                        for CHILD in DIE.iter_children():
                            if CHILD.tag == "DW_TAG_variable" or CHILD.tag == "DW_TAG_formal_parameter":
                                right_name = False
                                location = 0
                                for attr in itervalues(CHILD.attributes):
                                    if attr.name == "DW_AT_name":
                                        if attr.value == var_name:
                                            right_name = True
                                    # Check if this attribute contains location information
                                    if attr.name == "DW_AT_location":
                                        loc = loc_parser.parse_from_attribute(attr,
                                                                              CU['version'])
                                        if isinstance(loc, LocationExpr):
                                            parser = DWARFExprParser(dwarfinfo.structs)
                                            parsed = parser.parse_expr(loc.loc_expr)
                                            for op in parsed:
                                                if op.op_name == 'DW_OP_fbreg':
                                                    location = op.args[0]
                                if right_name:
                                    return location

def get_var_name(filename, function_name, offset):
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)

        if not elffile.has_dwarf_info():
            print('  file has no DWARF info')
            return

        # get_dwarf_info returns a DWARFInfo context object, which is the
        # starting point for all DWARF-based processing in pyelftools.
        dwarfinfo = elffile.get_dwarf_info()

        # The location lists are extracted by DWARFInfo from the .debug_loc
        # section, and returned here as a LocationLists object.
        location_lists = dwarfinfo.location_lists()

        # This is required for the descriptions module to correctly decode
        # register names contained in DWARF expressions.
        set_global_machine_arch(elffile.get_machine_arch())

        # Create a LocationParser object that parses the DIE attributes and
        # creates objects representing the actual location information.
        loc_parser = LocationParser(location_lists)

        for CU in dwarfinfo.iter_CUs():
            # DWARFInfo allows to iterate over the compile units contained in
            # the .debug_info section. CU is a CompileUnit object, with some
            # computed attributes (such as its offset in the section) and
            # a header which conforms to the DWARF standard. The access to
            # header elements is, as usual, via item-lookup.

            # A CU provides a simple API to iterate over all the DIEs in it.
            for DIE in CU.iter_DIEs():
                #Find the function
                if DIE.tag == "DW_TAG_subprogram":
                    fname = ""
                    for attr in itervalues(DIE.attributes):
                        if attr.name == "DW_AT_name":
                            fname = attr.value
                    if fname == function_name:
                        for CHILD in DIE.iter_children():
                            if CHILD.tag == "DW_TAG_variable" or CHILD.tag == "DW_TAG_formal_parameter" :
                                name = ""
                                right_loc = False
                                for attr in itervalues(CHILD.attributes):
                                    if attr.name == "DW_AT_name":
                                       name = attr.value
                                    # Check if this attribute contains location information
                                    if attr.name == "DW_AT_location":
                                        loc = loc_parser.parse_from_attribute(attr,
                                                                                  CU['version'])
                                        if isinstance(loc, LocationExpr):
                                            parser = DWARFExprParser(dwarfinfo.structs)
                                            parsed = parser.parse_expr(loc.loc_expr)
                                            for op in parsed:
                                                if op.op_name == 'DW_OP_fbreg' and op.args[0] == offset:
                                                    right_loc = True
                                if right_loc:
                                    return name

if __name__ == '__main__':
    print(get_var_name("tests\\test", b'execute_query', -24))
    print(get_var_offset("tests\\test", b'execute_query', b'query'))