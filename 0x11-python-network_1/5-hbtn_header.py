#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    body = requests.get(url)
    print(body.headers.get('X-Request-Id'))
