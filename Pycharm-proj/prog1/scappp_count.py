from scapy.all import sniff

packet=sniff(filter='tcp',count=5)
print("\n packet")