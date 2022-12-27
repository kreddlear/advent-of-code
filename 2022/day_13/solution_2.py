from functools import cmp_to_key

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

def test_order(left, right):
    # TLDR: right side always bigger

    # both ints
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return 1
        elif left < right:
            return -1

    # both lists
    elif isinstance(left, list) and isinstance(right, list):
        # we only care about testing the left ones
        for index in range(0,len(left)):
            # if we run out of right-side items before we hit a True
            if index >= len(right):
                return 1
            test_value = test_order(left[index],right[index])
            if test_value == -1:
                return -1
            elif test_value == 1:
                return 1
        # if we've run out of left items without a False
        if len(right) > len(left):
            return -1

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
    packet_list = []
    for line in lines:
        if line:
            packet_list.append(eval(line))
    packet_list.append([[2]])
    packet_list.append([[6]])

    sorted_list = sorted(packet_list, key=cmp_to_key(test_order))
    index_2 = sorted_list.index([[2]])+1
    print(index_2)
    index_6 = sorted_list.index([[6]])+1
    print(index_6)

    print(index_2*index_6)

main(contents)