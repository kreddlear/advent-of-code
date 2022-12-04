import string

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

def get_score(letter):
    letters = string.ascii_lowercase + string.ascii_uppercase
    score = letters.index(letter)+1
    return score

def main(lines):
    total = 0
    # split every line into two sets
    for line in lines:
        length_divided_by_two = int(len(line)/2)
        first_compartment = set((line[0:length_divided_by_two]))
        second_compartment = set((line[length_divided_by_two:]))
        # now find the common letter
        common = first_compartment.intersection(second_compartment)
        # common is a set so we have to get the value out
        total += get_score(common.pop())
    print(total)

main(contents)