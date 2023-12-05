from collections import defaultdict

def build_map(lines):
    maps = defaultdict(list)

    inside_map = None
    state = None
    for l in lines:
        l = l.strip()
        if inside_map:
            if l != "":
                destination_range_start, source_range_start, range_length = [int(n) for n in l.split(" ")]
                maps[inside_map] += [
                    (source_range_start, source_range_start + range_length - 1,
                     destination_range_start, destination_range_start + range_length -1 )
                ]
            else:
                inside_map = None

        elif l.endswith("map:"):
            map_name = l[:-4].strip()
            inside_map = tuple(map_name.split("-to-"))
    return maps


def find_next(value, type_, maps):
    for (from_, to), ranges in maps.items():
        if from_ == type_:
            for range_ in ranges:
                if value >= range_[0] and value <= range_[1]:
                    offset =  value - range_[0]
                    return range_[2] + offset, to
            else:
                return value, to



with open("input5.txt", "r") as f:
    lines = f.readlines()
    seeds = [int(s) for s in lines[0].split(":")[1].strip().split(" ")]

    maps = build_map(lines[1:])

    location_by_seed = {}
    for seed in seeds:
        type_ = "seed"
        value = seed
        while True:
            new_value, new_type = find_next(value, type_, maps)
            print(type_, value, " => ", new_type, new_value)
            if new_type == "location":
                print("LOCATION ======> ", new_value, "\n")
                location_by_seed[seed] = new_value
                break
            type_ = new_type
            value = new_value


    print(min(location_by_seed.values()))