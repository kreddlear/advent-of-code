# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

# If two hands have the same type, a second ordering rule takes effect.
# Start by comparing the first card in each hand. 
# If these cards are different, the hand with the stronger first card is considered stronger. 
# If the first card in each hand have the same label, however, 
# then move on to considering the second card in each hand, and so on.

# each hand is followed by its bid amount

# determine the total winnings of this set of hands 
# by adding up the result of multiplying each hand's bid with its rank (1 lowest)
# (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5)

from collections import Counter

with open('./input_test.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]

# test = [2, 1, 1, 1]

def hand_scoring(count_list):
    # error handling
    if sum(count_list) != 5:
        raise Exception("invalid hand")

    # five is highest
    if count_list[0] == 5:
        return 7
    elif count_list[0] == 4:
        return 6
    elif count_list[0] == 3:
        # could either be full house
        if count_list[1] == 2:
            return 5
        # or 3 of a kind
        elif count_list[1] == 1:
            return 4
    elif count_list[0] == 2:
        # count either be 2 pair
        if count_list[1] == 2:
            return 3
        # or 2 of a kind
        elif count_list[1] == 1:
            return 2
    elif count_list[0] == 1:
        return 1

# print(hand_scoring(test))

hands_grouped = {}

# parsing input
for line in lines:
# line = '32T3K 765'

    # split into cards and bid
    line_split = line.split(' ')
    bid = int(line_split[1])

    hand = line_split[0]
    counter = Counter(hand)

    # maybe I could create dicts for the hand
    # and then count how many elements they end up with?
    # isn't there something in Python that does this already...
    # yes collections.Counter - i.e. Counter({'K': 2, '7': 2, '6': 1})
    # and _count = Counter()
    # care most about highest nums
    sorted_counter = sorted(counter.values(), reverse=True)
    print(sorted_counter) # [2, 1, 1, 1]

    print(hand_scoring(sorted_counter))
    # then store...the counter and return a tuple??

# print(hands)

# can you iterate over a counter?


# so maybe first sort everything by the "of a kind" ordering
# and then within that, sort them within each "of a kind" group