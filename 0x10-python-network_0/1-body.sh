#!/bin/bash
# this takes in a URL, sends a GET request to the URL, and displays body of the response. Display only body of a 200 status code response
curl -sL "$1"
