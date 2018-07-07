"""
NOTE: traceroute is mac-specific.

TODO: Fix da NOTE.
"""

import subprocess
import re

def traceroute(host):
    host = host.strip()
    return subprocess.check_output(['traceroute', host])


def whois_domains(host):
    y = subprocess.check_output(['whois', whois])
    return re.findall('Name Server: (.*)', y)


whois = raw_input("host\n > ")

domains = whois_domains(whois)
print(domains)

for domain in domains:
    print domain
    x = traceroute(domain)
    print(x)
