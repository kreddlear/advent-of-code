with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.lower().strip() for line in f.readlines()]

# x (rock) beats c (scissors), draws a (rock), loses to b (paper)
# y (paper) beats a (rock), draws b (paper), loses to c (scissors)
# z (scissors) beats b (paper), draws c (scissors), loses to a (rock)

def choice_points(game):
    expected_index = {
        'x': 0, # lose
        'y': 1, # draw
        'z': 2 # win
    }
    which_index = expected_index[game[2]]
    result_arrays = {
        # they win, draw, lose
        'a': ['scissors', 'rock', 'paper'], # rock
        'b': ['rock', 'paper', 'scissors'], # paper
        'c': ['paper', 'scissors', 'rock'] # scissors
    }
    what_array = result_arrays[game[0]]
    result_choice = what_array[which_index]
    result_meaning = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }
    result_points = result_meaning[result_choice]
    return result_points

def what_score(game):
    # game 'a y' 'b x' etc
    my_dict = {
        'x': 0,
        'y': 3,
        'z': 6
    }
    score = my_dict[game[2]]
    score += choice_points(game)
    return score

def main(games):
    score = 0
    for game in games:
        score += what_score(game)
    print(score)


main(contents)