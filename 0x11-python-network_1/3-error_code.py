#!/usr/bin/python
"""
Script the takes in a url, send a request to the URL
display the vody of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
