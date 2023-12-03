import re

def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("\n")

def find_numbers(lines):
    # TODO: this could be rewritten just replacing all symbols with 'S',
    # without creating a matrix
    y = len(lines)
    x = len(lines[0])
    matrix = [x * [' '] for _ in range(y)]
    print(matrix)

    num_at_pos = {}

    for real_y, l in enumerate(lines):
        for m in  re.finditer("(\d+)", l):
            num = m.group(1)
            start, end = m.span()
            num_at_pos[(start, real_y)] = num
            print(num)
            for num_len in range(end - start):
                matrix[real_y][start + num_len] = "X"

        for m in re.finditer(r"[^\d]", l.strip("\n")):
            if m.group(0) == ".":
                continue
            start, end = m.span()
            matrix[real_y][start] = "S"

    print(num_at_pos)
    pp(matrix)
    return matrix, num_at_pos

def check_neightbours(matrix, position, num):
    len_num = len(num)
    bounds_y = len(matrix)
    bounds_x = len(matrix[0])
    real_x, real_y = position

    for offset in range(len(num)):
        for y in range(real_y-1, real_y+2):
            for x in range(real_x -1 + offset, real_x + 2 + offset):
                if y > 0 and y < bounds_y and x > 0 and x < bounds_x:
                    if matrix[y][x] == "S":
                        return True
    return False


with open('input3.txt', 'r') as f:
    matrix, nums_at_pos = find_numbers(f.readlines())
    part_numbers =[]
    for pos, num in nums_at_pos.items():
        part = check_neightbours(matrix, pos, num)
        if part:
            part_numbers += [int(num)]
    print(part_numbers)
    print(sum(part_numbers))

