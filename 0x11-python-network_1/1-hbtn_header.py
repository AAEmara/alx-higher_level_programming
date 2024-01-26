#!/usr/bin/python3
"""Taking a URL and sendig it a request to display the value of
`X-Request-Id` variable found in the response header."""


import urllib.request
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header_val = response.getheader('X-Request-Id')
    print(header_val)
