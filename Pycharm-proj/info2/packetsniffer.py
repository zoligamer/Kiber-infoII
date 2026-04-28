import logging
from urllib.parse import parse_qs

from scapy.all import sniff, get_if_list, Raw
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6


logger=logging.getLogger("sniffer")
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("sniffer.log")
file_handler.setLevel(logging.INFO)
formater=logging.Formatter("%(message)s")
file_handler.setFormatter(formater)
logger.addHandler(file_handler)


def packet_callback(packet):
    print(packet.summary())
    if packet.haslayer(HTTPRequest):
        req=packet[HTTPRequest]
        if req.Method and req.Method.decode()=="POST":
            if packet.haslayer(Raw):
                post_data=packet[Raw].load.decode("utf-8",errors="ignore")
                print(f"POST Data: {post_data}")
                ip="N/A"
                if packet.haslayer(IP):
                    ip=packet[IP].dst
                if packet.haslayer(IPv6):
                    ip=packet[IPv6].dst

                if "username" in post_data and "password" in post_data:
                    form_data=parse_qs(post_data)
                    user=form_data["username"]
                    password=form_data["password"]
                    msg=f"{ip} {user} {password}"
                    logger.info(msg)

if __name__=="__main__":
    print(get_if_list())
    sniff(iface="lo",prn=packet_callback,filter="tcp port 80")