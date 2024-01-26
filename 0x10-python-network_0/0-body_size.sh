#!/bin/bash
# Sending a request to the URL, displaying the size of the body of response.
curl -sw "%{size_download}\n" "$1" -o /dev/null
