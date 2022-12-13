from solution_1_reworked import move_head, move_tail

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.lower().strip() for line in f.readlines()]

def main(lines):

    head_position = [0,0]

    # create list of tail pos all 0,0
    tail_position_list = []
    for i in range(0,9):
        tail_position_list.append([0,0])

    tail_positions = set()
    tail_positions.add((tail_position_list[0][0],tail_position_list[0][1]))

    for line in lines:
        direction = line.split()[0]
        num_movement = int(line.split()[1])

        # for every space in a direction
        for num in range(0,num_movement):
            # move the head there
            head_position = move_head(head_position,direction)
            updateable_head_pos = head_position

            # check all but the last one of the tail position list
            for tail_coord in range(0,len(tail_position_list)-1):
                tail_coord = move_tail(tail_position_list[tail_coord], updateable_head_pos)
                updateable_head_pos = tail_coord

            # for the last one, actually get the coords
            final_tail_info = move_tail(tail_position_list[-1], updateable_head_pos)
            tail_positions.add((final_tail_info[0],final_tail_info[1]))

    # print(tail_position_list)

    # print(tail_positions)

    print(len(tail_positions))

main(contents)