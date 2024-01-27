#!/usr/bin/python3
"""Takes a URL, sends a request to it and displays the body of response."""


import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            output = response.read()
        print(output.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
