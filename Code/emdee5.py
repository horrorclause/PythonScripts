#!/bin/usr/python3
### Script for HTB emdee 5 for life challenge

import requests
import hashlib
import re

req = requests.Session()
url = "http://157.245.39.76:32294/" 

### GET Request
rget = req.get(url)
#print(rget.text) # Prints out HTML Page

### Will input rget.text html and will parse out the string to be encoded
def parse_and_encode(text):
    regx = re.compile(r"<h3 align='center'>(.*)</h3>", re.MULTILINE)    # Identifying the location of the string that needs hashing
    text = regx.findall(text)[0]    # Searching for all text in between h3 tags
    md5 = hashlib.md5(text.encode('utf-8'))    # Python3 is Unicode, so encoding is needed to UTF-8 before hashing to MD5
    dig = md5.hexdigest()    # Returns the actual hash
    return {'hash' : dig}
    

data = parse_and_encode(rget.text)


### POST Request

rpost = req.post(url=url, data=data)

print(rpost.text)



