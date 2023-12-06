from solution import check_num_horiz, check_num_vert, get_num_left, get_num_right

test_array_general = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......'
]

# checking the asterisk at 3,1
symbol_x = 3
symbol_y = 1

# check right
print(check_num_horiz(symbol_x, test_array_general[symbol_y], 1))
# check left
print(check_num_horiz(symbol_x, test_array_general[symbol_y], -1))
# check above
print(check_num_vert(symbol_x, test_array_general[symbol_y-1:symbol_y+2], -1))
# check below
print(check_num_vert(symbol_x, test_array_general[symbol_y-1:symbol_y+2], 1))

