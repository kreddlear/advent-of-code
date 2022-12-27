with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

def test_order(left, right):
    # TLDR: right side always bigger

    # both ints
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        elif left < right:
            return True

    # both lists
    elif isinstance(left, list) and isinstance(right, list):
        # we only care about testing the left ones
        for index in range(0,len(left)):
            # if we run out of right-side items before we hit a True
            if index >= len(right):
                # print("right list smaller, false")
                return False
            test_value = test_order(left[index],right[index])
            if test_value == True:
                return True
            elif test_value == False:
                return False
        # if we've run out of left items without a False
        if len(right) > len(left):
            return True

    # if left is int and right is list
    elif isinstance(left, int) and isinstance(right, list):
        # wrap it in a list and see what happens
        left = [left]
        return test_order(left, right)

    elif isinstance(left, list) and isinstance(right, int):
        # wrap it in a list and see what happens
        right = [right]
        return test_order(left, right)

def main(lines):
    formatted_pairs = []
    throwaway_list = []
    for line_num in range(0,len(lines),3):
        throwaway_list.append(eval(lines[line_num]))
        throwaway_list.append(eval(lines[line_num+1]))
        formatted_pairs.append(throwaway_list)
        throwaway_list = []

    properly_ordered = set()

    for pair_num in range(0,len(formatted_pairs)):
        result = test_order(formatted_pairs[pair_num][0],formatted_pairs[pair_num][1])
        if result:
            properly_ordered.add(pair_num+1)

    print("final",properly_ordered)
    solution = 0
    for num in properly_ordered:
        solution += num

    print(solution)

main(contents)