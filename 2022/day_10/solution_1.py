with open('./input_test_large.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

# count "cycles"
# x starts at 1
# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

# signal strength = the cycle number * value of the X register
# during the 20th cycle and every 40 cycles after that
# (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles)

def check_cycle(cycle):
    if cycle % 40 == 20:
        return True
    else:
        return False

def main(lines):
    x = 1
    cycle_num = 0

    signal_strength_sum = 0

    for line in lines:
        if line == 'noop':
            cycle_num += 1
            if check_cycle(cycle_num):
                signal_strength = cycle_num * x
                signal_strength_sum += signal_strength
        else:
            num = int(line.split()[1])
            cycle_num += 1
            if check_cycle(cycle_num):
                signal_strength = cycle_num * x
                signal_strength_sum += signal_strength
            cycle_num += 1
            if check_cycle(cycle_num):
                signal_strength = cycle_num * x
                signal_strength_sum += signal_strength
            x += num

    # print("final x",x)
    # print("final cycle",cycle_num)
    print(signal_strength_sum)

main(contents)