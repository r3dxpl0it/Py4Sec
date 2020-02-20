import os 
from netaddr import IPNetwork
import socket 
from multiprocessing import Pool

if not os.path.isdir('dns_data') : 
    os.mkdir('dns_data')

def simple_host(ip):
    try : 
        filename = 'dns_data/'+str(ip)+'.txt'
        if not os.path.isfile(filename) : 
            data = socket.gethostbyaddr(str(ip))
            print (data)
            f = open('dns_data/'+str(ip)+'.txt' , 'w')
            f.writelines(data)
            f.flush()
            f.close()
    except Exception as e:
        pass

for i in range(0, 256) : 
    for j in range(0 , 256) : 
            IP_RANGE = '{}.{}.0.0/16'.format(i , j)
            print (IP_RANGE)
            p = Pool(64)
            p.map(simple_host, IPNetwork(IP_RANGE))
            p.close() 
