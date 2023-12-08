from collections import defaultdict
from math import lcm


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

        start_nodes = {n: n for n in nodes_dict.keys() if n.endswith("A")}

        print("START_NODES", start_nodes)

        len_moves = len(moves)

        n_moves = defaultdict(int)
        while not all([n.endswith("Z") for n in start_nodes.values()]):
            for current_node, end_node in start_nodes.items():
                if end_node.endswith("Z"):
                    continue

                n = n_moves[current_node]
                if n < len_moves:
                    move = moves[n]
                else:
                    move = moves[n % len_moves]

                if move == "R":
                    start_nodes[current_node] = nodes_dict[end_node][1]
                else:
                    start_nodes[current_node] = nodes_dict[end_node][0]

                n_moves[current_node] += 1

        # Least common multiple
        lcm = lcm(*list(n_moves.values()))
        print("LCM", lcm)
