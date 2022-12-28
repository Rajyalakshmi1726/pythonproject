from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password":"Cisco12345"
}
##next establish the ssh connection
net_connect=ConnectHandler(**CSR)
#output_runhost=net_connect.send_command('show rum | i host')
##then send the command and print the output
output=net_connect.send_command('show ip int brief')
print(output)
net_connect.disconnect()
#output_clock=net_co