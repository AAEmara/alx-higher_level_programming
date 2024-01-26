#!/bin/bash
# Taking a URL, and displaying all HTTP methods the server will accept.
curl -si "$1" | grep 'Allow:' | sed 's/Allow: //g'
