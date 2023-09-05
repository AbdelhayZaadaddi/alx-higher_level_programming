#!/usr/bin/python3
def remove_char_at(str, n):
    f = n + 1
    if n < 0:
        return (str)
    return (str[:n] + str[f:])
