with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

# count "cycles"
# x starts at 1
# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

def check_cycle(cycle,row):
    if cycle % 40 == 0:
        print(row)
        return 0, ''
    else:
        return cycle, row

def draw_pixel(cycle,sprite_loc,row):
    if cycle in sprite_loc:
        row += '#'
    else:
        row += '.'
    return row

def main(lines):
    x = 1
    cycle_num = 0

    crt_row = ''

    for line in lines:
        sprite = [x-1,x,x+1]
        crt_row = draw_pixel(cycle_num,sprite,crt_row)
        if line == 'noop':
            cycle_num += 1
            cycle_num, crt_row = check_cycle(cycle_num,crt_row)
        else:
            cycle_num += 1
            cycle_num, crt_row = check_cycle(cycle_num,crt_row)
            crt_row = draw_pixel(cycle_num,sprite,crt_row)
            cycle_num += 1
            cycle_num, crt_row = check_cycle(cycle_num,crt_row)
            num = int(line.split()[1])
            x += num

main(contents)