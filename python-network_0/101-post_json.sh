#!/bin/bash
# Sends a POST request with a JSON file's content as the body
curl -s -X POST -H "Content-Type: application/json" --data-binary @"$2" "$1"
