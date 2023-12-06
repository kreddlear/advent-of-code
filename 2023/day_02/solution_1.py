'''
In game 1, three sets of cubes are revealed from the bag (and then put back again).
The first set is 3 blue cubes and 4 red cubes; 
the second set is 1 red cube, 2 green cubes, and 6 blue cubes; 
the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible 
if the bag had been loaded with that configuration. 
However, game 3 would have been impossible 
because at one point the Elf showed you 20 red cubes at once; 
similarly, game 4 would also have been impossible 
because the Elf showed you 15 blue cubes at once. 

If you add up the IDs of the games that would have been possible, you get 8.
'''

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = []
    for line in f.readlines():
        contents.append(line.strip())

bag_contents = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# possible_games = []
possible_games_sum = 0

test_line = 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'

for content in contents:

    # PARSING

    game_str, results_str = content.split(':')

    # get game num
    game_num = int(game_str.split(' ')[-1])

    # split results into handfuls
    results_handfuls = results_str.split(';')
    # print(results_handfuls)

    # start by assuming game is possible
    game_possible = True

    # split handfuls into colors
    for handful in results_handfuls:
        colors_array = handful.split(',')
        # print(colors_array)
        handful_possible = True
        # split colors into num and color
        for color in colors_array:
            num, color = color.lstrip().split(' ')

            # i could return it
            # so this parsing thing can be its own function
            # but also i don't neeeeed to
            # and then i could check each color separately

            # CHECK POSSIBILITY
            # if it's impossible,
            # set possible to False
            # and stop checking colors
            if int(num) > bag_contents[color]:
                handful_possible = False
                break
            # if it's still possible, keep checking
            # do i even need an else? guess not
            # else:

        # if we're here and possible is False,
        # don't bother checking other handfuls
        if not handful_possible:
            game_possible = False
            break

    if game_possible:
        possible_games_sum += game_num

# print(possible_games)
print(possible_games_sum)

# some things to remember
# as soon as i know one color is impossible,
# i can ditch the whole game
# (don't have to check every color)