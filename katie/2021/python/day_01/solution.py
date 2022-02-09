# count the number of times a depth measurement increases from the previous measurement

# import file
with open('./input.txt') as f:
    # strip whitespace and turn to ints, put in new array
    contents = [int(line) for line in f.readlines()]

# print(contents)

# part 1

def is_increasing(depths):
    previous_depth = depths[0]
    increases = 0
    for depth in depths:
        # print(depth)
        if depth > previous_depth:
            increases += 1
            # print("increases" + str(increases))
        previous_depth = depth
    return increases

print(is_increasing(contents))
