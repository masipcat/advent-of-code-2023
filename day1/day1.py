import string

text_nums = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
]

def get_value(l):
    first_num = None
    last_num = None
    for i, c in enumerate(l):
        if c in string.digits:
            if first_num is None:
                first_num = c
            else:
                last_num = c
        else:
            for text_num, num in text_nums:
                if l[i:].startswith(text_num):
                    if first_num is None:
                        first_num = num
                    else:
                        last_num = num
                    break
    if last_num is None:
        last_num = first_num
    return int(first_num + last_num)


with open('input1.txt', 'r') as f:
    total = 0
    for l in f.readlines():
        total += get_value(l)
    print(total)
