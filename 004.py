def palindrome(n):
    s = str(n)
    while len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            break
    return len(s) <= 1

l = []
for i in range(100, 999):
    for j in range(100, 999):
        l.append(i*j)
pals = sorted(list(filter(lambda x: palindrome(x), l)))

print(pals[-1])
