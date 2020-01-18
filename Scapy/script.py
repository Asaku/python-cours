#!/usr/bin/env python
# coding: utf-8

from scapy.all import *

#Png
rep = sr1(IP(dst='www.google.fr') / ICMP() / "payload")
#wrpcap('p.pcap', rep)
exit()
rep.show()

#Ping
sr1(IP(dst="www.google.fr")/TCP(dport=85,flags="S"),timeout=0.5)


#scan d'une plage d'adresse
rang = '192.168.1.1-50'
rep,non_rep = sr( IP(dst=rang) / ICMP() , timeout=0.5 )
for elem in rep :
	if elem[1].type == 0 :
		print (elem[1].src + ' a renvoye un echo-reply ')
