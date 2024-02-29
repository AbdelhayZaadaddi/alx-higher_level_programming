#!/bin/bash
# sends a get request to the URL, and display the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
