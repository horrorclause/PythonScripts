#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 pnptScanner.py <ip>")