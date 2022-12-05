from re import findall, finditer

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line for line in f.readlines()]

def split_structure_and_instructions(lines):
    split = lines.index('\n')
    cols_list = lines[0:split]
    instructions = lines[split+1:]
    return {
        "columns": cols_list,
        "instructions": instructions
    }

def set_up_columns(rows, num_columns):
    # set up tracking for the number of columns there will be
    column_map = {}
    for num in range(0,num_columns):
        column_map[num] = []

    # now iterate through rows and start adding crates to each column
    for row in rows:
        all_crate_indices = [i.start() for i in finditer(r'\[', row)]
        for index in all_crate_indices:
            # now get crate letter using the index
            crate = row[index+1]
            # now put the crate letter in the proper column
            column_num = int(index/4)
            column_map[column_num].append(crate)

    return column_map

def parse_instruction(instruction_string):
    nums_in_instruction = findall(r'[0-9]+', instruction_string)
    return [int(num) for num in nums_in_instruction]

def setup(chunk_of_text):
    split_format = split_structure_and_instructions(chunk_of_text)
    # get num_columns because we'll need it at the end
    num_columns = int(split_format['columns'][-1].strip()[-1])
    # get current structure
    structure = set_up_columns(split_format['columns'], num_columns)
    # get list of instructions
    instruction_list = [parse_instruction(instruction) for instruction in split_format['instructions']]

    return {
        'structure': structure,
        'parsed_instructions': instruction_list,
        'num_cols': num_columns
    }

def move_crates(structure, instruction_nums):
    num_crates = instruction_nums[0]
    origin = instruction_nums[1]-1
    destination = instruction_nums[2]-1

    # add loop to loop as many times as num_crates
    crate = 0
    while crate < num_crates:
        # pop from origin
        crate_to_move = structure[origin].pop(0)
        # insert in destination
        structure[destination].insert(0,crate_to_move)
        # print to confirm
        crate += 1

    return structure

def main(everything):
    input = setup(everything)
    num_columns = input['num_cols']
    structure = input['structure']
    # iterate through instructions
    for instruction_nums in input['parsed_instructions']:
        # set structure to result of moving crates
        structure = move_crates(structure, instruction_nums)

    # now get the answer: the first/top crate of each column
    answer = ''.join(structure[col][0] for col in range(0,num_columns))
    return answer

print(main(contents))





