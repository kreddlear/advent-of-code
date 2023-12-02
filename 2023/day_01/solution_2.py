'''
some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
'''

import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = []
    for line in f.readlines():
        contents.append(line.strip())

num_spellings = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def make_num(digit):
    try:
        return int(digit)
    except:
        return num_spellings[digit]
    
def find_last_with_overlaps(last_match, line):
    start_pos = last_match.start()

    new_line = line[start_pos+1:]

    new_last_match = re.search('\d|one|two|three|four|five|six|seven|eight|nine', new_line)
    if new_last_match != None:
        return find_last_with_overlaps(new_last_match, new_line)
    else:
        return last_match

test_line = 'eightwo'
sum = 0

for content in contents:
    # use regex to get digits
    # return an array of those
    first_raw = re.search('\d|one|two|three|four|five|six|seven|eight|nine', content)
    first = make_num(first_raw.group(0))

    # this doesn't apply to first
    # but for last, the tricky part is
    # "eightwothree" should be "8, 2, 3"
    last_raw = find_last_with_overlaps(first_raw, content)
    last = make_num(last_raw.group(0))

    calibration = first * 10 + last

    sum = sum + calibration

print(sum)
    
