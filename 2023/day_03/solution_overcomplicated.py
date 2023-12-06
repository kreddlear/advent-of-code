'''
Add up all the part numbers.

Any number adjacent to a symbol, even diagonally, 
is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)
'''

import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = []
    for line in f.readlines():
        contents.append(line.strip())

test_index_right = 2
test_index_left = 8
test_line_left = '.333.617*......'
test_line_right = '..*617...'
right = 1
left = -1

def check_num_horiz(symbol_index, string, right_or_left):
    # check if there's a num to the side of the provided index
    # in the provided string
    # right_or_left is either 1 or -1
    try:
        int(string[symbol_index+right_or_left])
        return True
    except:
        return False

# print(check_num_horiz(test_index_right, test_line_right, right))
# print(check_num_horiz(test_index_left, test_line_left, left))

test_index_above = 3
test_array_above = ['...3..','...*..','.......']

test_index_below = 4
test_array_below = ['.......','....*.','....4.']

above = -1
below = 1

def check_num_vert(symbol_index, row_array, above_or_below):
    # check if there's a num above or below the provided index
    # in one of the provided rows in the array
    print(row_array)
    current_row = 1
    row_to_check = row_array[current_row+above_or_below]
    try:
        int(row_to_check[symbol_index])
        return True
    except:
        return False

# print(check_num_vert(test_index_above, test_array_above, above))
# print(check_num_vert(test_index_below, test_array_below, below))

# assuming there's a num adjacent right, get num right
def get_num_right(string_right):
    num = re.search('\d+', string_right)
    return int(num.group(0)), len(num.group(0))

# num, num_length = get_num_right(test_index, test_line_right[test_index+1:])

# assuming there's a num adjacent left, get num left
def get_num_left(symbol_x, string_left):
    print(string_left)
    # find all, return last num
    nums_left = re.findall('\d+', string_left)
    last_num = nums_left[-1]
    return int(last_num), len(last_num)

# num, num_length = get_num_left(test_index, test_line_left[:test_index])

def check_all_directions(symbol_location_tuple, array_of_3_rows):
    pass

# check_all_directions()

# first off: what even is a symbol
# i could just troll through the input with a regex
symbol_locs = set()
symbols = re.finditer('[^.0-9]', test_line_right)
for symbol in symbols:
    # get the position where the symbol is
    # store the symbol index (x)
    symbol_x = symbol.start()
    # store the symbol row num (y)
    symbol_row = 0
    # then store the x and y in a set as a tuple
    symbol_locs.add((symbol_x, symbol_row))

    # well...wait maybe I don't even need to store the symbols
    # maybe I can just use the regex to look for symbols,
    # and when one is found, then check nearby for numbers

    # so the thing is that i don't want to use a set
    # because a number could appear more than once
    # BUT if a number is next to multiple symbols...
    # i only want to include it once

# so that means I have to store the number
# AND its location
# and put THAT in a set
# ...as a nested touple i guess?

    # check right
    # pass in symbol index and string from that point on


    # check left

# print(symbol_locs)

# so I can definitely use re
# at least to get a position horizontally
# and then it's vertically that will be different

# so look for symbols
# and then look for numbers adjacent to them??
# because a symbol is only one char

# horizontally will be easier so i'll do it first

