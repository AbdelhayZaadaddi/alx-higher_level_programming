#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_ = a_dictionary.copy()
    for i in dict_.keys():
        dict_[i] *= 2
    return dict_
