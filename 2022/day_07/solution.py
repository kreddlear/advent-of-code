with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.dirs = {}

    @property
    def final_sizes(self):
        total = sum(self.files.values())
        for dir in self.dirs.values():
            total += dir.final_sizes
        return total

def initial_map_setup(list_of_lines):
    filemap_output = []
    # start with /
    current_directory = Dir('root', None)
    filemap_output.append(current_directory)

    for line in list_of_lines:
        # it's just always useful to split it
        line_list = line.split()
        # ignore the first one
        if line == '$ cd /': continue
        # if it's a command
        elif line_list[0] == '$':
            # if it's a cd
            if line_list[1] == 'cd':
                if line_list[-1] == '..':
                    current_directory = current_directory.parent
                else:
                    # update current directory to one inside it
                    current_directory = current_directory.dirs[line_list[-1]]
            elif line_list[1] == 'ls':
                continue
        # if it's a dir
        elif line_list[0] == 'dir':
            # create a dir with that dir name and its parent
            new_dir = Dir(line_list[1], current_directory)
            # add it to the dirs of current_directory
            current_directory.dirs[new_dir.name] = new_dir
            # add it to the list
            filemap_output.append(new_dir)
        # if we get here, it's a file
        else:
            current_directory.files[line_list[1]] = int(line_list[0])
    return filemap_output

def main(lines):
    map_dict = initial_map_setup(lines)
    solution = 0
    for item in map_dict:
        if item.final_sizes <= 100000:
            solution += item.final_sizes
    print(solution)

main(contents)
