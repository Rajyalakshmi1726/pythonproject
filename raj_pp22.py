"""import scapy.all as scapy
request=scapy.ARP()
print(request.summary())"""



"""import scapy.all as scapy
request=scapy.ARP()##
print(request.show())"""

"""from scapy.all import *
ip=IP()
print(ip)
print(ip.show())"""

"""from scapy.all import *
my_frame=Ether()/ICMP()##
print(my_frame)##raw freame data
print(my_frame.show())"""

"""from scapy.all import *
s=IP(dst="google.com")/ ICMP()
print(s.show())"""

"""from scapy.all import *
a=IP(ttl=10)##Ip heart beats ->sent every 10sec
#print(a)
#print(a.src)
"""a.dst="192.168.1.1"
var1=a.src
print(var1.show())
print(a)
print(a.src)
del(a.ttl)
print(a.show())"""
from scapy.all import *
c=IP() /TCP()
print(c.show())
d=Ether()/IP()/TCP()##Header
print(d.show())
e=IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"##header and body
print(e.show())

from scapy.all import *
j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET/index.html HTTP/1.0\n\n"##
print(hexdump(j))

from scapy.all import *
k=IP(dst="www.slashdot.org/30")
#dst=Net('www.slashdot.org/30')
print([p for p in k])"""

import psutil
import time
UPDATE_DEALY= 1 #IN seconds
def get_size(bytes):
    for unit in ['','K','M','G''T','P']:
        if bytes< 1024:
            return f"{bytes:2f}{unit}B"
        bytes /=1024

        io=psutil.net_io_counters()
        bytes_sent,bytes_recv=io.bytes_sent,io.bytes_recv

while True:
    time.sleep(UPDATE_DEALY)
    io_2=psutil.net_io_counters()
    us,ds=io_2.bytes_sent,io_2.bytes_recv
    print(f"upload:{get_size(io_2.bytes_sent)}  "
    f",Download:{get_size(io_2.bytes_sent)}  "
    f",upload speed :{get_size(us/UPDATE_DEALY)} /s"
    f",Download speed :{get_size(ds/UPDATE_DEALY)} /s    ",end="\r")
    bytes_sent, bytes_recv=io_2.bytes_sent,io_2.bytes_recv



