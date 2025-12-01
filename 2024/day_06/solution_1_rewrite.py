'''
The map shows the current position of the guard with ^ 
(to indicate the guard is currently facing up from the perspective of the map). 
Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.

Predict the path of the guard. How many distinct positions 
will the guard visit before leaving the mapped area?
'''

import re
from itertools import cycle

with open('./input_test.txt') as f:
    lines = [line.strip() for line in f.readlines()]

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)
facing_order = cycle([up, right, down, left])
facing = next(facing_order)

# parse input
obstacles = []
mapped_grid = {}
for row, line in enumerate(lines):
    for col, coord_value in enumerate(line):
        mapped_grid[row, col] = coord_value
        if coord_value == '^':
            position = (row, col)
print("starting position is", position)

print(mapped_grid)

# visited_positions = set()
# visited_positions.add(position)

# while True:
#     # print(position)
#     new_position = position[0] + facing[0], position[1] + facing[1]
#     if new_position[0] < 0 or new_position[0] >= len(lines) or new_position[1] < 0 or new_position[1] >= len(lines[0]):
#         # print("oops, new_position is",new_position)
#         break
#     if new_position in obstacles:
#         # print("hit an obstacle at", new_position)
#         facing = next(facing_order)
#         # print("now facing", facing)
#     else:
#         position = new_position
#         visited_positions.add(position)

# # print(visited_positions)
# visited_positions_1 = visited_positions
# print(len(visited_positions))