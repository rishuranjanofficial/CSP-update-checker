#CSP-update-checker-v2.0
import validators
import requests
import json
from hashlib import sha256
import datetime


def isdomain(domain):    
    try:             
        if(validators.domain(domain)==True):                       
            iscsp(domain)            
        else:
            print("Please enter a valid domain")
            isdomain()       
    except:
        print("\nd_exit")
     
def iscsp(domain):
    try: 
       try:       
           url="https://"+domain           
       except:
          url="http://"+domain           
       req = requests.get(url)    
       header=req.headers
       if header is not None: 
           print("\nThe domain \""+domain+"\" is a valid domain")         
           try:         
               csp_header=req.headers['Content-Security-Policy']              
               if csp_header is not None:
                   print("\nThe CSP Policy of "+domain+":\n"+csp_header+"\n")  
                   checksumcsp(domain,csp_header)    
               else:
                   print("No CSP\n")  
           except:
               print("\nCSP is not implemented on "+domain)              
    except:
        print("\nNot a valid domain")
         
def checksumcsp(domain,csp_header): 
    try:
        new_domain=0
        datetime_object = datetime.datetime.now()
        csp_hash=sha256(csp_header.encode('utf-8')).hexdigest()
        print("The SHA256 checksum of CSP policy of \""+domain+"\" is "+csp_hash+" on "+str( datetime_object)+"\n")
        Domain_Hash=[]
        with open('Domain_Hash.txt', 'r') as fr:
            for line in fr:
                Domain_Hash.append(line.strip().split('&'))            
            for pair in Domain_Hash:        
                d,h,t = pair[0],pair[1],pair[2]
                if (d==domain and h==csp_hash):
                    print("No Change in CSP Policy since last checked on "+t)
                    fr.close()
                    return
                elif (d==domain and h != csp_hash):
                    with open('Domain_Hash.txt', 'a') as fw:  
                        fw.write('%s&%s&%s&%s\n' % (domain, csp_hash,datetime_object,csp_header))
                        print("CSP Policy for \""+domain+"\" is updated from last time "+t)
                        fr.close()
                        fw.close() 
                        return
                elif (domain!=d):
                    new_domain=1
        if (new_domain==1):            
            with open('Domain_Hash.txt', 'a') as fw:  
                fw.write('%s&%s&%s&%s\n' % (domain, csp_hash,datetime_object,csp_header))
                print("CSP Policy for \""+domain+"\" is added in record")
                fr.close()
                fw.close() 
                return                            
    except:
        print("Please try again\n")                                               
    
if __name__ == '__main__':
    choice=input("1. Check Content-Security-Policy(CSP) for single domain\n2. Check Content-Security-Policy(CSP) for list of domains\n")
    if(choice=='1'):
        print("Enter the Domain name")
        domain=input() 
        isdomain(domain)
    
    elif (choice=='2'):
        fileinput = input("Enter the file with list of domains: ") 
        try:        
            with open(fileinput, "r") as f: 
                while True:                         
                    line=f.readline()
                    if not line:
                        break
                    domain=line.strip()               
                    isdomain(domain) 
        except:
            print("Please give valid file")     
