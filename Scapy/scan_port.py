from scapy.all import IP, TCP, sr

def scan_port(host, port):
	reponse = sr( IP(dst=host)/TCP(dport=port), timeout=0.5, verbose=True )
	print(reponse)

	if reponse is None:
		print ("Port %s close" % port)
	else:
		print ("Port %s open" % port)

scan_port("192.168.56.1", 3306)
exit()

x = range(8000)
for port in x:
	scan_port("www.google.fr", port)

