#CSP-update-checker-v1.0
import validators
import requests
import json
from hashlib import sha256
import datetime

print("Enter the Domain name")
def isdomain():    
    try:
        domain=input()              
        if(validators.domain(domain)==True):                       
            iscsp(domain)            
        else:
           print("Please enter a valid domain")
           isdomain()       
    except:
        print("\nd_exit")
     
def iscsp(domain):
    try: 
              
       url="http://"+domain       
       req = requests.get(url)
       header=req.headers
       if header is not None: 
           print("The domain \""+domain+"\" is a valid domain")         
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
                    return
                elif (d==domain and h != csp_hash):
                    with open('Domain_Hash.txt', 'a') as fw:  
                        fw.write('%s&%s&%s\n' % (domain, csp_hash,datetime_object))
                        print("CSP Policy for \""+domain+" is updated from last time "+t) 
                        return
                elif (domain!=d):
                    new_domain=1
        if (new_domain==1):            
            with open('Domain_Hash.txt', 'a') as fw:  
                fw.write('%s&%s&%s\n' % (domain, csp_hash,datetime_object))
                print("CSP Policy for \""+domain+" is added in record") 
                return                            
    except:
        print("Please try again\n")                                               
    
if __name__ == '__main__':
    isdomain()
        
