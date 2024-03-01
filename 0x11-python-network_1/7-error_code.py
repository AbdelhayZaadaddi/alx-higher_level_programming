#!/usr/bin/python3
"""
Script that taken in a URL
ANd displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    responsee = requests.get(argv[1])
    status = responsee.status_code
    if status < 400:
        print(responsee.text)
    else:
        print("Error code: {}".format(responsee.status_code))
