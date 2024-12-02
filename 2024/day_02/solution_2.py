'''
tolerate a single bad level
'''

# so could I first sort the line one way and then another, 
# and see if either matches the original?
# and then if so, then check if the difference between adjacent numbers is 1, 2, or 3?

from solution_1 import incr_or_decr_2

with open('./input.txt') as f:
    # lines = [line.strip() for line in f.readlines()]
    contents = []
    for line in f.readlines():
        line_nums = [int(num) for num in line.split()]
        contents.append(line_nums)

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
    unsafe_reports = []
    for line in contents:
        # print('-------')
        # print('checking', line)
        if check(line):
            # print('safe: ', line)
            num_safe += 1
        else:
            # print('unsafe, rechecking: ', line)
            passed = False
            for index in range(len(line)):
                copy_report_pop = list(line)
                copy_report_pop.pop(index)

                if check(copy_report_pop):
                    num_safe += 1
                    passed = True
                    break  # don't bother continuing to check
            if passed == False:
                unsafe_reports.append(line)

    print(num_safe)

main(contents)

# got messed up because at first I used `copy_report.remove(copy_report[index])`, which removed the first
# instance of an item - so in a line like: [51, 53, 56, 57, 59, 56, 57, 60]
# where it was supposed to be testing removing index 5, 56, it instead
# removed index 2, 56. so I missed 6 lines that were safe.
# switching to using `copy_report.pop(index)` worked properly.