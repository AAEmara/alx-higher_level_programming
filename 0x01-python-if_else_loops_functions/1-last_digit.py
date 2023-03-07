#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = int(str(number)[-1]) * int((number/abs(number)))
if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd == 0:
    print(f"Last digit of {number} is {lastd} and is 0")
else:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
