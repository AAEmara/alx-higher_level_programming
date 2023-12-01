#!/bin/bash
# Takes a URL, and sends a DELETE request to the URL. Displays the body of the response.
curl -s -X DELETE "$1" 
