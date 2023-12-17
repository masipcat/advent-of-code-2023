def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

with open("input15.txt", "r") as f:
    steps = f.read().strip().split(",")

total = 0
for step in steps:
    h = hash(step)
    # print(step, h)
    total += h
print(total)