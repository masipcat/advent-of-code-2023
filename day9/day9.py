from collections import defaultdict

def get_next_value(seq):
    next_seq = []
    for i in range(len(seq) - 1):
        next_seq += [seq[i+1] - seq[i]]

    if all([v == 0 for v in next_seq]):
        return seq[-1]
    return seq[-1] + get_next_value(next_seq)


if __name__ == "__main__":
    with open("input9.txt", "r") as f:
        sequences = [[int(v) for v in seq.split(" ")] for seq in f.readlines()]
        total = 0
        for seq in sequences:
            total += get_next_value(seq)

        print("TOTAL", total)
