with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.lower().strip() for line in f.readlines()]

# x (rock) beats c (scissors), draws a (rock), loses to b (paper)
# y (paper) beats a (rock), draws b (paper), loses to c (scissors)
# z (scissors) beats b (paper), draws c (scissors), loses to a (rock)

# need to figure out:
# 1) if you won
# 2) what your score was
def who_won(game):
    result_arrays = {
        # win, draw, lose
        'x': ['c', 'a', 'b'],
        'y': ['a', 'b', 'c'],
        'z': ['b', 'c', 'a']
    }
    which_order = result_arrays[game[2]]
    what_result = which_order.index(game[0])
    result_meaning = {
        0: 6,
        1: 3,
        2: 0
    }
    return result_meaning[what_result]
    # figure out what the result was

def what_score(game):
    # game 'a y' 'b x' etc
    my_dict = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    score = my_dict[game[2]]
    score += who_won(game)
    return score

def main(games):
    score = 0
    for game in games:
        score += what_score(game)
    print(score)


main(contents)

# and then also keep track of all of that