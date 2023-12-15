def pp(matrix):
    for row in matrix:
        for val in row:
            print(val, end="")
        print("")


def move_up(matrix, j, i):
    if matrix[j][i] == "O" and matrix[j - 1][i] == ".":
        matrix[j - 1][i] = matrix[j][i]
        matrix[j][i] = "."
        if j > 1:
            move_up(matrix, j - 1, i)


def move_north(matrix):
    for j in range(1, len(matrix)):
        for i in range(len(matrix[j])):
            move_up(matrix, j, i)
    return matrix


def sum_load(matrix):
    matrix = matrix[::-1]
    total = 0
    for j in range(len(matrix)):
        total += matrix[j].count("O") * (j + 1)
    return total


if __name__ == "__main__":
    with open("input14.txt", "r") as f:
        matrix = f.read().strip()
        matrix = [list(l) for l in matrix.split("\n")]
        new_matrix = move_north(matrix)
        pp(new_matrix)
        load = sum_load(new_matrix)
        print(load)
