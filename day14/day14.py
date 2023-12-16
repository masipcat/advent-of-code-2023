from copy import deepcopy


def build_matrix(points, length):
    matrix = [length * ["."] for _ in range(length)]

    for j, i, v in points:
        matrix[j][i] = v
    return matrix


def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def _vertical(x):
    return x[1], x[0]


def _horizontal(x):
    return x[0], x[1]


def move(points, length, direction):
    if direction == "north":
        points = sorted(points, key=_vertical)
        y_axis = 0
        x_axis = 1
        direction = -1
    if direction == "south":
        points = sorted(points, key=_vertical)
        y_axis = 0
        x_axis = 1
        direction = 1
    elif direction == "west":
        points = sorted(points, key=_horizontal)
        y_axis = 1
        x_axis = 0
        direction = -1
    elif direction == "east":
        points = sorted(points, key=_horizontal)
        y_axis = 1
        x_axis = 0
        direction = 1

    len_points = len(points)

    if direction == -1:
        r = range(0, len(points))
    else:
        r = range(len(points) - 1, -1, -1)

    for i in r:
        p = points[i]
        if p[2] == "O":
            if i == 0 and direction == -1:
                prev_point = None
            elif i == len_points - 1 and direction == 1:
                prev_point = None
            else:
                # print(i, direction)
                prev_point = points[i + direction]

                if prev_point[x_axis] != p[x_axis]:
                    prev_point = None

            if prev_point is None:
                if direction == -1:
                    new_val = 0
                else:
                    new_val = length - 1
            else:
                new_val = prev_point[y_axis] - direction

            if y_axis == 0:
                points[i] = (new_val, p[1], p[2])
            else:
                points[i] = (p[0], new_val, p[2])

    return points


def sum_load(matrix):
    matrix = matrix[::-1]
    total = 0
    for j in range(len(matrix)):
        total += matrix[j].count("O") * (j + 1)
    return total


def get_points(matrix):
    points = []
    for j, row in enumerate(matrix):
        for i, val in enumerate(row):
            if val in "O#":
                points += [(j, i, val)]
    return points


if __name__ == "__main__":
    with open("input14.txt", "r") as f:
        matrix = f.read().strip()
        matrix = [list(l) for l in matrix.split("\n")]
        points = get_points(matrix)

        len_mat = len(matrix)

        iterations = []

        first_repetition = None
        first_same_points = None
        second_repetition = None

        TOTAL = 1000000000

        i = 0
        while i < TOTAL:
            points = move(points, len_mat, "north")

            matrix = build_matrix(points, len_mat)

            if first_same_points is None and matrix in iterations:
                first_repetition = i
                first_same_points = matrix
            elif second_repetition is None and matrix == first_same_points:
                second_repetition = i
                period = second_repetition - first_repetition
                # skip iterations
                i += ((TOTAL - i) // period) * period

            iterations += [matrix]

            points = move(points, len_mat, "west")
            points = move(points, len_mat, "south")
            points = move(points, len_mat, "east")

            i += 1

        matrix = build_matrix(points, len(matrix))
        pp(matrix)
        load = sum_load(matrix)
        print(load)
