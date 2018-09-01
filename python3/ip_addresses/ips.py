import ipaddress

# Courtesy of Christian H., a tutee of mine. 

try:
    input = raw_input
except:
    pass

ask = input('What IP would you like to find the range on? :')
default = u'2402:79c0:2100::/40'

try:
    ipa = ipaddress.ip_network(u''+ask)
except:
    print("Couldn't understand IP address: '"+ask+"'.")
    print("Using a default address, '"+default+"'.")
    ipa = ipaddress.ip_network(default)

for ip in ipa.hosts():
    ip = ip
    break

hm = int(str(ipa).split('/')[-1]) # Get number after slash.


if isinstance(ipa, ipaddress.IPv4Network):
    factor = ipaddress.IPV4LENGTH
elif isinstance(ipa, ipaddress.IPv6Network):
    factor = ipaddress.IPV6LENGTH

print("Range of addresses:")
print(ip)
print(ip + (pow(2, (factor - hm)) - 2))

#2402:79c0:2100::/40 + 2^(128 - 40)


# ip_range = ipaddress.ip_network(u'2402:79c0:2100::/40')
#
# for ip in ipa.hosts():
#     print(ip)
#2402:79c0:2100::/40
