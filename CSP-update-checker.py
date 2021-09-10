#CSP-update-checker-v0.1
import validators
import requests

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
               else:
                   print("No CSP\n")  
           except:
               print("\nCSP is not implemented on "+domain) 
       
    except:
        print("\nNot a valid domain")
         
    
        
if __name__ == '__main__':
    isdomain()
        
