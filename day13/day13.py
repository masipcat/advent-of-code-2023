from collections import defaultdict


def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix += [[matrix[j][i] for j in range(len(matrix))]]
    return new_matrix


def find_vertical(matrix):
    matrix = transpose(matrix)
    return find_horizontal(matrix)


def find_horizontal(matrix):
    max_rows = 0

    # Check if first row matches with another row
    first_row = matrix[0]
    start, end = 0, None
    for i, row in enumerate(matrix[::-1]):
        end = len(matrix) - 1 - i
        if row == first_row and start != end:
            rows = check_if_mirrors(matrix, start, end)
            if rows > max_rows:
                max_rows = rows

    # Check if last row matches with another row
    last_row = matrix[-1]
    start, end = None, len(matrix) - 1
    for i, row in enumerate(matrix):
        start = i
        if row == last_row and start != end:
            rows = check_if_mirrors(matrix, start, end)
            if rows > max_rows:
                max_rows = rows

    return max_rows


def check_if_mirrors(matrix, start, end):
    # check the rest of the rows match
    while True:
        if matrix[start] != matrix[end]:
            return 0

        if start - end == 1:
            return start

        start += 1
        end -= 1


def main():
    with open("input13.txt", "r") as f:
        matrices = f.read().strip().split("\n\n")

    total = 0
    for m in matrices:
        m = m.strip().split("\n")

        n_rows = find_horizontal(m)
        n_cols = find_vertical(m)

        total += n_cols + n_rows * 100

    print("total", total)


main()
