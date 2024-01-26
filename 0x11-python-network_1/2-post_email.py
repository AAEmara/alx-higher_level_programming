#!/usr/bin/python3
"""Takes in a URL and an email, sends a `POST` request to it.
The email used in the `POST` request is provided as a parameter."""


import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        output = response.read()
    print(output.decode('utf-8'))
