#!/usr/bin/python3
"""module to search user by letter"""
import sys
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': sys.argv[1][0] if len(sys.argv) > 1 else ""}
    r = requests.post(url, data=data)
    try:
        r_json = r.json()
        if not r_json:
            print('No result')
        else:
            print('[{}] {}'.format(r_json.get('id'), r_json.get('name')))
    except ValueError:
        print('Not a valid JSON')
