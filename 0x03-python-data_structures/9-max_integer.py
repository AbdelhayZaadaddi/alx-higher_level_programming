#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big = my_list[0]
    for n in range(len(my_list)):
        if big < my_list[n]:
            big = my_list[n]
    return big
