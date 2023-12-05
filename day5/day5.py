from collections import defaultdict

def build_map(lines):
    maps = defaultdict(lambda: [None, []])

    inside_map = None
    state = None
    for l in lines:
        l = l.strip()
        if inside_map:
            if l != "":
                destination_range_start, source_range_start, range_length = [int(n) for n in l.split(" ")]
                maps[inside_map][1] += [
                    (source_range_start, source_range_start + range_length - 1,
                     destination_range_start, destination_range_start + range_length -1 )
                ]
            else:
                inside_map = None

        elif l.endswith("map:"):
            map_name = l[:-4].strip()
            [inside_map, to] = tuple(map_name.split("-to-"))
            maps[inside_map][0] = to
    return maps


def find_next(value, type_, maps):
    to, ranges = maps[type_]
    for (src_range_start, src_range_end, dst_range_start, _) in ranges:
        if value >= src_range_start and value <= src_range_end:
            offset = value - src_range_start
            return dst_range_start + offset, to

    return value, to


def find_prev(value, type_, maps):
    for from_, (to, ranges) in maps.items():
        if to == type_:
            break

    for (src_range_start, src_range_end, dst_range_start, dst_range_end) in ranges:
        if value >= dst_range_start and value <= dst_range_end:
            offset = value - dst_range_start
            return src_range_start + offset, from_

    if from_ == "seed":
        return None, from_
    return value, from_


def get_seeds_range(seeds):
    return [
         seeds[2*i:2*i+2]
        for i in range(len(seeds) // 2)
    ]

def get_seeds(seeds):
    for source, length in get_seeds_range(seeds):
        for i in range(length):
            val = source + i
            yield val


def get_locations(maps):
    for to, ranges in maps.values():
        if to == "location":
            for (_, _, dst_range_start, dst_range_end) in sorted(ranges, key=lambda x: x[2]):
                for l in range(dst_range_start, dst_range_end):
                    yield l
            break


def check_location_match_seeds(value, seeds_ranges, maps):
    type_ = "location"
    location = value
    while True:
        new_value, new_type = find_prev(value, type_, maps)
        if new_type == "seed":
            if new_value is not None:
                for (source, length) in seeds_ranges:
                    if new_value >= source and new_value <= (source+length):
                        return location
            break

        type_ = new_type
        value = new_value

    return None


if __name__ == "__main__":
    with open("input5.txt", "r") as f:
        lines = f.readlines()
        seeds = [int(s) for s in lines[0].split(":")[1].strip().split(" ")]

        maps = build_map(lines[1:])

        seeds_ranges = get_seeds_range(seeds)

        for value in get_locations(maps):
            found = check_location_match_seeds(value, seeds_ranges, maps)
            if found:
                print("first", found)
                break

        lowest_location = None
        for value in range(0, found):
            found = check_location_match_seeds(value, seeds_ranges, maps)
            if found:
                if lowest_location is None or found < lowest_location:
                    lowest_location = found
                    print("second", found)

        print(lowest_location)
