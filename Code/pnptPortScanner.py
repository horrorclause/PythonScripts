#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 pnptScanner.py <ip>")
    
#Add a banner
print("-"* 50)
print(f"Scanning target: {target}")
print(f"Start time: {datetime.now()}")
print("-"*50)

try:
    for port in range(100,1001):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #Timesout after 1 second if no response
        result = s.connect_ex((target, port)) #Socket Target:Port
        #print(f"Trying port# {port}")
        if result == 0:                       #connect_ex is an error indicator, if port is open returns 0, is closed returns 1
            print(f"Port {port} is open.")
        s.close()

except KeyboardInterrupt:
    print("\nStopping..")
    sys.exit()
    
except socket.gaierror:
    print(f"Hostname: {target} could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")        
    sys.exit()
        
    