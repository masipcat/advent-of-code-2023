from copy import deepcopy

mat_len = None


def pp(points, length):
    matrix = [length * ["."] for _ in range(length)]

    for j, i, v in points:
        matrix[j][i] = v

    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def rotate_minus_90deg(j, i, length):
    return j, length - 1 - i


def rotate_minus_deg(j, i, length, deg):
    for _ in range(deg // 90):
        j, i = rotate_minus_90deg(j, i, length)
    return j, i


def get_at(matrix, j, i, deg):
    global mat_len
    length = mat_len
    j, i = rotate_minus_deg(j, i, length, deg)
    return matrix[j][i]


def put_at(matrix, j, i, val, deg):
    global mat_len
    length = mat_len
    j, i = rotate_minus_deg(j, i, length, deg)
    matrix[j][i] = val



def move_up(points, o, direction, length):
    if direction == "north":
        y_axis = 0
        x_axis = 1
        direction = -1
    if direction == "south":
        y_axis = 0
        x_axis = 1
        direction = 1
    elif direction == "east":
        y_axis = 1
        x_axis = 0
        direction = 1
    elif direction == "west":
        y_axis = 1
        x_axis = 0
        direction = -1

    if direction == -1:
        blocker = -1
    else:
        blocker = length

    # if o[0] == 3 or o[1] ==  1:
    #     breakpoint()

    for p in points:
        if p == o:
            continue

        if p[y_axis] != o[y_axis]:
            continue

        # check if there are vectors in the way
        if direction == -1:
            if p[x_axis] < o[x_axis]:
                if blocker is None or p[x_axis] > blocker:
                    blocker = p[x_axis]
        else:
            if p[x_axis] > o[x_axis]:
                if blocker is None or p[x_axis] < blocker:
                    blocker = p[x_axis]


    if y_axis == 0:
        return (blocker - 1 * direction, o[1], o[2])
    else:
        return (o[0], blocker - 1 * direction, o[2])


def move(points, length, direction):

    # if direction == "north":
    #     points = sorted(points, key=lambda x: (x[0], x[1]))
    # if direction == "south":
    #     points = sorted(points, key=lambda x: (x[0], x[1]), reverse=True)
    # elif direction == "west":
    #     points = sorted(points, key=lambda x: (x[1], x[0]))
    # elif direction == "east":
    #     points = sorted(points, key=lambda x: (x[1], x[0]), reverse=True)


    for i in range(len(points)):
        p = points[i]
        if p[2] == "O":
            p = move_up(points, p, direction, length)
            points[i] = p

    pp(points, length)
    print()
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




def tilt(points, length):
    points = move(points, length, "north")
    # points = move(points, length, "west")
    # points = move(points, length, "south")
    # points = move(points, length, "east")
    return points

if __name__ == "__main__":
    with open("input14.txt", "r") as f:
        matrix = f.read().strip()
        matrix = [list(l) for l in matrix.split("\n")]
        points = get_points(matrix)
        print(points)

        last = None


        for i in range(1):
            points = tilt(points, len(matrix))
            # pp(matrix)
            # print()
            # if copy == last:
            #     break
            # if last is None:
            #     last = copy
            if i % 1000 == 0:
                print(i)

        # TODO
        raise Exception("TODO")
        load = sum_load(matrix)
        print(load)
