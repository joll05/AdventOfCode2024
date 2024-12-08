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

total = 0

for update in updates:
    valid = True

    for i, page in enumerate(update):
        if page in rules:
            for prerequisite in rules[page]:
                if prerequisite not in update[:i] and prerequisite in update[i+1:]:
                    valid = False
                    break
        
        if not valid:
            break
    
    if valid:
        total += update[len(update) // 2]

print(total)