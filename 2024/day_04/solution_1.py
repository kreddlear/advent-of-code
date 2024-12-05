'''
help her with her word search (your puzzle input). She only has to find one word: XMAS.
This word search allows words to be 
horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
It's a little unusual, though, as you don't merely need to find one instance of XMAS - 
you need to find all of them. Here are a few ways XMAS might appear, 
where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

right = (0,1)
left = (0,-1)
up = (-1,0)
down = (1,0)
up_right = (-1,1)
down_right = (1,1)
up_left = (-1,-1)
down_left = (1,-1)
'''

with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def check_specific_coord(coords_to_check, desired_char):
    try:
        row = lines[coords_to_check[0]]
        char = row[coords_to_check[1]]
        if char == desired_char:
            return True
        else:
            return False
    except IndexError:
        return False

def check_x(row_num, col_num, valid_directions, desired_char=0, found=[]):
    chars = ['M','A','S']
    for try_direction in valid_directions:
        row_num_to_check = row_num + try_direction[0]
        col_num_to_check = col_num + try_direction[1]
        found_next = check_specific_coord((row_num_to_check, col_num_to_check), chars[desired_char])
        if found_next:
            if desired_char == 2:
                return found.append((row_num, col_num))
            else:
                next_char = desired_char+1
                if row_num_to_check >= 0 and col_num_to_check >= 0:
                    check_x(row_num_to_check, col_num_to_check, [try_direction], next_char, found)
    return found

count = []
for row_num in range(len(lines)):
    row = lines[row_num]
    for col_num in range(len(row)):
        is_x = check_specific_coord((row_num, col_num), 'X')
        if is_x:
            count = check_x(row_num, col_num, valid_directions=[(0,1),(0,-1),(-1,0),(1,0),(-1,1),(1,1),(-1,-1),(1,-1)])
print(len(count))