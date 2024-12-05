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

def fix_mistakes(update, broken_rule):
    fixed_update = update.copy()
    # switch em
    fixed_update[update.index(broken_rule[0])] = broken_rule[1]
    fixed_update[update.index(broken_rule[1])] = broken_rule[0]
    fixed, new_broken = check_against_rules(fixed_update)
    if fixed:
        return fixed_update
    else:
        return fix_mistakes(fixed_update, new_broken)

def check_against_rules(update):
    for rule in rules:
        correct = True
        if rule[0] in update and rule[1] in update:
            correct = update.index(rule[0]) < update.index(rule[1])
            if not correct:
                return False, rule
    return correct, None

incorrect_updates = []
incorrect_updates_middles = []
for index in range(len(updates)):
    correct, broken = check_against_rules(updates[index])
    if not correct:
        incorrect_updates.append(index)
        fixed = fix_mistakes(updates[index], broken)
        updates[index] = fixed
        middle = len(fixed) // 2
        incorrect_updates_middles.append(fixed[middle])

print(sum(incorrect_updates_middles))
