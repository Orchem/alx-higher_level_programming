#!/usr/bin/python3
"""module for fetching body response"""
import requests

if __name__ == '__main__':
    webpage = requests.get('https://alx-intranet.hbtn.io/status')
    content = webpage.text
    print("""Body response:
\t- type: {}
\t- content: {}""".format(type(content), content))
