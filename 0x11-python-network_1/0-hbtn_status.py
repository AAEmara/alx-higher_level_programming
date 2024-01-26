#!/usr/bin/python3
"""Fetches a link using `urlib` package."""

import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print(f"Body response:\n\t- type: {type(html)}\n\t- content: {html}\n\t"
          f"- utf8 content: {html.decode('utf-8')}")
