from solution_1 import get_score

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [set((line.strip())) for line in f.readlines()]

def compare_three_sets(list_of_sets):
    common_first = list_of_sets[0].intersection(list_of_sets[1])
    common = common_first.intersection(list_of_sets[2])
    return common

def main(lines):
    total = 0
    x=0
    while x < len(lines):
        current_elf = [lines[x], lines[x+1], lines[x+2]]
        common = compare_three_sets(current_elf)
        for letter in common:
            total += get_score(letter)
        x += 3

    print(total)

main(contents)