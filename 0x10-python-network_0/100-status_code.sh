#!/bin/bash
# this sends a request to a URL, and displays only the status code of the response. your not allowed to use any pipe, redirection, etc.
curl -s -o /dev/null -w "%{http_code}" "$1"
