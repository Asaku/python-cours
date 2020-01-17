from scapy.all import sr1, IP, TCP

def scan_port(host, port):

	print ("Scanning port %s" % port)

	res = sr1(IP(dst=host) / TCP(dport=port), timeout=0.5, verbose=False)

	if res is not None and TCP in res:
		if res[TCP].flags == 18:
			OPEN_PORTS.append(port)
			print ("Port %s open" % port)
	else:
		print ("Port %s close" % port)

scan_port('www.google.fr', 85)

