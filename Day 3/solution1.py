import re

with open("input.txt") as f:
    raw_input = f.read().rstrip()

mul_pattern = r"mul\((\d+),(\d+)\)"

matches = re.finditer(mul_pattern, raw_input)

total = 0

for match in matches:
    total += int(match[1]) * int(match[2])

print(total)