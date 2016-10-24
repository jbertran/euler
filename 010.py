import itertools as it

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
