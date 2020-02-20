import os
from netaddr import IPNetwork
from multiprocessing import Pool
 
IP_RANGE = '192.168.1.0/24'
SINGLE_IP = None
 
 
def Check_IP_PING(ip) :
    a = os.system('ping -c 1 -W 1 -q ' + str(ip) +'  > /dev/null 2>&1' )
    if a == 0 :
        print ('Up' , ip)
    else :
        print ('Down' , ip)
 
if SINGLE_IP == None :
    ips = [str(ip) for ip in IPNetwork(IP_RANGE)]  
    p = Pool(12)
    p.map(Check_IP_PING, ips)
else :
    Check_IP_PING(str(SINGLE_IP))
