#!/usr/bin/python3
"""Script that prints the body or an error code using requests."""
import requests
import sys

response = requests.get(sys.argv[1])
if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print(response.text)
