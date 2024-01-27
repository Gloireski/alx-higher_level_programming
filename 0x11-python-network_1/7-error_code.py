#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get(url)
        print(req.text)
    except requests.exceptions.HTTPError as er:
        print("Error code: {}".format(er.status_code))
