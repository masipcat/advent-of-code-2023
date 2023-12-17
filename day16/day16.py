from collections import defaultdict
import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)


def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def debug(matrix, points, latest=None):
    new_matrix = [list(r) for r in matrix]
    for p in energized_points:
        y, x = p
        if p == latest:
            new_matrix[y][x] = "*"
        else:
            new_matrix[y][x] = "#"
    pp(new_matrix)
    print()


def get_next(prev_point, current_point, symbol):
    direction = None

    if prev_point[0] == current_point[0]:
        if prev_point[1] < current_point[1]:
            direction = "right"
        else:
            direction = "left"
    elif prev_point[1] == current_point[1]:
        if prev_point[0] < current_point[0]:
            direction = "down"
        else:
            direction = "up"
    else:
        breakpoint()
        x = 1

    if symbol == ".":
        return [move(current_point, direction)]
    elif symbol == "/":
        if direction == "down":
            new_direction = "left"
        elif direction == "up":
            new_direction = "right"
        elif direction == "left":
            new_direction = "down"
        elif direction == "right":
            new_direction = "up"
        return [move(current_point, new_direction)]
    elif symbol == "\\":
        if direction == "down":
            new_direction = "right"
        elif direction == "up":
            new_direction = "left"
        elif direction == "left":
            new_direction = "up"
        elif direction == "right":
            new_direction = "down"
        return [move(current_point, new_direction)]
    elif symbol == "-":
        if direction in ("right", "left"):
            return [move(current_point, direction)]
        else:
            return [move(current_point, "right"), move(current_point, "left")]
    elif symbol == "|":
        if direction in ("up", "down"):
            return [move(current_point, direction)]
        else:
            return [move(current_point, "up"), move(current_point, "down")]
    else:
        breakpoint()
        x = 1


def move(point, direction):
    y, x = point
    if direction == "right":
        return (y, x + 1)
    elif direction == "left":
        return (y, x - 1)
    elif direction == "up":
        return (y - 1, x)
    elif direction == "down":
        return (y + 1, x)
    raise Exception("Unknown direction")


def subset_in_list(subset, list_):
    if len(subset) < 3:
        return False

    f = subset[0]
    indices = [i for i, _ in enumerate(list_) if list_[i] == f]
    found = 0
    for start in indices:
        if subset == list_[start : start + len(subset)]:
            found += 1
        if found == 2:
            return True
    return False


def follow_beam(matrix, energized_points, prev_point, current_point):
    symbol = matrix[current_point[0]][current_point[1]]

    points = get_next(prev_point, current_point, symbol)
    for point in points:
        if (
            point[0] < 0
            or point[0] >= len(matrix)
            or point[1] < 0
            or point[1] >= len(matrix[0])
        ):
            # out of bounds
            continue

        if subset_in_list([prev_point, current_point, point], energized_points):
            # loop!
            continue

        energized_points.append(point)
        # print(point)
        # debug(matrix, energized_points, point)
        follow_beam(matrix, energized_points, current_point, point)


if __name__ == "__main__":
    boxes = defaultdict(dict)

    with open("input16.txt", "r") as f:
        matrix = [list(r) for r in f.read().strip().split("\n")]

        energized_points = []

        prev_point = (0, -1)
        current_point = (0, 0)
        energized_points.append(current_point)
        follow_beam(matrix, energized_points, prev_point, current_point)

        debug(matrix, energized_points)
        print(len(set(energized_points)))
