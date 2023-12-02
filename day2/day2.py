# only 12 red cubes, 13 green cubes, and 14 blue cubes?
dedired = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_game(line):
    [game_num, games] = line.split(":")
    game_num = int(game_num[5:])
    games = games.split(";")
    print("Game", game_num)

    min_each_color = {
        "red": None,
        "green": None,
        "blue": None
    }

    possible = True
    for g in games:
        for color in g.split(","):
            color_count, color = color.strip().split(" ", 2)
            color_count = int(color_count)
            if color_count > (min_each_color[color] or 0):
                min_each_color[color] = color_count
            if color_count > dedired[color] :
                possible = False

    power = 1
    print(min_each_color)
    for min_ in min_each_color.values():
        power *= min_ or 1
    return game_num, possible, power


with open("input2.txt", "r") as f:
    total = 0
    total_powers = 0
    for l in f.readlines():
        game_num, possible, power = parse_game(l)
        print(game_num, power)
        if possible:
            total += game_num
        total_powers += power
    print("total", total)
    print("total_power", total_powers)