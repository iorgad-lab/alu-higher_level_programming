#!/usr/bin/python3
"""Script that displays the X-Request-Id header using requests."""
import requests
import sys

response = requests.get(sys.argv[1])
print(response.headers.get("X-Request-Id"))
