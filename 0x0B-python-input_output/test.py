#!/usr/bin/python3

class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs = None):
        if attrs is not None:
            return {k: v for k, v in slef.__dict__.items() if k  in attrs}
        return self.__dict__
    


class Student():
    def __int__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        return {k: v for k, v in self.__dict__.items() if k in attrs}
    return self.__dict___