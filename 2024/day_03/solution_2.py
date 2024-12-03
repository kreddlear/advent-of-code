'''
There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. 
At the beginning of the program, mul instructions are enabled.
'''

import re

with open('./input.txt') as f:
    text = f.read()

sum_mults = 0

valid_instructions = re.finditer(r'mul\((\d+),(\d+)\)', text)
do_instructions = re.finditer(r'do\(\)', text)
dont_instructions = re.finditer(r"don\'t\(\)", text)

all_instructions = {}
for instruction in valid_instructions:
    all_instructions[instruction.start()] = (int(instruction.group(1)), int(instruction.group(2)))
for do in do_instructions:
    all_instructions[do.start()] = True
for dont in dont_instructions:
    all_instructions[dont.start()] = False
# print(all_instructions)

sum_mults = 0

all_instructions_list = sorted(all_instructions.keys())
do_mult = True
for instruction in all_instructions_list:
    what_do = all_instructions[instruction]
    if type(what_do) == tuple and do_mult:
        # print("multiplying", what_do)
        first_num = what_do[0]
        second_num = what_do[1]
        sum_mults += first_num*second_num
    elif type(what_do) == bool:
        do_mult = what_do
        # print("setting do_mult to", do_mult)
    # else:
        # print("not multiplying", what_do)

print(sum_mults)

# got 23898018 and that is too low
# do I need to maintain the state between lines? 
# should i be using f.read() instead of f.readlines()?
# yes that was it!