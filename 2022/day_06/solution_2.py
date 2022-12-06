with open('./input.txt') as f:
    contents = f.readlines()

def compare_14_chars(string):
    i=0
    while i < len(string):
        list_of_14_chars = []
        # what to add to the index
        j=0
        while j < 14:
            list_of_14_chars.append(string[i+j])
            j += 1
        test_set = set(list_of_14_chars)
        if len(test_set) == 14:
            print(i+14)
            break

        i += 1

compare_14_chars(contents[0])