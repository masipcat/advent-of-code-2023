import re
from collections import defaultdict


def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val


if __name__ == "__main__":
    boxes = defaultdict(dict)

    with open("input15.txt", "r") as f:
        steps = f.read().strip().split(",")

    for step in steps:
        m = re.match("(\w+)(-|=\d)", step)
        label = m.group(1)
        op = m.group(2)
        h = hash(label)

        box = boxes[h]
        if op == "-":
            if label in box:
                del box[label]
            # TODO: move?
        else:
            focal_len = op[1:]
            if label in box:
                new_box = {}
                for k, v in box.items():
                    if k == label:
                        v = focal_len

                    new_box[k] = v
                boxes[h] = new_box
            else:
                box[label] = focal_len

    print({k: v for k, v in boxes.items() if v})

    total = 0
    for box_k in sorted(boxes.keys()):
        box = boxes[box_k]
        n_box = box_k + 1
        for i, focal_len in enumerate(box.values()):
            total += n_box * (i + 1) * int(focal_len)

    print(total)
