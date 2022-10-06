from math import *

x, y = int(input()), int(input())

def func(arg_x, arg_y):
    print(cos(arg_y) + arg_x - 1.5)
    print(2 * arg_y - sin(arg_x - 0.5) - 1)

func(x, y)
