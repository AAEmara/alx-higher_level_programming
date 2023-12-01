#!/bin/bash
# Takes a URL, sends a GET request and displays response the server will accept.
curl -s -H "X-School-User-Id: 98" "$1"
