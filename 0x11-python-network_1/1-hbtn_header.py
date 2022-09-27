#!/usr/bin/python3
"""module to check header for X-Request-Id"""
import sys
import urllib.request as request

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(url) as webpage:
        print(webpage.getheader('X-Request-Id'))
