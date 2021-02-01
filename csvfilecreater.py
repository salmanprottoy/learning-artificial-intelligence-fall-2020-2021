import csv
import ipaddress

with open('ip.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Host_Address'])
    net4 = ipaddress.ip_network('192.0.2.0/24')

    for i in net4.hosts():
        print(i)
        writer.writerow([i])



