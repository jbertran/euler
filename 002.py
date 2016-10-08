def fibsum(cur, prev, acc):
    res = cur + prev
    if res >= 4e6:
        return acc
    if res % 2 == 0:
        acc += res
    return fibsum(res, cur, acc)

print(fibsum(1, 1, 0))
