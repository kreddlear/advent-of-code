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
        print("checking cycle...it's",cycle)
        return True
    else:
        return False

def main(lines):
    x = 1
    cycle_num = 0

    signal_strength_sum = 0

    for line in lines:
        print("-------------")
        print("starting line:",line)
        print("x equals:",x)
        if line == 'noop':
            print("cycle",cycle_num,"complete")
            cycle_num += 1
            print("starting cycle",cycle_num)
            print("noop")
            if check_cycle(cycle_num):
                print("it's 20!",x)
                signal_strength = cycle_num * x
                signal_strength_sum += signal_strength
                print(signal_strength)
            print("cycle",cycle_num,"complete")
        else:
            num = int(line.split()[1])
            print("cycle",cycle_num,"complete")
            cycle_num += 1
            print("starting cycle",cycle_num)
            if check_cycle(cycle_num):
                print("it's in the middle!!!",x)
                signal_strength = cycle_num * x
                signal_strength_sum += signal_strength
                print(signal_strength)
            print("cycle",cycle_num,"complete")
            cycle_num += 1
            print("starting cycle",cycle_num)
            if check_cycle(cycle_num):
                print("it's 20!",x)
                signal_strength = cycle_num * x
                signal_strength_sum += signal_strength
                print(signal_strength)

            print("cycle",cycle_num,"complete")
            print(x,"updating with:",num)
            x += num

    print("final x",x)
    print("final cycle",cycle_num)
    print(signal_strength_sum)

main(contents)