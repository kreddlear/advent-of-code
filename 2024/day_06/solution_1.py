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

with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)
facing_order = [up, right, down, left]

# parse input
obstacles = []
for i, line in enumerate(lines):
    if '^' in line:
        position = (i, line.index('^'))
        print("starting position is", position)
        facing = up
    # find all # in line
    obstacle_matches = re.finditer('#', line)
    for obstacle_match in obstacle_matches:
        obstacles.append((i, obstacle_match.start()))
# print(position, obstacles)

visited_positions = set()
visited_positions.add(position)

while True:
    # print(position)
    new_position = position[0] + facing[0], position[1] + facing[1]
    if new_position[0] < 0 or new_position[0] >= len(lines) or new_position[1] < 0 or new_position[1] >= len(lines[0]):
        # print("oops, new_position is",new_position)
        break
    if new_position in obstacles:
        # print("hit an obstacle at", new_position)
        try:
            facing = facing_order[facing_order.index(facing)+1]
        except IndexError:
            facing = facing_order[0]
        # print("now facing", facing)
    else:
        position = new_position
        visited_positions.add(position)

# print(visited_positions)
visited_positions_1 = visited_positions
print(visited_positions)