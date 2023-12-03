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
    gears_at_pos = {}

    for real_y, l in enumerate(lines):
        for m in  re.finditer("(\d+)", l):
            num = m.group(1)
            start, end = m.span()
            num_at_pos[(start, real_y)] = num
            for num_len in range(end - start):
                matrix[real_y][start + num_len] = num

        for m in re.finditer(r"[^\d]", l.strip("\n")):
            if m.group(0) == ".":
                continue
            start, end = m.span()
            if m.group(0) == "*":
                gears_at_pos[(start, real_y)] = "*"
                matrix[real_y][start] = "*"
            else:
                matrix[real_y][start] = "S"

    print(num_at_pos)
    pp(matrix)
    return matrix, num_at_pos, gears_at_pos

def check_neightbours(matrix, position, num):
    len_num = len(num)
    bounds_y = len(matrix)
    bounds_x = len(matrix[0])
    real_x, real_y = position

    for offset in range(len(num)):
        for y in range(real_y-1, real_y+2):
            for x in range(real_x -1 + offset, real_x + 2 + offset):
                # fFix y >= 0, x >= 0 ??
                if y > 0 and y < bounds_y and x > 0 and x < bounds_x:
                    if matrix[y][x] in ("*", "S"):
                        return True
    return False

def check_gear_neightbours(matrix, position):
    len_num = len(num)
    bounds_y = len(matrix)
    bounds_x = len(matrix[0])
    real_x, real_y = position

    adjacent_numbers = set()

    for y in range(real_y-1, real_y+2):
        for x in range(real_x -1 , real_x + 2 ):
            if y >= 0 and y < bounds_y and x >= 0 and x < bounds_x:
                if re.match("\d+", matrix[y][x]):
                    adjacent_numbers.add(int(matrix[y][x]))


    if len(adjacent_numbers) == 2:
        adjacent_numbers = list(adjacent_numbers)
        return adjacent_numbers[0] * adjacent_numbers[1]
    return 0



with open('input3.txt', 'r') as f:
    matrix, nums_at_pos, gears_at_pos = find_numbers(f.readlines())
    part_numbers =[]
    for pos, num in nums_at_pos.items():
        part = check_neightbours(matrix, pos, num)
        if part:
            part_numbers += [int(num)]
    print(part_numbers)
    print(sum(part_numbers))

    gears =[]
    for pos, _ in gears_at_pos.items():
        gear = check_gear_neightbours(matrix, pos)
        if gear:
            gears += [gear]
    print(gears)
    print(sum(gears))
