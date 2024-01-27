#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    status = req.status_code
    print(req.text) if status < 400 else print(
        "Error code: {}".format(req.status_code))
