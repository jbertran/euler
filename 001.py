import functools

print(functools.reduce(lambda x, y: x + y if y % 3 == 0 or y % 5 == 0 else x, range(1, 1000), 0))
