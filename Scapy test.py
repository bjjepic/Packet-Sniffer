from scapy.all import get_if_list, get_if_hwaddr

for iface in get_if_list():
    print(f"Interface: {iface}, MAC Address: {get_if_hwaddr(iface)}")
