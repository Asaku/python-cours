#!/usr/bin/env python
# coding: utf-8

from scapy.all import *


#Ping
mac = Ether() / IP(dst='192.168.1.27') / ICMP()

rep,non_rep = srp(mac)

#Sniff

rep = sniff(filter="host 192.168.1.24")

rep.show()
