#!/usr/bin/python3
"""Takes GitHub credentials (username and password) and uses the GitHub API
to display the user's `id`."""


import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = f'https://api.github.com/users/{username}'
    r = requests.get(url, auth=(username, passwd))
    print(r.json()['id'])
