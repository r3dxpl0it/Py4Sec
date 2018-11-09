'''_____________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
import socket
import argparse 
from extractor import *

def ethernet_frame(data):
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
	return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

class sniffer : 
	def __init__(self , verbose = False) :
		self.verbose = verbose
	def Launch(self) : 
		conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
		while True:
			raw_data, addr = conn.recvfrom(65536)
			dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
			print('-'*20)
			print('MAC Dest: {}\tMAC Source: {}\t'.format(dest_mac, src_mac))
			if eth_proto == 8:
				(version, header_length, ttl, proto, src, target, data) = ipv4_Packet(data)
				if self.verbose : 
					print("IPV4 Packet:")
					print('>>>Version: {}\n>>>Header Length: {}\n>>>TTL: {}'.format(version, header_length, ttl))
					print('>>>protocol: {}\n>>>IP Source: {}\n>>>IP Target: {}'.format(proto, src, target))
				else : 
					print('IP Source: {}\tIP Target: {}'.format(src, target))


				# ICMP
				if proto == 1:
					icmp_type, code, checksum, data = icmp_packet(data)
					if self.verbose :	
						print('ICMP Packet:')
						print('Type: {}\nCode: {}\nChecksum: {},'.format(icmp_type, code, checksum))			
						if format_output_line(data) is not None : 
								print('ICMP Data:')
								print(format_output_line(data))

				# TCP
				elif proto == 6:
					src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin = struct.unpack(
				'! H H L L H H H H H H', raw_data[:24])
					if self.verbose :	
						print('TCP Segment:')
						print('>>>Source Port: {}\n>>>Destination Port: {}'.format(src_port, dest_port))
						print('>>>Sequence: {}\n>>>Acknowledgment: {}'.format(sequence, acknowledgment))
						print('>>>URG: {}\n>>>ACK: {}\n>>>PSH: {}'.format(flag_urg, flag_ack, flag_psh))
						print('>>>RST: {}\n>>>SYN: {}\n>>>FIN:{}'.format(flag_rst, flag_syn, flag_fin))

						if len(data) > 0:
							# HTTP
							if src_port == 80 or dest_port == 80:	
								print('HTTP Data:')
								try:
									http = HTTP(data)
									http_info = str(http.data).split('\n')
									for line in http_info:
										print(str(line))
								except:
									print(format_output_line(data))
							else:
								if format_output_line(data) is not None : 

									print('TCP Data:')
									print(format_output_line(data))
					# UDP
				elif proto == 17:
					src_port, dest_port, length, data = udp_seg(data)
					if self.verbose :	
						print('UDP Segment:')
						print('Source Port: {}\nDestination Port: {}\nLength: {}'.format(src_port, dest_port, length))

				# Other IPv4
				else:
					if self.verbose :
						print('Other IPv4 Data:')
						print(format_output_line(data))

			else:
				if format_output_line(data) is not None and self.verbose : 
					print('Ethernet Data:')
					print(format_output_line(data))


if __name__ == "__main__" : 
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', help='Verbose OutPut', dest='verbose', default = False ,action='store_true')
	args = parser.parse_args()
	try : 
		test = sniffer(args.verbose).Launch()
	except KeyboardInterrupt :
		quit()
