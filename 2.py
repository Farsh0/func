from math import *

x = int(input())

def func(arg_x):
    print(((arg_x - 1) ** 2) - sin(2 * arg_x))

func(x)