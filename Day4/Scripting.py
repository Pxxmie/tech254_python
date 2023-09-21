# Scripting

# there are seven modules that we can consider "core" in Python

import sys
import os
import subprocess
import math
import random  # you can also write from random .randrange
import datetime as dt  # you can use as to change the full name to shortform so dt instead of datetime
import json

# sys

print(sys.version)  # shows the version of python we have - can check hardware such as cpu

# os

# print(os.getcwd()) #tells me the current directory I am in
#
# os.mkdir("test_dir") # made a new directory in my current folder


# subprocess

# subprocess.run(["python", "helloworld.py"])

# math

pi = math.pi
pi_string = str(pi)
print(f"the value of pi is {pi_string}")

# random
rand_num = random.randrange(1, 10)
print(rand_num)

# datetime
date = dt.datetime.now()
print(date)

# json # changes the type of string
x = {
    "name": "Prismika",
    "age": 26,
    "city": "London"
}

print(type(x))

y = json.dumps(x)
print(y)
