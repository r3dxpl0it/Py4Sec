import requests 
from multiprocessing import Process
import threading
import time 
import random
import argparse
import requests 
import xmltodict
import os 

def list_files(url , check_permission = False) :
    data = requests.get(url)
    xpars = xmltodict.parse(data.text)
    for item in xpars['ListBucketResult']['Contents'] : 
        content = url + '/' + item['Key']
        if check_permission : 
            print (content , check_status_200_premissions(content))
        else : 
            print ('\t{}:\t{}'.format(url , content))

def check_status_200_premissions(url) :
    req = requests.get(url, verify=False)
    if req.status_code == 200 : 
        return True
    else : 
        return False 

def check_s3_bucket_access(url) : 
    try : 
        if check_status_200_premissions(url) :
            print ('[{}] {}'.format(200 , url))

            list_files(url)
            return True , True 
        else : 
            pass
        return True , False 

    except Exception as e : 
        return False , False 

if __name__ == '__main__' : 
    parser = argparse.ArgumentParser()

    parser.add_argument('-f' , '--file', help='Dictionary to check', required=True)
    parser.add_argument('-d','--domain', default='.s3.amazonaws.com' , help='Default is s3 domain')
    args = parser.parse_args()

    if os.path.isfile(args.file) : 
        f = open(args.file , 'r')
    else : 
        raise ValueError('File Do Not Exist')

    sublist = f.readlines()
    random.shuffle(sublist)

    try :
        for item in sublist :
            t = random.uniform(0.0009,0.5)
            time.sleep(t)
            url = 'http://' + str(item).replace('\n' , '') + args.domain
            p = Process(target=check_s3_bucket_access, args=(url,))
            p.start()
            p.join()
    except Exception as e: 
        print (e)
