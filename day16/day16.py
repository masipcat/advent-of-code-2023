from collections import defaultdict
import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)


cache = {}


def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def debug(matrix, points, latest=None):
    new_matrix = [list(r) for r in matrix]
    for p in points:
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


def follow_beam(matrix, prev_point, current_point, local_cache):
    symbol = matrix[current_point[0]][current_point[1]]

    points = get_next(prev_point, current_point, symbol)

    local_points = set()

    for point in points:
        if (
            point[0] < 0
            or point[0] >= len(matrix)
            or point[1] < 0
            or point[1] >= len(matrix[0])
        ):
            # out of bounds
            continue

        tail = (current_point, point)
        if local_cache.get(tail, 0) >= 2:
            # loop!
            continue

        if tail in cache:
            ppp = cache[tail]
        else:
            local_cache[tail] += 1
            ppp = follow_beam(matrix, current_point, point, local_cache)
            if len(points) > 1:
                cache[tail] = ppp

        local_points.add(point)
        local_points = local_points.union(ppp)

    return local_points


def count_energized_tiles(matrix):
    total = 0

    # perimeter
    points = (
        [((-1, x), (0, x)) for x in range(len(matrix[0]))]
        + [((len(matrix), x), ((len(matrix) - 1, x))) for x in range(len(matrix[0]))]
        + [((y, -1), (y, 0)) for y in range(len(matrix))]
        + [((y, len(matrix[0])), (y, len(matrix[0]) - 1)) for y in range(len(matrix))]
    )

    for i, (prev_point, start_point) in enumerate(points):
        print(i, start_point)
        local_cache = defaultdict(int)
        energized_points = follow_beam(matrix, prev_point, start_point, local_cache)
        energized_points.add(start_point)
        count = len(energized_points)
        if count > total:
            total = count

    # debug(matrix, energized_points)
    return total


if __name__ == "__main__":
    boxes = defaultdict(dict)

    with open("input16.txt", "r") as f:
        matrix = [list(r) for r in f.read().strip().split("\n")]

        total = count_energized_tiles(matrix)
        print(total)
