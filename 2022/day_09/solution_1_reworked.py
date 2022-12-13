with open('./input_test.txt') as f:
    # strip whitespace, put in new array
    contents = [line.lower().strip() for line in f.readlines()]

# okay what if we check one at a time, every time head moves
# that should simplify things
# and also not depend on each other
def move_tail(tail,head,testing=False):
    # return a set of places tail has visited and a new tail pos
    x_delta = head[0] - tail[0]
    abs_x = abs(x_delta)
    y_delta = head[1] - tail[1]
    abs_y = abs(y_delta)
    if testing:
        print("---------")
        print("x delta:",x_delta)
        print("abs x:",abs_x)
        print("y delta:",y_delta)
        print("abs y:",abs_y)

    # no movement, return immediately
    if abs_x <= 1 and abs_y <= 1:
        if testing:
            print("no movement")
        return tail

    # need to move up or down
    # if same row (abs_x == 0) but diff col (abs_y > 1)
    if not abs_x and abs_y > 1:
        if testing:
            print("moving up or down")
        # if positive, increase tail[y]
        # i.e. head at 0,2 tail at 0,0 => tail at 0,1
        if y_delta > 0:
            tail[1] += 1
        # if negative, decrease tail[y]
        # i.e. head at 0,0 tail at 0,2 => tail at 0,1
        elif y_delta < 0:
            tail[1] -= 1

    # need to move left or right
    elif not abs_y and abs_x > 1:
        if testing:
            print("moving left or right")
        # if positive, increase tail[y]
        # i.e. head at 0,2 tail at 0,0 => tail at 0,1
        if x_delta > 0:
            tail[0] += 1
        # if negative, decrease tail[y]
        # i.e. head at 0,0 tail at 0,2 => tail at 0,1
        if x_delta < 0:
            tail[0] -= 1

    # need to move diagonally
    # works because above cases will catch others
    elif abs_x > 1 or abs_y > 1:
        if testing:
            print("moving diagonally")
        if x_delta > 0:
            tail[0] += 1
        elif x_delta < 0:
            tail[0] -= 1
        if y_delta > 0:
            tail[1] += 1
        elif y_delta < 0:
            tail[1] -= 1

    if testing:
        print("new tail:",tail)
    return tail

# head at 0,2 tail at 0,0 -> new_tail should be at 0,1
test_tail_pos = [4,3]
test_head_pos = [0,2]
# move_tail(test_tail_pos,test_head_pos)

def move_head(head, direction):
    if direction == 'r':
        head[0] += 1
    elif direction == 'l':
        head[0] -= 1
    elif direction == 'u':
        head[1] += 1
    elif direction == 'd':
        head[1] -= 1
    return head

test_instruction = [0,-3]
# move_head([4,0],[0,0],test_instruction)

def main(lines):

    head_position = [0,0]
    tail_position = [0,0]

    tail_positions = set()
    tail_positions.add((tail_position[0],tail_position[1]))

    for line in lines:
        direction = line.split()[0]
        num_movement = line.split()[1]

        for num in num_movement:
            move_head(head_position,direction)


        movements = move_head(head_position,tail_position)
        head_position = movements['head_pos']
        tail_position = movements['tail_info']['tail_pos']
        tail_positions.update(movements['tail_info']['list_of_coords'])

    print(len(tail_positions))

# main(contents)