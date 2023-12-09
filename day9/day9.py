from collections import defaultdict

def get_next_value(seq):
    next_seq = []
    for i in range(len(seq) - 1):
        next_seq += [seq[i+1] - seq[i]]

    if all([v == 0 for v in next_seq]):
        return seq[0]

    y = get_next_value(next_seq)
    x_0 = seq[0]
    next_val =  -y + x_0
    return next_val


if __name__ == "__main__":
    with open("input9.txt", "r") as f:
        sequences = [[int(v) for v in seq.split(" ")] for seq in f.readlines()]
        total = 0
        for seq in sequences:
            res = get_next_value(seq)
            print(res)
            total += res

        print("TOTAL", total)
