# import math
import os
import sys

# print(sys.version)
# print(sys.executable)
print("It worked!!!")


def greet(whoToGreet):
    gretting = "Hello, {}".format(whoToGreet)
    return gretting


x = input("Who am I greeting? ")
print(greet(x))
