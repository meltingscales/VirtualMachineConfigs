#!/usr/bin/env python2

import sys, socket

with open('pattern_create_3200.dat', 'r') as f:
	offset = f.readline()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.33.16', 9999))
cmd=('TRUN /.:/' + offset)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()
