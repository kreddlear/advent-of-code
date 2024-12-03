'''
It seems like the goal of the program is just to multiply some numbers. 
It does that with instructions like mul(X,Y), 
where X and Y are each 1-3 digit numbers. 
For instance, mul(44,46) multiplies 44 by 46 to get 
a result of 2024. 
Similarly, mul(123,4) would multiply 123 by 4.
However, there are also many invalid characters that should be ignored, 
even if they look like part of a mul instruction. 
Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

Only the four highlighted sections are real mul instructions. 
Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. 
What do you get if you add up all of the results of the multiplications?
'''

import re

with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

sum_mults = 0

for line in lines:
    # get matches, with the numbers each in a group
    valid_instructions = re.finditer(r'mul\((\d+),(\d+)\)', line)

    # loop through matches and multiply the numbers
    for instruction in valid_instructions:
        first_num = int(instruction.group(1))
        second_num = int(instruction.group(2))
        sum_mults += first_num*second_num

print(sum_mults)
