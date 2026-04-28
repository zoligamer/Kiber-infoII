from scapy.all import sniff, get_if_list,Raw
from scapy.layers.http import HTTPRequest


def packet_callback(packet):
    print(packet.summary())
    if packet.haslayer(HTTPRequest):
        req=packet[HTTPRequest]
        if req.Method and req.Method.decode()=="POST":
            if packet.haslayer(Raw):
                post_data=packet[Raw].load.decode("utf-8",errors="ignore")
                print(f"POST Data: {post_data}")

if __name__=="__main__":
    print(get_if_list())
    sniff(iface="lo",prn=packet_callback,filter="tcp port 80")