from functools import reduce
from fractions import gcd

def lcm(a, b):
    return (a*b) / gcd(a, b)

r = reduce(lambda x, y: lcm(x, y), range(20, 1, -1))

print(r)
