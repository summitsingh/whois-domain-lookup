# Summit Singh Thakur
# 15 Feb 2021
#
# Without using any prebuilt APIs, Packages, SDKs, Linux "whois" or examples found on Stack Overflow, how can you get
# a domain name's expiration date using Python 3.6+? The input should be any .com domain name, the output should be
# just the expiration date as a datetime object. Code is preferred, pseudocode is acceptable. Hint: It should utilize
# a socket.

# !/usr/bin/env python3

from datetime import datetime
import socket
import idna
import sys

# found whois server on internet
whois_host = "whois.markmonitor.com"
whois_port = 43


def lookupDomain(domain):
    # remove http and www
    domain = domain.replace('http://', '')
    domain = domain.replace('www.', '')
    domain = idna.encode(domain) + "\n".encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((whois_host, whois_port))
        s.sendall(domain)
        data = s.recv(4096)
        data = data.decode('utf-8')
        return data


def getStamp():
    stamp = str(datetime.now())
    return stamp


if len(sys.argv) > 0:
    domain = sys.argv[1]
else:
    # default domain if command line argument is not passed
    domain = "google.com"
data = lookupDomain(domain)
# Line 6 contains expiration date
expirationDate = data.splitlines()[6].split()

# print whole whois data
# print(data)

# print expiration date as string
# print(expirationDate[-1])

# print expiration date as DateTime object
expirationDateTimeObject = datetime.strptime(expirationDate[-1], '%Y-%m-%dT%H:%M:%S-%f')
print(expirationDateTimeObject)
