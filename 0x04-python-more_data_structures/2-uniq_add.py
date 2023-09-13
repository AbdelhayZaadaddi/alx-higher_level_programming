#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_lsit = []
    sum = 0
    for i in my_list:
        if i not in new_lsit:
            sum = sum + i
            new_lsit.append(i)
    return sum
