# get the left and right lists
with open('./input.txt') as f:
    # strip whitespace, put in new arrays
    left = []
    right = []
    for line in f.readlines():
        split = line.split()
        left.append(int(split[0]))
        right.append(int(split[-1]))

# sort the lists
left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    difference = abs(left[i] - right[i])
    sum += difference

print(sum)