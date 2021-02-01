import ipaddress

net4 = ipaddress.ip_network('192.0.2.0/24')

for i in net4.hosts():
    print(i)

