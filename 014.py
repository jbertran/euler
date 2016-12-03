c_lengths = {}

def collatz_length(num, c_lens=c_lengths):
    len = 0
    n = num
    while n > 1:
        if c_lens.get(n) is not None:
            c_lens[num] = c_lens[n] + len
            return c_lens[n] + len

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        len += 1
    c_lens[num] = len
    return len

max = 0
cn = 0
for i in range(1000000):
    cl = collatz_length(i)
    if max < cl:
        max = cl
        cn = i

print(cn)
