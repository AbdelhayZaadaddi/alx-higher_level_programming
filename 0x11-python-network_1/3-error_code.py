#!/usr/bin/python3
"""
Script the takes in a url, send a request to the URL
display the vody of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resoponse:
            print(resoponse.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
