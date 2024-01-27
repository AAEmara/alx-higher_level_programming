#!/usr/bin/python3
"""Fetvhing a certain URL."""


import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print(f"Body response:\n\t- type: {type(r.text)}\n\t"
          f"- content: {r.text}")
