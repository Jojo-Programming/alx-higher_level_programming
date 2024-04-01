#!/bin/bash
# Sends a DELETE request to a given URL, request to the URL passed as the first argument and display the response body,
curl -sX DELETE "$1"
