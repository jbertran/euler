import math

# Ugly. Gotta sieve prime dividers and combine them instead

dividers = {}

max_divs = 0
tr = 0
next_add = 1

while True:
    tr += next_add

    tr_divs = [1]
    it = math.ceil(math.sqrt(tr))
    while it > 1:
        if tr % it == 0:
            if dividers.get(it):
                for div in dividers[it]:
                    if div not in tr_divs:
                        tr_divs.append(div)
                break
            else:
                tr_divs.append(it)
        it -= 1

    dividers[tr] = tr_divs

    if len(dividers[tr]) >= 500:
        break
    if len(dividers[tr]) > max_divs:
        max_divs = len(dividers[tr])

    next_add += 1
    if next_add % 1000 == 0:
        print(next_add, tr, max_divs)

print(tr)























































cur_step = 2
triangular = 1
trig_max = 1
div_dict = {1: [1]}

while trig_max < 500:
    triangular += cur_step
    cur_step += 1
    div_dict[triangular] = [triangular]
    for k,v in div_dict.items():
        if triangular % k == 0:
            div_dict[triangular] += v
    if len(div_dict[triangular]) > trig_max:
        trig_max = len(div_dict[triangular])

print(triangular)
