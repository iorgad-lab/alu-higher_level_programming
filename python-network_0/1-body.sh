#!/usr/bin/env bash
# Displays the body of the response only if the status code is 200
response=$(curl -s -w "\n%{http_code}" "$1")
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')
if [ "$http_code" = "200" ]; then
    echo "$body"
fi
