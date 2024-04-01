#!/bin/bash
# this script makes request to 0.0.0.0:5000/catch_me that causes server respond with a message containing You got me!, in body of response.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
