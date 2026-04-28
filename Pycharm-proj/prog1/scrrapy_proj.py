from firewall.core.ipXtables import ICMP
from scapy.all import *
dest="8.8.8.8"
packet=IP(dst=dest)/ICMP()
respond=sr1(packet,timeout=5)
if respond:
    print(f"{dest} available, responding:{respond.time - packet.time:.2f}")
else:
    print(f"{dest} not available")