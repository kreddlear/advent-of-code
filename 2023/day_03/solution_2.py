import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]

star_locs = set()
star_loc_counts = {}
number_locs = {}

for line_num, line in enumerate(lines):

    # find all the stars
    symbols = re.finditer('\*', line)
    for symbol in symbols:
        # get the position where the symbol is
        symbol_x = symbol.start()
        # store the symbol row num (y)
        symbol_y = line_num
        # then store the x and y in a set as a tuple
        star_locs.add((symbol_x, symbol_y))
        star_loc_counts[(symbol_x, symbol_y)] = []

    # find all the numbers, store location and value
    nums_in_line = re.finditer('\d+', line)
    for num_match in nums_in_line:
        # get the value of the number
        num_value = num_match.group()
        # get the location of the number
        num_loc_x = num_match.start()
        num_loc_y = line_num
        number_locs[(num_loc_x,num_loc_y)] = num_value

nums_with_symbol = []

# okay, now figure out for each number if there's a symbol adjacent...
for num_loc in number_locs:
    # num_loc = (6,2) # 633
    # print(number_locs[num_loc])
    len_num = len(number_locs[num_loc])
    # print("length", len_num)

    surrounding_locations = []

    # for right, just account for the length of the number
    right = (num_loc[0]+len_num,num_loc[1])
    surrounding_locations.append(right)

    left = (num_loc[0]-1,num_loc[1])
    surrounding_locations.append(left)

    # need to check each index above each digit
    for x in range(num_loc[0]-1,num_loc[0]+len_num+1): # 5, 9
        up = (x,num_loc[1]-1)
        surrounding_locations.append(up)

        down = (x,num_loc[1]+1)
        surrounding_locations.append(down)

    # print(surrounding_locations)

    for sur_loc in surrounding_locations:
        # print("checking",sur_loc)
        if sur_loc in star_locs:
            star_loc_counts[sur_loc].append(int(number_locs[num_loc]))

sum_gear_ratios = 0

for star_loc in star_loc_counts:
    if len(star_loc_counts[star_loc]) == 2:
        sum_gear_ratios += star_loc_counts[star_loc][0] * star_loc_counts[star_loc][1]

print(sum_gear_ratios)