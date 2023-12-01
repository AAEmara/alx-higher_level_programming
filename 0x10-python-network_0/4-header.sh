#!/bin/bash
# Takes a URL, sends a GET request and displays response the server will accept.
curl -s -b "X-School-User-Id=98" "$1"
