import re

with open('./input_test.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]

# get seeds first since that's unique and easy
seeds_raw = lines[0][7:]
seeds = seeds_raw.split(' ')

# now let's go through and split up each section
sections = []
for line_num, line in enumerate(lines[2:]):
    if ':' in line:
        