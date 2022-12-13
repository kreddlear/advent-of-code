with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.lower().strip() for line in f.readlines()]

# concern: will they ever have the step go into the negatives?
# that would screw things up!
# nope doesn't seem that way

def move_tail(tail,head):
    # return a set of places tail has visited and a new tail pos
    # ex head at 0,0 tail at 4,0
    x_delta = head[0] - tail[0] # -4
    abs_x = abs(x_delta)
    y_delta = head[1] - tail[1] # 0
    abs_y = abs(y_delta)

    list_of_coords = set()

    no_movement = {
        'tail_pos': tail,
        'list_of_coords': list_of_coords
    }

    # okay what if we check one at a time.
    # what's okay and doesn't need movement:

    # adjacent i.e.
    # if abs_x == 0 and abs_y < 2 i.e if not abs_x
    if not abs_x:
        if not abs_y:
            # literally overlapping, no movement needed
            return no_movement
        # head at 0,0 tail at 0,1
        elif abs_y < 2:
            # adjacent, no movement needed
            return no_movement
        else:
            # update y till it's only 1 away from head[y]
            for y in range(0,abs_y-1):
                # if positive, increase tail[y]
                # i.e. head at 0,2 tail at 0,0 => tail at 0,1
                if y_delta > 0:
                    tail[1] += 1
                # if negative, decrease tail[y]
                # i.e. head at 0,0 tail at 0,2 => tail at 0,1
                if y_delta < 0:
                    tail[1] -= 1
                list_of_coords.add((tail[0],tail[1]))

    # if abs_x < 2 and abs_y == 0 i.e if not abx_y
    elif not abs_y:
        # head at 0,0 tail at 1,0
        if abs_x < 2:
            # adjacent, no movement needed
            return no_movement
        else:
            # TODO update x till it's only 1 away from head[x]
            for x in range(0,abs_x-1):
                # if positive, increase tail[y]
                # i.e. head at 0,2 tail at 0,0 => tail at 0,1
                if x_delta > 0:
                    tail[0] += 1
                # if negative, decrease tail[y]
                # i.e. head at 0,0 tail at 0,2 => tail at 0,1
                if x_delta < 0:
                    tail[0] -= 1
                list_of_coords.add((tail[0],tail[1]))

    # diagonally adjacent i.e.
    # head at 0,0 tail at 1,1
    # if abx_x < 2 and abs_y < 2
    elif abs_x < 2 and abs_y < 2:
        # this is fine, no movement needed
        return no_movement

    # else if not adjacent AND not same row OR col
    # else if both exist and one/both greater than or equal to 2
    # ex tail at 1,1 head at 2,3 => tail goes to 2,2
    elif abs_x and abs_y:
        # TODO fix this all up
        # move diagonally till in adjacent row/col
        # if both pos
        # how do i check if it's in an adj row/col??

        max_num = max(abs_x,abs_y)
        for row_or_col in range(0,min(abs_x,abs_y)):
            # if x delta positive, increase tail[0]
            if x_delta > 0:
                tail[0] += 1
            # if x delta negative, decrease tail[0]
            elif x_delta < 0:
                tail[0] -= 1
            # if y delta positive, increase tail[1]
            if y_delta > 0:
                tail[1] += 1
            # if y delta negative, decrease tail[1]
            elif y_delta < 0:
                tail[1] -= 1
            list_of_coords.add((tail[0],tail[1]))
            max_num -= 1
        # figure out which was bigger
        for row_or_col in range(0,max_num-1):
            if abs_x > abs_y:
                # there's still x movement, move till it's over
                # if x delta positive, increase tail[0]
                if x_delta > 0:
                    tail[0] += 1
                # if x delta negative, decrease tail[0]
                elif x_delta < 0:
                    tail[0] -= 1
                list_of_coords.add((tail[0],tail[1]))
            elif abs_y > abs_x:
                # there's still y movement, move till it's over
                # if y delta positive, increase tail[1]
                if y_delta > 0:
                    tail[1] += 1
                # if y delta negative, decrease tail[1]
                elif y_delta < 0:
                    tail[1] -= 1
                list_of_coords.add((tail[0],tail[1]))


    # calc_tail_pos(tail,new_tail)
    return {
        'tail_pos': tail,
        'list_of_coords': list_of_coords
    }

# head at 0,2 tail at 0,0 -> new_tail should be at 0,1
test_tail_pos = [4,3]
test_head_pos = [0,2]
# move_tail(test_tail_pos,test_head_pos)

def move_head(current_head_position, current_tail_position, movement):
    # move head
    # print("moving from",current_head_position,"using direction, number in",movement)
    # 0 or 1
    which_index_to_update = movement[0]
    delta = movement[1]
    # ending head position
    current_head_position[which_index_to_update] += delta

    new_tail_info = move_tail(current_tail_position, current_head_position)

    return {
        'head_pos': current_head_position,
        'tail_info': new_tail_info # tail pos and set of tail coords
    }

test_instruction = [0,-3]
# move_head([4,0],[0,0],test_instruction)

def setup(lines):
    list_of_parsed_directions = []
    for line in lines:
        line_list = line.split()
        # if r/l, update index 0
        # if u/d, update index 1
        if line_list[0] in ["l","r"]:
            index_to_update = 0
        else:
            index_to_update = 1
        # if left or down, make it negative
        if line_list[0] in ["l","d"]:
            delta = int(f'-{line_list[1]}')
        else:
            delta = int(line_list[1])
        parsed_direction = [index_to_update,delta]
        list_of_parsed_directions.append(parsed_direction)
    return list_of_parsed_directions

def main(everything):
    instruction_list = setup(everything)

    head_position = [0,0]
    tail_position = [0,0]

    tail_positions = set()
    tail_positions.add((tail_position[0],tail_position[1]))

    for instruction in instruction_list:
        movements = move_head(head_position,tail_position,instruction)
        head_position = movements['head_pos']
        tail_position = movements['tail_info']['tail_pos']
        tail_positions.update(movements['tail_info']['list_of_coords'])

    print(len(tail_positions))

main(contents)