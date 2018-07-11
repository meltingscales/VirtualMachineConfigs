"""
NOTE: ping_statistics and traceroute are Mac-specific.

TODO: Fix da NOTE.
"""

import time
import subprocess
import re

def traceroute(host):
    host = host.strip()
    return subprocess.check_output(['traceroute', host])


def whois_domains(host):
    y = subprocess.check_output(['whois', whois])
    return re.findall('Name Server: (.*)', y)

def ping(host, times=2):
    args = ['ping','-c %d' % times, host]
    return subprocess.check_output(args)

def ping_statistics(ping_info):
    return re.findall('round-trip .+? = (\d.*) ms', ping_info)

host = raw_input("ping host\n > ")

try:
    while True:

        time.sleep(3)

        results = ping(host)
        stats = ping_statistics(results)
        stats = '\n'.join(stats) # turns stats from a list into a string separated by newlines

        print(stats)

        f = open('log.txt', 'a')

        f.write(stats + '\n')

        f.close()
except KeyboardInterrupt:
    print("ok ill stop")

print("done!")
