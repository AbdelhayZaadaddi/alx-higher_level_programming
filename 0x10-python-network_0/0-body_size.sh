#!/bin/bash
# GET length of body of request
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
