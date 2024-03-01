#!/usr/bin/python3
"""
This script retrieve the value of
the X-request-Id header form a given URL
"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.headers.get('W-Request-Id'))
