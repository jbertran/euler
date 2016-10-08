from functools import reduce

r = range(1, 101)
ssq = reduce(lambda x, y: x + y*y, r, 0)
s = reduce(lambda x, y: x + y, r, 0)
sqs = s * s

print(sqs - ssq)
