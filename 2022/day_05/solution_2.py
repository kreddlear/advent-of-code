from solution_1 import setup

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line for line in f.readlines()]

def new_move_crates(structure, instruction_nums):
    num_crates = instruction_nums[0]
    origin = instruction_nums[1]-1
    destination = instruction_nums[2]-1

    # get list of crates
    crates_to_move = structure[origin][:num_crates]
    # also manually remove them from origin
    crate = 0
    while crate < num_crates:
        structure[origin].pop(0)
        crate += 1
    # insert in destination
    structure[destination] = crates_to_move + structure[destination]

    return structure

def main(everything):
    input = setup(everything)
    num_columns = input['num_cols']
    structure = input['structure']
    # iterate through instructions
    for instruction_nums in input['parsed_instructions']:
        # set structure to result of moving crates
        structure = new_move_crates(structure, instruction_nums)

    # now get the answer: the first/top crate of each column
    answer = ''.join(structure[col][0] for col in range(0,num_columns))
    return answer

print(main(contents))