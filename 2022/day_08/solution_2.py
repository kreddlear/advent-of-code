with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

# thoughts
# if one of the directions is zero aka on the edge, don't even bother finding the other directions
# if a tree has a tall tree next to it, its viewing distance there is not zero, but one

def count_right(row, col_num, row_len):
    # print("checking right with",row,col_num)
    current = row[col_num]
    # print("current",current)
    size = 0
    for index in range(col_num+1,row_len):
        num_to_check = row[index]
        size += 1
        if num_to_check >= current:
            break
        # don't think i need an else here...
    return size

# shouldn't i be able to combine the above with a "direction" param or something?
def count_left(row, col_num):
    # print("checking left")
    current = row[col_num]
    # print("current",current)
    size = 0
    for index in range(col_num-1,-1,-1):
        num_to_check = row[index]
        # print("checking", num_to_check,"at index",index)
        size += 1
        if num_to_check >= current:
            break
    return size

test_row = '33549'
test_col_num = 2
# count_right(test_row, test_col_num, len(test_row))
# count_left(test_row, test_col_num, len(test_row))

def count_up(grid, col_num, row_num):
    # print("checking up")
    current = grid[row_num][col_num]
    # print("current",current)
    size = 0
    for row in range(row_num-1,-1,-1):
        # check the next row up, same column/index
        num_to_check = grid[row][col_num]
        # print("checking", num_to_check,"at row",row)
        size += 1
        if num_to_check >= current:
            break
    return size

def count_down(grid, col_num, row_num, col_len):
    # print("checking down")
    current = grid[row_num][col_num]
    # print("current",current)
    size = 0
    for row in range(row_num+1,col_len):
        # check the next row down, same column/index
        num_to_check = grid[row][col_num]
        # print("checking", num_to_check)
        size += 1
        if num_to_check >= current:
            break
    return size

# count_up(contents, 2, 3, len(contents))
# count_down(contents, 2, 1, len(contents))

def main(everything):
    # this should be optimized so that if a new size is found that's bigger, it just replaces this one
    # but for now i want to see all of them
    biggest_size = 0

    width = int(len(everything[0]))
    height = int(len(everything))

    # iterate over chars in each row
    for row in range(1,height):
        for col in range(1,width):
            size = 1
            size *= count_right(everything[row],col,width)
            if size != 0:
                size *= count_left(everything[row],col)
            if size != 0:
                size *= count_up(everything,col,row)
            if size != 0:
                size *= count_down(everything,col,row,height)

            if size > biggest_size:
                biggest_size = size

    print(biggest_size)


main(contents)