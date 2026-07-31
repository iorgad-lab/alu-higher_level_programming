#!/bin/bash
# Displays the body of the response only if the status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
