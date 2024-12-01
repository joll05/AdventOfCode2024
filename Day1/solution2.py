from collections import Counter

with open("input.txt") as f:
    raw_input = f.read().rstrip()

lines = raw_input.splitlines()
# create a list of rows with the numbers from the respective columns
rows = [tuple(int(i) for i in line.split()) for line in lines]

# zip the rows together to get 2 lists with the columns
left, right = zip(*rows)

left_count = Counter(left)
right_count = Counter(right)

total = 0
for number in left_count:
    total += left_count[number] * right_count[number] * number

print(total)