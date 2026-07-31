#!/bin/bash
# Sends a GET request with a header variable X-HolbertonSchool-User-Id=98
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
