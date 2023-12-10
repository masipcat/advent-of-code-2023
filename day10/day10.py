from collections import defaultdict
from unittest import mock

import gc
import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

pipe_connections = {
    "|": ("N", "S"),
    "-": ("E", "W") ,
    "L": ("N", "E") ,
    "J": ("N", "W") ,
    "7":  ("S", "W") ,
    "F":  ("S", "E") ,
    ".":  (None, None),
    "S":  (mock.ANY, mock.ANY),
}

possible_neighbours = [
    (0, 1, "E"),
    (-1, 0, "N"),
    (0, -1, "W"),
    (1, 0, "S"),
]

can_go = {
    "E": ["-", "7", "J", "S"],
    "W": ["-", "L", "F", "S"],
    "N": ["|", "7", "F", "S"],
    "S": ["|", "L", "J", "S"],
}


def find_s(matrix):
    for j, row in enumerate(matrix):
        for i, col in enumerate(row):
            if col == "S":
                return (j, i)
    raise Exception("Not found")


def find_loop(start, matrix, visited):
    current_y, current_x = start
    if visited == []:
        visited = [(current_y, current_x)]

    current_pipe = matrix[current_y][current_x]

    neighbours = [n for n in possible_neighbours if n[2] in pipe_connections[current_pipe]]

    max_ = []

    for move_y, move_x, direction in neighbours:
        next_y, next_x = (current_y + move_y, current_x + move_x)
        if next_y < 0 or next_y >= len(matrix) or next_x < 0 or next_x >= len(matrix[0]):
            continue
        if (next_y, next_x) in visited[-3:-1]:
            continue
        next_pipe = matrix[next_y][next_x]
        # hack!!!
        if next_pipe == "S" and len(visited) > 1:
            # loop ended
            return [(current_pipe, current_y, current_x)]
        if current_pipe == "S" or next_pipe in can_go[direction]:
            # print(current_pipe, f"=>", next_pipe, f"[{next_y},{next_x}]")
            loop = find_loop((next_y, next_x), matrix, visited + [(next_y, next_x)])
            if loop != []:
                if (len(loop) + 1) > len(max_):
                    loop.insert(0, (current_pipe, current_y, current_x))
                    max_ = loop
                continue

    return max_


def find_tiles(loop, matrix):
    size_y, size_x = len(matrix), len(matrix[0])
    new_matrix = [size_x * ["."] for _ in range(size_y)]
    for c, y, x in loop:
        new_matrix[y][x] = c

    total = 0
    for y in range(size_y):
        for x in range(size_x):
            is_inside = is_point_inside_loop((y, x), loop)
            if is_inside:
                new_matrix[y][x] = "I"
                total += 1

    return total


pipe_direction = {
    "F": "E",
    "7": "W",
    "J": "W",
    "L": "E",
}


def is_point_inside_loop(point, loop):
    """
    https://stackoverflow.com/a/24721030

    Count the number of intersections of this line with the line segments that make up the perimeter of your polygon.
    If it is odd, the point is inside. If even, it is outside.
    """

    points_in_loop = [
        (v[1], v[2]) for v in loop
    ]

    y, x = point

    # This point is part of the loop
    if (y, x) in points_in_loop:
        return False

    h_points_in_loop = {
        (v[1], v[2]): v[0] for v in loop
        if v[0] in "-|FJL7S"
    }

    pipes = []
    for y in range(y):
        if (y, x) in h_points_in_loop:
            pipe = h_points_in_loop[(y, x)]
            pipes += [pipe]

    count = 0
    prev_pipe = None
    for pipe in pipes:
        if pipe == "|":
            pass

        elif pipe == "S":
            count += 1
            prev_pipe = None

        elif pipe == "-":
            count += 1
            prev_pipe = None

        elif prev_pipe is None:
            count += 1
            prev_pipe = pipe

        elif pipe_direction[prev_pipe] == pipe_direction[pipe]:
            count += 1
            prev_pipe = None

        else:
            prev_pipe = None

    return count % 2 != 0


if __name__ == "__main__":
    with open("input10.txt", "r") as f:
        matrix = [l.strip() for l in f.readlines()]
        start = find_s(matrix)
        loop = find_loop(start, matrix, [])
        print(loop)
        total = find_tiles(loop, matrix)
        print(total)
