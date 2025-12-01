# okay so for this one we're trying to get them stuck in a loop
# by adding a single obstruction
# so i guess my first question is...how do we define a loop?

# man i don't know how to do this without being super inefficient

# maybe i try to get them BACK on the path they already went on?
# because we already know where they will go, and that they ended up at the obstacle on that path?
# so could i start tracking not just obstacles, but obstacles that have been hit
# and what direction the guard was facing when hit
# and then check if:
# there are any obstacles in the NEXT direction from the one they're facing (row or column)
# that they have already hit facing in that next direction?
# because if so, adding an obstacle would result in them getting back on the same path

import re
# from solution_1 import visited_positions_1

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
        start_position = (i, line.index('^'))
        # print("starting position is", start_position)
        facing = up
    obstacle_matches = re.finditer('#', line)
    for obstacle_match in obstacle_matches:
        obstacles.append((i, obstacle_match.start()))

# okay, so...another while loop
visited_positions = set()
visited_positions.add(start_position)

# this is (obstacle_coord): (facing)
# i.e. {(0, 4): (-1, 0)}
hit_obstacles = {}

possible_obstacles = 0
possible_obstacles_list = []

def take_position_and_go(starting_position, facing, obstacle_list, hit_obstacles={}): # , potential_obstacle=None):
    # hit_obstacles is (obstacle_coord): { facing : hit_times }
    # i.e. { (5,6): { (0,0): 4 } }
    loop = False
    while True:
        # print("starting while loop with position", starting_position)
        new_position = starting_position[0] + facing[0], starting_position[1] + facing[1]
        if new_position[0] < 0 or new_position[0] >= len(lines) or new_position[1] < 0 or new_position[1] >= len(lines[0]):
            # print("left the map at", new_position)
            break
        elif new_position in obstacle_list:
            # track which obstacles i've hit
            # print("hit an obstacle at", new_position, "facing", facing)
            if new_position not in hit_obstacles:
                hit_obstacles[new_position] = { facing: 1 }
            else: # it is in hit_obstacles
                if facing in hit_obstacles[new_position]:
                    # add one
                    hit_obstacles[new_position][facing] += 1
                    if hit_obstacles[new_position][facing] >= 500:
                        # assume if we've hit the same obstacle facing the same direction 4x
                        # we're in a loop and should break
                        loop = True
                        break
                else:
                    hit_obstacles[new_position][facing] = 1
                    # otherwise continue
            # handle turning
            try:
                facing = facing_order[facing_order.index(facing)+1]
            except IndexError:
                # start from the top
                facing = facing_order[0]
            # print("now facing", facing)
        else:
            starting_position = new_position
    # return either False (goes off map) or True (loops)
    # print("loop is", loop)
    return loop

# test if I add a looping obstacle, if it detects it properly
# expected: (1,1), (1,3), (4,0)
# obstacles.append((1,3))
# take_position_and_go(start_position, facing, obstacles)

position = start_position
starting_original_position = start_position
facing = up
print("starting second runthrough with position", position)
while True:
    # print("******************************")
    # print(position)
    new_position = position[0] + facing[0], position[1] + facing[1]
    if new_position[0] < 0 or new_position[0] >= len(lines) or new_position[1] < 0 or new_position[1] >= len(lines[0]):
        # print("left the map at", new_position)
        break
    elif new_position in obstacles:
        # track which obstacles i've hit
        # print("hit an obstacle at", new_position, "facing", facing)
        if new_position not in hit_obstacles:
            hit_obstacles[new_position] = { facing: 1 }
        else: # it is in hit_obstacles
            if facing in hit_obstacles[new_position]:
                # add one
                hit_obstacles[new_position][facing] += 1
            else:
                hit_obstacles[new_position][facing] = 1
        # print(hit_obstacles)

        # handle turning
        try:
            facing = facing_order[facing_order.index(facing)+1]
        except IndexError:
            # start from the top
            facing = facing_order[0]
    else:
        # check in the direction they would turn next IF there were an obstacle
        # ...where??? in front of in front of them
        # okay so I need to store that position because that's what the loop will test
        potential_obstacle_position = new_position[0] + facing[0], new_position[1] + facing[1]

        # if there's already an obstacle here...don't bother!!!
        if (
            potential_obstacle_position not in obstacles 
            and potential_obstacle_position != starting_original_position
        ):
            new_obstacles = list(obstacles)
            new_obstacles.append(potential_obstacle_position)

            # also calculate what direction they would face if they turned now
            try:
                next_facing = facing_order[facing_order.index(facing)+1]
            except IndexError:
                next_facing = facing_order[0]
            # set this so i can use/set it in the while loop without poisoning it
            new_new_position = new_position
        
            # print("calculating potential obstacle at", potential_obstacle_position)
            loop = take_position_and_go(new_new_position, next_facing, new_obstacles, hit_obstacles)
            # print("loop?", loop)
            if loop: # and new_new_position in visited_positions_1:
                # run it again to confirm it works from the beginning
                # otherwise throw it out
                # print("rerunning to check", starting_original_position)
                loop = take_position_and_go(starting_original_position, up, new_obstacles, hit_obstacles)
                if loop:
                    # print("potential obstacle found", potential_obstacle_position)
                    possible_obstacles_list.append(potential_obstacle_position)
                    possible_obstacles += 1
                # else:
                #     print("throwing out, doesn't work")
        position = new_position
        visited_positions.add(position)

# print(hit_obstacles)
print(possible_obstacles)
# print(possible_obstacles_list)
# this should be: [(6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)]
# damn my solution 580 is not working for the main input...sighhh too low

# okay now i'm getting (3, 4) and (1, 7) which shouldn't be in there
# okay but actually looking at it, (3, 4) is kind of valid??
# ohh no wait it's not because the guard would go off the map
# so like he hit the obstacle again facing the same direction but then still go off the map
# sighhh

# ooookay this new input here https://old.reddit.com/r/adventofcode/comments/1h8in8j/day_6_help/m0t7mlt/
# i think will help
# i'm only getting 1 when i should be getting 3
# so the guard gets stuck in a loop on obstacles they have not hit before
# so i think my solution of relying on obstacles they have hit before won't work

# can i just have a method that takes a position and a direction and runs it through the while loop
# and tracks the obstacles it hits
# and breaks if it either goes off the map or hits an obstacle 4x?
# that will take forever though...but maybe worth a try