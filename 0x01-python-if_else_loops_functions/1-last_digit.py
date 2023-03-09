#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    remndr = number % 10
else:
    remndr = number % -10

if remndr > 5:
    print(f"Last digit of {number} is {remndr} and is greater than 5")
elif remndr == 0:
    print(f"Last digit of {number} is {remndr} and is 0")
else:
    print(f"Last digit of {number} is {remndr} and is less than 6 and not 0")
