#!/usr/bin/python3
"""fetch alx-interner.hbtn.io"""
import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
