#!/usr/bin/python3
"""list github commits for a repository"""
import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
                                                              sys.argv[2],
                                                              sys.argv[1]
                                                              )
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    r_json = r.json()
    for commit in r_json[:10]:
        print('{}: {}'.format(
                              commit.get('sha'),
                              commit.get('commit').get('author').get('name')
                              ))
