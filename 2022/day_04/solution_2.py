from solution_1 import which_bigger

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

def is_overlap(which_one, list_of_ranges):
    which = {
        'first_bigger': [1,0],
        'second_bigger': [0,1]
    }
    overlap = list_of_ranges[which[which_one][0]][1] - list_of_ranges[which[which_one][1]][0]
    if overlap > -1:
        return True
    else: return False

def new_contains_range(lower, higher, list_of_lists):
    # if they're different, it's always True
    if lower != higher:
        return True
    # if they're the same and both actual values,
    # pass in one and also the lists
    elif lower and higher:
        return is_overlap(lower, list_of_lists)
    # if they're the same and both False, it's True
    return True

def new_calc_bigger(line):
    lo = which_bigger(line[0][0], line[1][0])
    hi = which_bigger(line[0][1], line[1][1])
    return new_contains_range(lo,hi,line)

def main(lines):
    sum_pairs = 0
    for line in lines:
        # dumb splitting/reformatting
        line_array = line.split(",")
        list_of_lists = []
        for range in line_array:
            nums = range.split("-")
            new_nums = []
            for num in nums:
                new_nums.append(int(num))
            list_of_lists.append(new_nums)
        if new_calc_bigger(list_of_lists):
            sum_pairs += 1
    print(sum_pairs)

main(contents)