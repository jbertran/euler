# this is terrible

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
