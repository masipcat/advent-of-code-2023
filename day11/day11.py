from collections import defaultdict

def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def expand_universe(matrix):
    out = []
    for l in matrix:
        out += [list(l)]
        if all(n == "." for n in l):
            out += [list(l)]

    x = 0

    while x < len(out[0]):
        column = [out[y][x] for y in range(len(out))]
        if all(n == "." for n in column):
            for row in out:
                row.insert(x, ".")
            x += 1
        x += 1

    return out


def get_galaxy(matrix):
    galaxies = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "#":
                galaxies += [(y, x)]
    return galaxies

def get_pairs(galaxies):
    pairs = set()
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 == g2:
                continue
            pair = tuple(sorted((g1, g2)))
            pairs.add(pair)
    return pairs

def distance_pair(pair):
    g1, g2 = pair

    distance_y = abs(g2[0] - g1[0])
    distance_x = abs(g2[1] - g1[1])
    distance = distance_x + distance_y
    print(g1, g2, distance)
    return distance


if __name__ == "__main__":
    with open("input11.txt", "r") as f:
        matrix = [l.strip() for l in f.readlines()]
        matrix = expand_universe(matrix)
        pp(matrix)
        galaxies = get_galaxy(matrix)
        print(galaxies)
        pairs = get_pairs(galaxies)
        print(len(pairs), pairs)

        total = 0
        for pair in pairs:
            total += distance_pair(pair)
        print("total", total)
