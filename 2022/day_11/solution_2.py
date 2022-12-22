from re import findall, search

with open('./input.txt') as f:
    # strip whitespace, put in new array
    contents = [line.strip() for line in f.readlines()]

class Monkey:
    def __init__(self, monkey):
        self.monkey_num = monkey
        self.items = []

        self.operator = None
        self.operator_num = None # could be "old" or int

        self.test_divisible = None
        self.test_true = None
        self.test_false = None

        self.inspection_num = 0

    def __str__(self):
        return f'Monkey {self.monkey_num}: {self.items}, {self.inspection_num}'

    def inspection(self, item_worry_level, mult_divisors):
        # assume receiving ONE item
        # output worry level + monkey-to-throw-to

        # (handle old versus int)
        if type(self.operator_num) != int:
            operator_num = item_worry_level
        else:
            operator_num = self.operator_num

        # handle Operation to get new worry level
        if self.operator == '*':
            new_item_worry_level = item_worry_level * operator_num
        elif self.operator == '+':
            new_item_worry_level = item_worry_level + operator_num

        # handle worry level not getting too big
        new_item_worry_level = new_item_worry_level % mult_divisors

        if new_item_worry_level % self.test_divisible == 0:
            monkey_to_throw_to = self.test_true
        else:
            monkey_to_throw_to = self.test_false

        self.inspection_num += 1

        # output new worry level of item
        # and also which monkey to throw to based on test
        return [new_item_worry_level,monkey_to_throw_to]

def setup_monkey_list(monkey_line_list):
    monkey_list = []
    for line in monkey_line_list:
        if line.startswith("Monkey"):
            monkey_num = int(line[-2])
            current_monkey = Monkey(monkey_num)
        elif line.startswith("Starting"):
            str_list_items = findall(r'[0-9]+', line)
            for item in str_list_items:
                current_monkey.items.append(int(item))
        elif line.startswith("Operation"):
            current_monkey.operator = line[21]
            ending_num = line.rsplit(" ")[-1]
            if ending_num == 'old':
                # I'll handle this when inspecting
                current_monkey.operator_num = ending_num
            else:
                current_monkey.operator_num = int(ending_num)
        elif line.startswith("Test:"):
            current_monkey.test_divisible = int(search(r'\d+', line).group())
        elif line.startswith("If true"):
            current_monkey.test_true = int(line[-1])
        elif line.startswith("If false"):
            current_monkey.test_false = int(line[-1])
            # "if false" is the last line, so add the monkey and increase monkey num
            monkey_list.append(current_monkey)
            monkey_num += 1

    return monkey_list

def main(lines):
    proper_monkey_list = setup_monkey_list(lines)

    divisors_multiplied = 1
    for monkey in proper_monkey_list:
        divisors_multiplied *= monkey.test_divisible
    # 96577 for test

    num_rounds = 10000

    for round in range(0,num_rounds):
        # iterate over monkeys
        for monkey in proper_monkey_list:
            if len(monkey.items) > 0:
                for item in monkey.items:
                    new_item_value, monkey_to_throw_to = monkey.inspection(item, divisors_multiplied)
                    proper_monkey_list[monkey_to_throw_to].items.append(new_item_value)
                # clear out all items
                monkey.items = []

    list_of_inspection_nums = []
    for monkey in proper_monkey_list:
        list_of_inspection_nums.append(monkey.inspection_num)

    solution = sorted(list_of_inspection_nums)[-1] * sorted(list_of_inspection_nums)[-2]
    print(solution)

main(contents)