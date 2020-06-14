import math
import os
import sys

import requests

# print(sys.version)
# print(sys.executable)
# print sys.version


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))

r = requests.get("https://www.google.com")
print(r.status_code)

# name = input("name? ")
# print(name)
