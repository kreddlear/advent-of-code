import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]

test_line = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'

def calculate_down(card_dict, currently_processing):
    # print("currently processing", currently_processing)
    # print("copies: ",card_dict[currently_processing]['card_copies'])
    for y in range(0,card_dict[currently_processing]['card_copies']):
        # print("copy number",y+1)
        
        one_more_than_card = currently_processing+1
        # print(one_more_than_card) # 2, then 3

        # for some reason this is the problem child
        # it's not as big as it should be
        # 1 is worth 4 so +2 = 6 (because it should do 5)
        # 2 is worth 2 so +2 = 4??? but that's not right, it should be 5
        # ohhh it's one_more_than_card plus the worth!!!
        end_card_worth = one_more_than_card + card_dict[currently_processing]['card_worth']
        # print(end_card_worth)
        
        for x in range(one_more_than_card,end_card_worth):
            # print("adding one to", x)
            card_dict[x]['card_copies'] += 1
    card_dict[currently_processing]['done'] = True

    return card_dict

card_copies_and_values = {
    # card_num : {card_copies, card_worth}
}

# go through and figure out how many copies of each card I end up with
# and how many points each one is worth
for card_num, line_text in enumerate(lines, start=1):

    my_nums_raw = line_text.split('|')[-1]
    my_nums = re.findall('\d+', my_nums_raw)

    winning_nums_raw = line_text.split(':')[-1].split('|')[0]
    winning_nums = re.findall('\d+', winning_nums_raw)

    card_copies_and_values[card_num] = {}

    card_copies_and_values[card_num]['card_copies'] = 1
    card_copies_and_values[card_num]['done'] = False

    card_points = 0

    for num in my_nums:
        if num in winning_nums:
            card_points += 1

    card_copies_and_values[card_num]['card_worth'] = card_points

for card in card_copies_and_values:
    card_copies_and_values = calculate_down(card_copies_and_values, card)

total_cards_won = 0

for card in card_copies_and_values:
    total_cards_won += card_copies_and_values[card]['card_copies']

print(total_cards_won)

'''
1 instance of card 1
2 instances of card 2
4 instances of card 3
8 instances of card 4
14 instances of card 5
1 instance of card 6

sum: 30
'''