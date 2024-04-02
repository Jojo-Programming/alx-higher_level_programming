#!/usr/bin/python3

"""
This takes a URL as input, sends request to URL using the requests package
and displays the value of the 'X-Request-Id' header from the response.
"""

import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches URL, sends request, displays 'X-Request-Id' header from response.

    :param url: The URL to fetch.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
