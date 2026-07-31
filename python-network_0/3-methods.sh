#!/usr/bin/env bash
# Displays all HTTP methods a server accepts for a given URL
curl -s -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
