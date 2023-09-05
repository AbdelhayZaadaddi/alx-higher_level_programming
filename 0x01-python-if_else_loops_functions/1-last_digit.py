#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_degit = abs(number) % 10
if number < 0:
    last_degit = -last_degit

print(f"Last digit of {number} is {last_degit} and is ", end="")
if last_degit > 5:
    print("greater than 5")
elif last_degit == 0:
    print("0")
else:
    print("less than 6 and not 0")
