from collections import defaultdict
from functools import cmp_to_key


if __name__ == "__main__":
    with open("input8.txt", "r") as f:
        lines = f.readlines()
        moves = lines[0].strip()
        nodes = lines[2:]

        nodes_dict = {}

        for n in nodes:
            node, dest = n.split(" = ")
            lnode, rnode = dest[1:-2].split(",")
            nodes_dict[node] = (lnode.strip(), rnode.strip())

        n_moves = 0
        current_node = "AAA"

        while True:
            if n_moves < len(moves):
                move = moves[n_moves]
            else:
                move = moves[n_moves % len(moves) ]

            n_moves += 1

            if move == "R":
                current_node = nodes_dict[current_node][1]
            else:
                current_node = nodes_dict[current_node][0]

            if current_node == "ZZZ":
                break

        print("Total moves", n_moves)
