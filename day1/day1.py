

def get_value(l):
    first_num = None
    last_num = None
    for c in l:
        if c >= '0' and c <= '9':
            if first_num is None:
                first_num = c
            else:
                last_num = c
    if last_num is None:
        last_num = first_num
    return int(first_num + last_num)


with open('input1.txt', 'r') as f:
    total = 0
    for l in f.readlines():
        total += get_value(l)
    print(total)
