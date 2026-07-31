#!/usr/bin/python3
"""Script that reads stdin line by line and computes log statistics."""
import sys

VALID_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def print_stats(total_size, status_codes):
    """Print the total file size and line count per status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {}
count = 0
last_printed = -1

try:
    for line in sys.stdin:
        parts = line.split()
        try:
            size = int(parts[-1])
            code = parts[-2]
        except (IndexError, ValueError):
            continue
        total_size += size
        if code in VALID_CODES:
            status_codes[code] = status_codes.get(code, 0) + 1
        count += 1
        if count % 10 == 0:
            print_stats(total_size, status_codes)
            last_printed = count
except KeyboardInterrupt:
    if count != last_printed:
        print_stats(total_size, status_codes)
    raise
else:
    if count != last_printed:
        print_stats(total_size, status_codes)
