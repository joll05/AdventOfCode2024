import re

with open("input.txt") as f:
    raw_input = f.read().rstrip()

instruction_pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

matches = re.finditer(instruction_pattern, raw_input)

total = 0
enabled = True

for match in matches:
    if match[3]: # if the third capturing group is not empty, it's a do() instruction
        enabled = True
    elif match[4]: # if the fourth capturing group is not empty, it's a don't() instruction
        enabled = False
    elif enabled:
        total += int(match[1]) * int(match[2])

print(total)