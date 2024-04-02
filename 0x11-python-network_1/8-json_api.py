#!/usr/bin/python3

"""
This takes letter as input sends POST request http://0.0.0.0:5000/search_user
with letter as parameter 'q'. It processes response displays result accordingl
"""

import requests
import sys


def search_user(letter):
    """
    Sends POST request with the letter as a parameter and displays the result.

    :param letter: The letter to search for.
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
