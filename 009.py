def find():
    for a in range(1, 1001):
        for b in range(1, a - 1):
            c = 1000 - a - b
            if a*a+b*b == c*c:
                return a*b*c
    return 0

print(find())
