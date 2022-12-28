"""from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",


    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "port":22,
    "username": "developer",
    "password":"C1sco12345"
}
hostname=net_connect.send_command('show run | i host')
hostname.split(" ")

hostname,device,*rest=hostname.split(" ")
print("Backing up"+device)
filename=('document.txt')
showrun=net_connect.send_command("show run")
showvlan=net_connect.send_command('show vlan')
shower=net_connect.send_command('show ver')
log_file= open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(shower)
log_file.write("\n")
net_conne"""
"""import uuid
print("The MAC address in formated way is :", end="")
print(':'.join(['{:02x}'.format((uuid.getnode()>>ele) & 0xff)
for ele in range(0,8*6,8)]))"""
"""import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)



##ifaddr::
import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IP of anetwork adapter" + adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print("%s/%s"%(ip.ip,ip.network_prefix))
    else:
        print(" No ips configured")


##PSUTIL
import psutil
#result01=psutil.cpu_times()
#result02=psutil.cpu_stats()
#result03=psutil.disk_partitions()
result04=psutil.net_io_counters(pernic=True)
print(result01)
print(result02)
print(result03)
print(result04)"""

##
"""import psutil
network_stats=psutil.net_io_counters(pernic=false)
bytes_sent=getattr('network_stats','bytes_sent')
bytes_recv=getattr('network_stats','bytes_recv')
print("Bytes sent={0} | bytes recevied={1}".format(bytes_sent,bytes_recv))



import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear',shell=True)
remoteserver=input("Enter a remote host to scan")
remoteserverIP=socket.gethostbyname(remoteserver)
print(" "*60)
print("please wait,scanning remote host",remoteserverIP)
print(" "*60)
t1=datetime.now()
try:
    for port in range(1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STRESAM,AF_UNIX)##connection meta parameter
        result=socket.connect_ex((remoteserverIP,port))#socket.connect_ex:returns the true or false
        if result ==0:
            print("port{}:          open".fomat(port))
            sock.close()
except keyboardInterrupt:
    print("you pressed ctrl+c")
    sys.exit()
except socket.gaierror
"""




import sacpy.all as scapy
request=scapy.ARP()
print(request.summmary())
