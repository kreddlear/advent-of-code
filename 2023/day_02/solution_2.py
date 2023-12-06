'''
In each game you played, 
what is the fewest number of cubes of each color
that could have been in the bag to make the game possible?

In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48.
In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
'''

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = []
    for line in f.readlines():
        contents.append(line.strip())

test_line = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

power_sum = 0

for content in contents:

    power = 1

    minimum_bag_contents = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    # PARSING

    # game_str, results_str = test_line.split(':')
    game_str, results_str = content.split(':')

    # get game num
    game_num = int(game_str.split(' ')[-1])

    # split results into handfuls
    results_handfuls = results_str.split(';')
    # print(results_handfuls)

    # split handfuls into colors
    for handful in results_handfuls:
        colors_array = handful.split(',')
        # print(colors_array)
        handful_possible = True
        # split colors into num and color
        for color in colors_array:
            num, color = color.lstrip().split(' ')

            # if the num is greater than the num in the minimum bag contents,
            # increase that number
            if minimum_bag_contents[color] < int(num):
                minimum_bag_contents[color] = int(num)

            # otherwise we don't care,
            # BUT we still have to check every thing in every handful
            # because i'm too lazy to check the numbers or be smarter about it

    # print(minimum_bag_contents)
    for color in minimum_bag_contents:
        power = power * minimum_bag_contents[color]
    # print(power)
    power_sum += power

print(power_sum)

# some things to remember
# as soon as i know one color is impossible,
# i can ditch the whole game
# (don't have to check every color)