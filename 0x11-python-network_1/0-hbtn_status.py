#!/usr/bin/python3
"""module that fetches data from a webpage"""
import urllib.request as request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = request.Request(url)
    with request.urlopen(req) as webpage:
        content = webpage.read()
        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(
                               type(content),
                               content,
                               content.decode('utf-8')
                               ))
