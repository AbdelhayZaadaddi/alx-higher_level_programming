#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for n, m in list(a_dictionary.items()):
        if m is value:
            a_dictionary.pop(n)
    return a_dictionary
