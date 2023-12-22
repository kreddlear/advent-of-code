import re

with open('./input.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]

# Holding down the button charges the boat, 
# and releasing the button allows the boat to move. 

# Boats move faster if their button was held longer, 
# but time spent holding the button counts against the total race time.
    
# Your boat has a starting speed of zero millimeters per millisecond.
# For each whole millisecond you spend at the beginning of the race holding down the button,
# the boat's speed increases by one millimeter per millisecond.

time_nums = re.findall('\d+', lines[0])
record_nums = re.findall('\d+', lines[1])

ways_to_win_mult = 1

for race in range(0,len(time_nums)):

    race_time = int(time_nums[race])
    race_rec = int(record_nums[race])

    # so do i want to start from the beginning and go thru every num?
    # or start from the end and work backwards
    # maybe both? start from the beginning and then once i find that lowest
    # then start from the end

    ways_to_win = 0

    # let's just go thru every num
    # since my brain is currently fried
    for time_to_hold in range(1,race_time): # 1 thru 6
        # print(time_to_hold)
        time_to_float = race_time - time_to_hold
        distance = time_to_float * time_to_hold
        
        if distance > race_rec:
            ways_to_win += 1

    # then calc the delta of the range??
    ways_to_win_mult = ways_to_win_mult * ways_to_win

print(ways_to_win_mult)