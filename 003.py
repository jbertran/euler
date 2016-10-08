import math

def isprime(n):
    i = int(math.sqrt(n))
    while (i > 1):
        if n % i == 0:
            return False
        i -= 1
    return True

n = 600851475143
i = int(math.sqrt(n))

while (i > 0):
    if n % i == 0 and isprime(i):
        break
    i -= 1

print(i)
