import functools

print(functools.reduce(lambda x, y: x + y if y % 3 == 0 or y % 5 == 0 else x, range(1, 1000), 0))

"""
s = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)
"""
