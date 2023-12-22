with open('./input.txt') as f:
    # strip whitespace, put in new array
    lines = [line.strip() for line in f.readlines()]
    
# strip all whitespace out
stripped_time = lines[0].replace(' ','')
stripped_rec = lines[1].replace(' ','')
# i know how long the word "time:" is...
race_time = int(stripped_time[5:])
race_rec = int(stripped_rec[9:])

ways_to_win = 0

# let's just go thru every num
# since my brain is currently fried
for time_to_hold in range(1,race_time): # 1 thru 6
    time_to_float = race_time - time_to_hold
    distance = time_to_float * time_to_hold
    
    if distance > race_rec:
        ways_to_win += 1

print(ways_to_win)