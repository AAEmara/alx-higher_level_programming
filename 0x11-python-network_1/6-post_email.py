#!/usr/bin/python3
"""Takes a URL and an email address, send a `POST` request to the URL
with the email and  displays the body of the response."""


import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
