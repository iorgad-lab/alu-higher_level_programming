#!/usr/bin/python3
"""Script that adds command line arguments to a JSON list file."""
import json
import os
import sys

filename = "add_item.json"

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, encoding="utf-8") as f:
        items = json.load(f)
else:
    items = []

items.extend(sys.argv[1:])

with open(filename, "w", encoding="utf-8") as f:
    json.dump(items, f)
