#!/bin/bash
# Script that sends a POST request to to the passed URl and displays the body response, that takes in a URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
