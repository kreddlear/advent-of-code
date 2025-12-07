with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    # split the lines into tuples of (direction, distance)
    rotations = []
    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        rotations.append((direction, distance))

# note: we need recursion here if we have something like R500
def add_vs_subtract(new_pos):
    if new_pos < 0:
        # e.g. dial is pointing at 5 and we move L10, so new_pos is -5
        # we should return 95
        print("returning 100 + new_pos", 100 + new_pos)
        return add_vs_subtract(100 + new_pos)
    elif new_pos > 99:
        # e.g. dial is pointing at 95 and we move R5, so new_pos is 100
        # we should return 0
        print("returning new_pos - 100", new_pos - 100)
        return add_vs_subtract(new_pos - 100)
    else:
        # print("returning new_pos", new_pos)
        return new_pos

position = 50
count_zeros = 0

test_position = 0
position = test_position
test_rotations = [('R', 200)]
rotations = test_rotations

for rotation in rotations:
    direction = rotation[0]
    distance = rotation[1]
    # print(rotation)
    if direction == 'L':
        position = add_vs_subtract(position - distance)
    elif direction == 'R':
        position = add_vs_subtract(position + distance)
    print(position)
    if position == 0:
        count_zeros += 1

print(count_zeros)