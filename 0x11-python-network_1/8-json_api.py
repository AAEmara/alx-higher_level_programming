#!/usr/bin/python3
"""Takes in a letter and sends a `POST` request to a certain URL with
the letter."""


import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) == 1):
        letter = ""
    else:
        letter = sys.argv[1]

    r = requests.post(url, data={"q": letter})
    try:
        r = r.json()
        if (not r):
            print("No result")
        else:
            print(f"[{r['id']}] {r['name']}")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
