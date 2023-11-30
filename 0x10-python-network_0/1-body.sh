#!/bin/bash
# Takes a URL, and sends a GET request to the URL. Displays the body of the response.
curl -s -w "%{http_code}" "$1" | grep 200
