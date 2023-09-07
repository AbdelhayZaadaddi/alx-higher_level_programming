#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":

    _names = dir(hidden_4)
    for name in _names:
        if name[:2] != "__":
            print(name)
