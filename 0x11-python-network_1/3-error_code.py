#!/usr/bin/python3
"""module handling error from webpage"""
import sys
import urllib.request as request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as webpage:
            content = webpage.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
