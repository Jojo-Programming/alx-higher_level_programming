#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept and tested using the web server running on port 5000
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
