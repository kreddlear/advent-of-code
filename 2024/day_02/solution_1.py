'''
The unusual data (your puzzle input) consists of many reports, 
one report per line. Each report is a list of numbers called 
levels that are separated by spaces.
The engineers are trying to figure out which reports are safe.
The Red-Nosed reactor safety systems can only tolerate levels that
are either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
'''

# so could I first sort the line one way and then another, 
# and see if either matches the original?
# and then if so, then check if the difference between adjacent numbers is 1, 2, or 3?

with open('./input.txt') as f:
    # lines = [line.strip() for line in f.readlines()]
    contents = []
    for line in f.readlines():
        line_nums = [int(num) for num in line.split()]
        contents.append(line_nums)

def incr_or_decr_2(report):
    # just check the first 2 nums
    reverse = False
    if report[0] > report[1]:
        reverse = True
    sorted_list = sorted(report, reverse=reverse)
    if report == sorted_list:
        return True
    else:
        # print('not safe', report)
        return False

def adjacent_check(line):
    passed = False
    distances = []
    for index in range(len(line)-1):
        current_num = line[index]
        next_num = line[index+1]
        distances.append(abs(current_num - next_num))

    if max(distances) <= 3 and min(distances) > 0:  # between 1 and 3 inclusive
        passed = True

    return passed

def check(line):
    first_pass = incr_or_decr_2(line)
    second_pass = adjacent_check(line)
    return first_pass and second_pass

def main(contents):
    num_safe = 0
    for line in contents:
        if check(line):
            num_safe += 1

    print(num_safe)

main(contents)