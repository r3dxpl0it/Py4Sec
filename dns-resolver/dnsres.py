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
import dns , dns.query , dns.resolver

def socketreq(Target) : 
	try  : 
		ip = socket.gethostbyname(Target)
		return ip
	except socket.gaierror : 
		return None

def dns_resolve(Target) : 
	try : 
		ns = dns.resolver.query(Target,'NS')
		name_servers = list()
		for names in ns :
			name_servers.append(names)
		return name_servers
	except Exception as s : 
		return s

def dns_extractor(a) : 
	nameservers = list()
	for ns in a : 
		print (ns , ' IP : ' , socketreq(str(ns)))
		nameservers.append(ns)
	return nameservers
