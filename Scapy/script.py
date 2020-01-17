#!/usr/bin/env python
# coding: utf-8

from scapy.all import *


#Ping
mac = Ether() / IP(dst='192.168.1.50') / ICMP()

#change the source mac
t.src = 'ddd'

t.show()

rep = sniff(filter="host 192.168.1.50")

rep.show()
