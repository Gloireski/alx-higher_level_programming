#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests


body = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(body.text)))
print("\t- content: {}".format(body.text))
