with open('./input.txt') as f:
    contents = f.readlines()

def compare_4_chars(string):
    i=0
    while i < len(string):
        list_of_4_chars = []
        # what to add to the index
        j=0
        while j < 4:
            list_of_4_chars.append(string[i+j])
            j += 1
        test_set = set(list_of_4_chars)
        if len(test_set) == 4:
            print(i+4)
            break

        i += 1
    # make the first 4 chars a set
    # check if the set is less than 4 chars
    # if so, move on to the next one
    # if not, break and return those 4 chars

compare_4_chars(contents[0])