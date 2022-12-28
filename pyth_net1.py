from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",


    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "port":22,
    "username": "developer",
    "password":"C1sco12345"
}
##next establish the ssh connection
net_connect=ConnectHandler(**CSR)
output=net_connect.send_command('show ip int brief')
print(output)
"""output_routes=
output_runconfig=net_connect.send_command('show run')
print("output_runconfig")
net_connect.disconnect()"""
