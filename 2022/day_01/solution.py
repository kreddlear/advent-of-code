with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = []
    for line in f.readlines():
        if line.strip() != '':
            contents.append(int(line.strip()))
        else:
            contents.append(line.strip())

# part 1

# define top_three
max_cals = 0
# define current_cals
current_cals = 0
for current_index in range(len(contents)):
    # if it's not an empty string:
    if contents[current_index] != '':
        current_cals += contents[current_index]
    # else if it is an empty string or is the end of the array
    if contents[current_index] == '' or (current_index == len(contents)-1):
        if current_cals > max_cals:
            max_cals = current_cals
        current_cals = 0

print(max_cals)

# part 2

# define top_three
top_three = [0, 0, 0]
# define current_cals
current_cals = 0
for current_index in range(len(contents)):
    # if it's not an empty string:
    if contents[current_index] != '':
        current_cals += contents[current_index]
    # else if it's an empty string or the end of the list
    if (contents[current_index] == '') or (current_index == len(contents)-1):
        top_three.append(current_cals)
        top_three.sort(reverse = True)
        top_three.pop()
        current_cals = 0

print(sum(top_three))