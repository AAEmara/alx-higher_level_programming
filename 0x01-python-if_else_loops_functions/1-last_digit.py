#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if (last_digit < 6 and last_digit != 0):
    if (number < 0):
        last_digit -= 10
    print(f"Last digit of {number:d} is {last_digit:d}\
 and is less than 6 and not 0")
elif (last_digit == 0):
    print(f"Last digit of {number:d} is {last_digit:d}\
 and is 0")
else:
    print(f"Last digit of {number:d} is {last_digit:d}\
 and is greater than 5")
