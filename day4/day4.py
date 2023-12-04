from collections import defaultdict


def get_points(card):
    card_name, numbers = card.split(":")
    winnin_num, mine_num = numbers.split("|")
    winnin_num = [int(n) for n in winnin_num.strip().split(" ") if n.strip()]
    mine_num = [int(n) for n in mine_num.strip().split(" ") if n.strip()]
    matches = 0
    for n in winnin_num:
        if n in mine_num:
            matches += 1
    return matches


with open("input4.txt", "r") as f:

    scratchcards = defaultdict(int)

    copies = defaultdict(int)
    for i, l in enumerate(f.readlines()):
        i += 1

        scratchcards[i] += 1
        scratchcards[i] += copies[i]

        matches = get_points(l)

        if matches:
            for j in range(1, matches + 1):
                copies[i + j] += scratchcards[i]

    print("Total", sum(scratchcards.values()))
