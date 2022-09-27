#!/usr/bin/python3
"""module that sends email using post method"""
import sys
import urllib.parse
import urllib.request as request

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode()
    req = request.Request(url, data)
    with request.urlopen(req) as webpage:
        content = webpage.read().decode('utf-8')
        print(content)
