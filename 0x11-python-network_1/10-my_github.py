#!/usr/bin/python3
"""prints github user id using github api"""
import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    headers = {
               'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer {}'.format(sys.argv[2])
               }
    r = requests.get(url, headers=headers)
    r_json = r.json()
    print(r_json.get('id'))
