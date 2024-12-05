with open('./input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# split on newline
index_split = lines.index('')
rule_strs = lines[:index_split]
update_strs = lines[index_split+1:]

# parse rules
rules = []
for rule_str in rule_strs:
    rule_list = rule_str.split('|')
    rule = (int(rule_list[0]), int(rule_list[1]))
    rules.append(rule)

# parse updates
updates = []
for update_str in update_strs:
    update_list = update_str.split(',')
    update = [int(x) for x in update_list]
    updates.append(update)

test_line = [75,47,61,53,29]
test_bad_line = [75,97,47,61,53]

correct_update_middles = []
for update in updates:
    for rule in rules:
        correct = True
        if rule[0] in update and rule[1] in update:
            correct = update.index(rule[0]) < update.index(rule[1])
            if not correct:
                # print('incorrect', update)
                break
    if correct:
        middle = len(update) // 2
        correct_update_middles.append(update[middle])

print(sum(correct_update_middles))
