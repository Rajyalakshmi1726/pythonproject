"""from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        Router={
            "device_type":"cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect= ConnectHandler(**Router)
        print('connecting to ' + IP)
        print('-------------------------------------------------')
        output=net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()"""

import scapy.all as scapy
request=scapy.ARP()
print(request.summmary())

