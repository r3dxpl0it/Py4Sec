### dnsres.py 
Simple DNS Resolver Just in 3 Functions with Sockets and dns Module 
#### Usage 
```
from dnsres import *
DOMAIN = 'polito.it'
if socketreq(DOMAIN) is not None : 
	print(socketreq(DOMAIN))
test = dns_extractor((dns_resolve(DOMAIN)))

```
### mass_dns.py 
Multi Processes DNS resolver for Internet Surface DNS 
#### Usage 
```
python3 mass_dns.py 
```
