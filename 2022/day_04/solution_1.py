with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

def which_bigger(x, y):
    if x > y:
        return "first_bigger"
    elif y > x:
        return "second_bigger"
    else:
        # if they're equal, return that
        return False

def contains_range(lower, higher):
    # if they're different, it's always True
    if lower != higher:
        return True
    # if they're the same and both actual values, False
    elif lower and higher:
        return False
    # if they're the same and both False, it's True
    return True

def calc_bigger(list):
    lo = which_bigger(list[0][0], list[1][0])
    hi = which_bigger(list[0][1], list[1][1])

    contains_range(lo,hi)

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
        if calc_bigger(list_of_lists):
            sum_pairs += 1
    print(sum_pairs)

main(contents)