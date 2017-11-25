#!/usr/bin/env python
# coding: utf-8

import socket, sys

TCP_IP = ""
TCP_PORT = 15555
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(sys.argv[1])
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data