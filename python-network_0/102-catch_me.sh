#!/bin/bash
# Makes a chained PUT request to /catch_me and prints the final response
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
