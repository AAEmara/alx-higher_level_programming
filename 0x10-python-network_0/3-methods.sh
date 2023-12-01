#!/bin/bash
# Takes a URL, and displays all the HTTP methods the server will accept.
curl -sL -i -X OPTIONS "$1" | grep Allow: | cut -d " " -f 2-
