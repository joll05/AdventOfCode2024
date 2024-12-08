with open("input.txt") as f:
    raw_input = f.read().rstrip()

rules_input, updates_input = raw_input.split("\n\n")

rules: dict[int, set[int]] = {}

for rule in rules_input.splitlines():
    prerequisite, page = map(int, rule.split("|"))
    
    if page not in rules:
        rules[page] = {prerequisite}
    else:
        rules[page].add(prerequisite)

# for page, prereqs in rules.items():
#     print(f"{page} len {len(prereqs)}: {prereqs}")

updates = [list(map(int, update.split(","))) for update in updates_input.splitlines()]

def correct_order(rules: dict[int, set[int]], update: list[int]):
    for i, page in enumerate(update):
        if page in rules:
            for prerequisite in rules[page]:
                if prerequisite not in update[:i] and prerequisite in update[i+1:]:
                    prerequisite_index = update.index(prerequisite)
                    new_update = update[:i] + update[i+1:prerequisite_index+1] + [page] + update[prerequisite_index+1:] # move page to after its prerequisite
                    return correct_order(rules, new_update)
        
    return update
    

total = 0

for update in updates:
    corrected = correct_order(rules, update)
    if corrected != update:
        total += corrected[len(corrected) // 2]

print(total)