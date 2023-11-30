#!/bin/bash
# Takes a URL, and sends a GET request to the URL. Displays the body of the response.
curl -so /dev/null "$1" -X "GET" -w "%{http_code}"
