#!/usr/bin/env python
# coding: utf-8

from scapy.all import *


t = Ether()

#change the source mac
t.src = 'ddd'

t.show()

sendp(t)
