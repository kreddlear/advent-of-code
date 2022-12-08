with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

def check_row(row, row_num, row_len):
    new_vis_list = set()
    # left to right
    current = row[0]
    for index in range(0,row_len):
        num_to_check = row[index]
        if num_to_check > current:
            new_vis_list.add((index,row_num))
            current = num_to_check

    # right to left
    current = row[-1]
    for index in range(row_len-1,0,-1):
        num_to_check = row[index]
        if num_to_check > current:
            new_vis_list.add((index,row_num))
            current = num_to_check

    return new_vis_list

def check_col(grid, col_num, col_len):
    new_vis_list = set()
    # top to bottom
    current = grid[0][col_num]
    for row in range(0,col_len):
        num_to_check = grid[row][col_num]
        if num_to_check > current:
            new_vis_list.add((col_num,row))
            current = num_to_check

    # bottom to top
    current = grid[col_len-1][col_num]
    for row in range(col_len-1,0,-1):
        num_to_check = grid[row][col_num]
        if num_to_check > current:
            new_vis_list.add((col_num,row))
            current = num_to_check

    return new_vis_list

def main(everything):
    list_of_vis = set()

    width = int(len(everything[0]))
    height = int(len(everything))

    # iterate over chars in each row
    for row in range(0,height):
        # add edges to set
        list_of_vis.add((0,row))
        list_of_vis.add((height-1,row))

        row_check_list = check_row(everything[row], row, width)
        list_of_vis.update(row_check_list)

    for col in range(0,width):
        # add edges to set
        list_of_vis.add((col,0))
        list_of_vis.add((col,width-1))

        # iterate over rows
        col_check_list = check_col(everything, col, height)
        list_of_vis.update(col_check_list)

    # print(sorted(list_of_vis))

    print(len(list_of_vis))

main(contents)