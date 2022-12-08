from solution_1 import initial_map_setup

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

# "the total size of the outermost directory (and thus the total amount of used space) is 48381165
# this means the size of the unused space must currently be 21618835"
# 70000000 minus 48381165 = 21618835
# "which isn't quite the 30000000 required by the update.
# Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run."
# 30000000 - 21618835 = 8381165

def main(lines):
    filemap_list = initial_map_setup(lines)

    total_space = 70000000
    min_unused = 30000000

    # get the size of the biggest dir (root)
    for item in filemap_list:
        if item.name == 'root':
            biggest_dir = item.final_sizes

    currently_unused = total_space - biggest_dir
    remaining_to_delete = min_unused - currently_unused

    possible_to_delete = []
    for item in filemap_list:
        if item.final_sizes > remaining_to_delete:
            possible_to_delete.append(item.final_sizes)
    print(min(possible_to_delete))

main(contents)