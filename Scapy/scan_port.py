from scapy.all import IP, TCP, sr1

def scan_port(host, port):
	reponse = sr1( IP(dst=host)/TCP(dport=port), timeout=0.5, verbose=False )

	if reponse is None:
		print ("Port %s close" % port)
	else:
		print ("Port %s open" % port)

host = str(input("Host to scan: "))
p_min = int(input("Port min: "))
p_max = int(input("Port max: "))

for port in range(p_min, p_max):
	scan_port(host, port)

