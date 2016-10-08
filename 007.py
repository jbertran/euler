from functools import reduce
import itertools

def erat2(n):
    D = {}
    i = 1
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            i += 1
            if i == n:
                return q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

print(erat2(10001))

class StopIterationExc(Exception):
    def __init__(self, val):
        self.val = val

class prime_gate(object):

    def __init__(self, prime, place):
        if place == 10001:
            raise StopIterationExc(prime)
        self.prime = prime
        self.place = place
        self.nextP = None

    def passes(self, n):
        if n % self.prime != 0:
            if self.nextP is None:
                self.nextP = prime_gate(n, self.place + 1)
            else:
                self.nextP.passes(n)

start = prime_gate(2, 1)

def primes_obj():
    """
    lel max recursion depth exceeded
    """
    n = 3
    while True:
        try:
            start.passes(n)
            n += 2
        except StopIterationExc as e:
            print(e.val)
            break
