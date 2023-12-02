'''
On each line, the calibration value can be found by combining 
the first digit and the last digit (in that order) to form a single two-digit number.

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
Adding these together produces 142.

Consider your entire calibration document. 
What is the sum of all of the calibration values?
'''

import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = []
    for line in f.readlines():
        contents.append(line.strip())

# day 1

test_line = 'treb7uchet'
sum = 0

for content in contents:
    # use regex to get digits
    # return an array of those
    digits = re.findall('\d', content)

    # take first and last index
    # (to get around if there's only one digit)
    # and make that an int
    calibration = int(f'{digits[0]}{digits[-1]}')
    # add to sum
    sum = sum + calibration

print(sum)
    
