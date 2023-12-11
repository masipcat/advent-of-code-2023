from collections import defaultdict


def expand_universe(matrix):
    horizontal_expands = []

    out = []
    for y, l in enumerate(matrix):
        out += [list(l)]
        if all(n == "." for n in l):
            horizontal_expands += [y]

    vertical_expands = []
    for x in range(len(out[0])):
        column = [out[y][x] for y in range(len(out))]
        if all(n == "." for n in column):
            vertical_expands += [x]

    return horizontal_expands, vertical_expands


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


def distance_pair(pair, hor_exp, ver_exp):
    g1, g2 = pair

    total_y = 0
    for y in hor_exp:
        if g2[0] > g1[0]:
            if g2[0] > y and g1[0] < y:
                total_y += 1000000 - 1
        else:
            if g1[0] > y and g2[0] < y:
                total_y += 1000000 - 1

    total_x = 0
    for x in ver_exp:
        if g2[1] > g1[1]:
            if g2[1] > x and g1[1] < x:
                total_x += 1000000 - 1
        else:
            if g1[1] > x and g2[1] < x:
                total_x += 1000000 - 1

    distance_y = total_y + abs(g2[0] - g1[0])
    distance_x = total_x + abs(g2[1] - g1[1])
    distance = distance_x + distance_y
    print(g1, g2, distance)
    return distance


if __name__ == "__main__":
    with open("input11.txt", "r") as f:
        matrix = [l.strip() for l in f.readlines()]
        hor_exp, ver_exp = expand_universe(matrix)
        galaxies = get_galaxy(matrix)
        print(galaxies)
        pairs = get_pairs(galaxies)
        print(len(pairs), pairs)

        total = 0
        for pair in pairs:
            total += distance_pair(pair, hor_exp, ver_exp)
        print("total", total)
