#!/usr/bin/python3
"""Script that displays a response body or handles HTTPError."""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
