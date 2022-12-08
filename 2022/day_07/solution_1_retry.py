with open('./input_test.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

# if you see $ cd that's the current directory name
# if you see ls, start iterating till there's another $ cd

# do we even care if there's a `dir`?
# yes i think we do because that tells us what to add up

def add_dir_size_and_remove(list_of_dirs, final_sizes):
    # this should return a list of dirs with one/more removed, and a size to add
    size_sum = 0
    for dir in list_of_dirs:
        if dir in final_sizes:
            size_to_add = final_sizes.get(dir)
            size_sum += size_to_add
            list_of_dirs.remove(dir)
    return {
        'new_list': list_of_dirs,
        'size_sum': size_sum
    }

def find_empty_dirs(initial_map, final_sizes):
    for key, value in initial_map.items():
        if len(value['contents_dirs']) == 0:
            final_sizes[key] = value['size']
        else:
            new_dir_info = add_dir_size_and_remove(value['contents_dirs'], final_sizes)
            value['contents_dirs'] = new_dir_info['new_list']
            value['size'] += new_dir_info['size_sum']
    return {
        'new_map': initial_map,
        'new_final_sizes': final_sizes
    }

def initial_map_setup(list_of_lines):
    filemap_output = {}
    for line in list_of_lines:
        # it's just always useful to split it
        line_list = line.split()
        # if it's a command
        if line_list[0] == '$':
            # if it's a cd
            if line_list[1] == 'cd':
                if line_list[-1] == '..':
                    # TODO
                    pass
                else:
                    # add that dir name to the filemap
                    current_directory = line_list[-1]
                    filemap_output[current_directory] = {}
                    filemap_output[current_directory]['size'] = 0
                    filemap_output[current_directory]['contents_dirs'] = []
                    filemap_output[current_directory]['contents_files'] = []
            # if it's ls
            elif line_list[1] == 'ls':
                # i think this is important because it tells us what we need to add up??
                # TODO
                pass
        # if it's a dir
        elif line_list[0] == 'dir':
            # TODO
            filemap_output[current_directory]['contents_dirs'].append(line_list[1])
        # if we get here, it's a file
        else:
            filemap_output[current_directory]['contents_files'].append(line_list[1])
            filemap_output[current_directory]['size'] += int(line_list[0])
            # we gotta clear the list of contents at some point...
    return filemap_output

def main(lines):
    map_dict = initial_map_setup(lines)
    print(map_dict)
    # map_dict = {'d': {'size': 24933642, 'contents_dirs': [], 'contents_files': ['j', 'd.log', 'd.ext', 'k']}}
    final_sizes = {}
    while map_dict.keys() != final_sizes.keys():
        new_info = find_empty_dirs(map_dict, final_sizes)
        map_dict = new_info['new_map']
        final_sizes = new_info['new_final_sizes']

    solution_list = []
    for value in final_sizes.values():
        if value <= 100000:
            solution_list.append(value)
    print(solution_list)

main(contents)