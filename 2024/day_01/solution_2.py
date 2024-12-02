# similarity score
with open('./input.txt') as f:
    # strip whitespace, put in new arrays
    left = []
    right = []
    for line in f.readlines():
        split = line.split()
        left.append(int(split[0]))
        right.append(int(split[-1]))

similarity_score = 0

# store counted nums
# so I don't have to recount numbers if I've seen them before
counted_nums = {}
# loop through each number in left
for num in left:
    # if it's not in counted_nums
    if num not in counted_nums:
        # count how many times it appears in right list
        right_count = right.count(num)
        # add to list
        counted_nums[num] = right_count
    else:
        # if it is in counted_nums, use the count
        right_count = counted_nums[num]
    # add to similarity score: num * count
    similarity_score = similarity_score + (num * right_count)

print(similarity_score)