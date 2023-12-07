from collections import defaultdict
from functools import cmp_to_key

def count_by_card(hand):
    count = defaultdict(int)
    for c in hand:
        count[c] += 1
    sorted_count = sorted(list(count.items()), key=lambda x: x[1], reverse=True)
    if sorted_count[0][0] == "J" and len(sorted_count) > 1:
        return sorted_count[1]
    return sorted_count[0]

def get_hand_type(hand, recursive=0):
    most_repeated_card, repeated_times = count_by_card(hand)

    if "J" in hand and recursive == 0:
        hand = hand.replace("J", most_repeated_card)
        return get_hand_type(hand, recursive+1)

    if all([c == hand[0] for c in hand]):
        return 7, "five_of_kind"
    elif len(set(hand)) == 2 and hand.count(hand[0]) in (1, 4):
        return 6, "four_of_kind"
    elif len(set(hand)) == 2 and hand.count(hand[0]) in (2, 3):
        return 5, "full_house"
    elif len(set(hand)) == 3:
        if repeated_times == 3:
            return 4, "three_of_kind"
        else:
            return 3, "two_pair"
    elif len(set(hand)) == 4:
        return 2, "one_pair"
    else:
        return 1, "high_pair"


def cmp_card(c1, c2):
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    c1_pos = cards.index(c1)
    c2_pos = cards.index(c2)
    if c1_pos < c2_pos:
        return -1
    elif c1_pos > c2_pos:
        return 1
    else:
        return 0


def hand_sorter(h1, h2):
    """
    A comparison function is any callable that accepts two arguments, compares them,
    and returns a negative number for less-than, zero for equality, or a positive number
    for greater-than. A key function is a callable that accepts one argument and returns another value to be used as the sort key.
    """
    v1, _ = get_hand_type(h1)
    v2, _ = get_hand_type(h2)
    if v1 > v2:
        return -1
    elif v1 < v2:
        return 1
    else:
        for ch1, ch2 in zip(h1, h2):
            order = cmp_card(ch1, ch2)
            if order != 0:
                return order
        raise 0



if __name__ == "__main__":
    with open("input7.txt", "r") as f:
        lines = f.readlines()

        bid_by_hand = {}

        for line in lines:
            hand, bid = line.split(" ")
            bid_by_hand[hand] = int(bid)

        total = 0
        rank = len(bid_by_hand)

        hands_sorted = sorted(bid_by_hand.keys(), key=cmp_to_key(hand_sorter))

        for hand in hands_sorted:
            _, type_ = get_hand_type(hand)
            bid = bid_by_hand[hand]
            points = bid * rank
            print(rank, hand, type_, bid)
            total += points
            rank -= 1

        print(total)
