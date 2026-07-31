#!/usr/bin/python3
"""Script that searches a user via a JSON API."""
import requests
import sys

letter = ""
if len(sys.argv) > 1:
    letter = sys.argv[1]

response = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

try:
    result = response.json()
except ValueError:
    print("Not a valid JSON")
else:
    if not result:
        print("No result")
    else:
        print("[{}] {}".format(result.get("id"), result.get("name")))
