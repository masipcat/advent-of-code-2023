from collections import defaultdict

def num_of_ways_to_win(time, distance):
    ways = []
    for hold_time in range(time):
        speed = hold_time * 1
        race_duration = time - hold_time
        if race_duration * speed > distance:
            ways += [hold_time]
    print(ways, "=", len(ways))
    return len(ways)

if __name__ == "__main__":
    with open("input6.txt", "r") as f:
        lines = f.readlines()
        times = [t.strip() for t in lines[0].split("Time: ")[1].split(" ") if t.strip()]
        distances = [d.strip() for d in lines[1].split("Distance: ")[1].split(" ") if d.strip()]

        time = int("".join(times))
        distance = int("".join(distances))

        n_ways = num_of_ways_to_win(time, distance)
        print(time, distance, "=", n_ways)
        total = n_ways

        print("TOTAL", total)

