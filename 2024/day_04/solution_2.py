"""
Looking for the instructions, you flip over the word search to find that this isn't
actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed
to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

So, there are 9 in the example below:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

up_right = (-1,1)
down_right = (1,1)
up_left = (-1,-1)
down_left = (1,-1)
"""

# okay, so actually my previous solution could still sorta work.
# instead of starting by looking for Xs, I'll start by looking for As

from solution_1 import check_specific_coord

with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def check_x(row_num, col_num):
    chars = ['M','M','S','S']
    valid_directions = [(-1,1),(1,1),(-1,-1),(1,-1)]
    list_of_chars = {}
    for try_direction in valid_directions:
        row_num_to_check = row_num + try_direction[0]
        col_num_to_check = col_num + try_direction[1]
        if row_num_to_check >= 0 and col_num_to_check >= 0:
            try:
                char = lines[row_num_to_check][col_num_to_check]
            except IndexError:
                return False
            list_of_chars[(row_num_to_check, col_num_to_check)] = char
        else:
            return False
    if (
        sorted(list_of_chars.values()) != chars
        # lazy check for diagonal same
        or list_of_chars[(row_num+1, col_num+1)] == list_of_chars[(row_num-1, col_num-1)]
    ):
        return False
    else:
        return True

count = 0
for row_num in range(len(lines)):
    row = lines[row_num]
    for col_num in range(len(row)):
        is_a = check_specific_coord((row_num, col_num), 'A')
        if is_a:
            if check_x(row_num, col_num):
                count += 1
print(count)