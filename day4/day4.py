def get_points(card):
    card_name, numbers = card.split(":")
    winnin_num, mine_num = numbers.split("|")
    winnin_num = [int(n) for n in winnin_num.strip().split(" ") if n.strip()]
    mine_num = [int(n) for n in mine_num.strip().split(" ")  if n.strip()]
    matches = 0
    for n in winnin_num:
        if n in mine_num:
            matches += 1
    if matches:
        return 2**(matches - 1)
    else:
        return 0



with open('input4.txt', 'r') as f:
    total = 0
    for l in f.readlines():
        total += get_points(l)
    print("Total", total)
