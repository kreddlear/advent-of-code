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

# this isn't actually necessary; it performs fine just counting every time!
# counted_nums = {}
# for num in left:
#     if num not in counted_nums:
#         right_count = right.count(num)
#         counted_nums[num] = right_count
#     else:
#         right_count = counted_nums[num]
#     similarity_score = similarity_score + (num * right_count)

for num in left:
    right_count = right.count(num)
    similarity_score = similarity_score + (num * right_count)

print(similarity_score)