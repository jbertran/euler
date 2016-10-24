import itertools as it

def erat2():
    D = {}
    i = 1
    l = [2]
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            i += 1
            if q > 2e6:
                return l
            l.append(q)
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

res = erat2()

print(res[:10])

print(sum(res))
