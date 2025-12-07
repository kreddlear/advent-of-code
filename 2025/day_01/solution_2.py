with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    # split the lines into tuples of (direction, distance)
    rotations = []
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        rotations.append((direction, distance))

def add_vs_subtract(position):
    updated = False
    if position < 0:
        updated = True
        return 100 + position, updated
    elif position > 99:
        updated = True
        return position - 100, updated
    else:
        return position, updated

# e.g. dial is pointing at 5 and we move L10, so new_pos is -5
# we should return 95
# and have passed zero once
# e.g. dial is pointing at 95 and we move R5, so new_pos is 100
# we should return 0
# print("returning new_pos - 100", new_pos - 100)
# if the dial is pointing at zero and we moved R100 so new_pos is 100,
# and new_new_pos is 0,
# already_on_zero is True,
# but we should still count it as passing zero once
# R1000 R1050 should end up as 21 total (R1000 = 10, R1050 = 11)

position = 50
times_on_zero = 0
count_zeros = 0

# test_position = 0
# position = test_position
# test_rotations = [('R', 300)]
# rotations = test_rotations

for rotation in rotations:
    count_zeros = 0
    direction = rotation[0]
    raw_distance = rotation[1]
    # ignore multiple rotations for now
    distance = raw_distance % 100
    # print(rotation[0], " ", distance)
    # print("position is", position)
    initial_position = position

    # determine if it ends on zero
    if direction == 'L':
        position, updated = add_vs_subtract(position - distance)
    elif direction == 'R':
        position, updated = add_vs_subtract(position + distance)

    # print("position: ", position)
    # print("updated: ", updated)
    # if the raw distance % 100 is zero, just count the number of times we pass zero
    if distance == 0:
        count_zeros += raw_distance // 100
        times_on_zero += count_zeros
        # print("times on zero: ", times_on_zero)
        continue
    # if we end on zero, count that
    elif position == 0:
        count_zeros += 1
    # if we don't end on zero but we did update
    # (e.g. we moved past zero), we passed zero once
    elif updated and initial_position != 0: 
        count_zeros += 1
    # now handle multiple rotations
    count_zeros += raw_distance // 100
    # print("count zeros: ", count_zeros)
    times_on_zero += count_zeros

print("times on zero: ", times_on_zero)

# answer = 100 // 100
# mod_answer = 100 % 100
# print(answer, mod_answer)