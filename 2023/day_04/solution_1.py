import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]

test_line = 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'

total_points = 0

for card_num, line_text in enumerate(lines):

    my_nums_raw = line_text.split('|')[-1]
    my_nums = re.findall('\d+', my_nums_raw)

    winning_nums_raw = line_text.split(':')[-1].split('|')[0]
    winning_nums = re.findall('\d+', winning_nums_raw)

    card_points = 0

    for num in my_nums:
        if num in winning_nums:
            if card_points == 0:
                card_points = 1
            else:
                card_points = card_points * 2

    total_points += card_points

print(total_points)