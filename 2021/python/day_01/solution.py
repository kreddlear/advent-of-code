# count the number of times a depth measurement increases from the previous measurement

# import file
# assume it'll always be run from the day_00 directory
with open('./input_test.txt') as f:
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

# part 2

def is_increasing_sums(depths):
    previous_depth_sum = sum(depths[:3])
    print(previous_depth_sum)
    increases = 0
    print(enumerate(depths))
    for index, depth in enumerate(depths):
        print(index, depth)
        if depth > previous_depth_sum:
            increases += 1
            # print("increases" + str(increases))
        previous_depth_sum = depth
    return increases

print(is_increasing_sums(contents))
