# only add and multiply
# operators are always evaluated left to right

from itertools import combinations

with open('./input.txt') as f:
    lines = [line for line in f.readlines()]

content = []
for line in lines:
    slice = line.index(':')
    solution = int(line[:slice])
    nums = [int(x) for x in line[slice+2:].split()]
    content.append((solution, nums))

def multiply(numbers_list):
    sol = 1
    for num in numbers_list:
        sol *= num
    return sol

def determine_based_on_operator(num1, num2, operator):
    # print("determine function - num1", num1, "num2", num2)
    if operator == '+':
        answer = sum([num1,num2])
    elif operator == '*':
        answer = multiply([num1,num2])
    # print("answer is", answer)
    return answer

can_be_true = []

# content = [(292, [11, 6, 16, 20])]
# test [(3267, [81, 40, 27])]
for solution, nums in content:
    # first try just all a single operator
    if solution == sum(nums):
        can_be_true.append(solution)
        continue
    elif solution == multiply(nums):
        can_be_true.append(solution)
        continue
    else:
        # so we know it needs to be some mix...
        # maybe i need to check how many nums? like even or odd?
        # okay...maybe I just need to generate a list of all possible combinations
        # of operators and then just try them all?
        # how could I get that?
        # so I know the length of the list
        # I know the number of operators has to be 1 less than that
        # so for example, with 3 numbers, I need 2 operators. Those options are:
        # [++], [**], [+*], [*+]
        # Can I use itertools.combinations to generate those?
        # The list would be 2 times the number of operators
        # and the options are either + or *
        solved = False
        num_ops = len(nums) -1
        potential_ops = ['+', '*'] * num_ops
        all_combos = set(combinations(potential_ops, num_ops))
        all_combos.remove(tuple('+') * num_ops)
        all_combos.remove(tuple('*') * num_ops)
        # now I need to try each of those combos
        for combo in all_combos:
            # print("current combo is", combo)
            for i in range(0, len(nums)-1):
                # print("i equals: ", i)
                # print("current relevant num",nums[i])
                # for op in combo:
                op = combo[i]
                # print("current op is",op)
                # treat the first one differently
                if i == 0:
                    result = determine_based_on_operator(nums[0], nums[1], op)
                    if result > solution:
                        # print("giving up, result is already", result)
                        break
                    # print("first step: result is now", result)
                # if we've already gone past the solution, give up
                else:
                    # print("determining", result, nums[i], op)
                    result = determine_based_on_operator(result, nums[i+1], op)
                    if result > solution:
                        # print("giving up, result is already", result)
                        break
                    # print("result is now", result)
                    # treat the last one differently
                    # print("i is now", i, "result is now", result, "solution is", solution, "len is", len(nums)-2)
                    if i == len(nums)-2 and result == solution:
                        # print("we did it!")
                        can_be_true.append(solution)
                        solved = True
                        break
            if solved:
                break

            # print("result",result)

        # for combo in all_combos:
        #     result = 0
        #     for op in combo:
        #         if op == '+':


# print(can_be_true)
print(sum(can_be_true))