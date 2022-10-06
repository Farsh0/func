import sympy
def proc():
    for i in range(100, 1000):
        if sympy.isprime(i):
            print(i)
proc()
