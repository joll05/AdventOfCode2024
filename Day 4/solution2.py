with open("input.txt") as f:
    raw_input = f.read().rstrip()

DIRECTIONS = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

def x_mas(word_search, x, y):
    if word_search[y][x] != "A":
        return False
    
    diag_1 = word_search[y + 1][x + 1] + word_search[y - 1][x - 1]
    diag_2 = word_search[y + 1][x - 1] + word_search[y - 1][x + 1]

    return "M" in diag_1 and "S" in diag_1 and "M" in diag_2 and "S" in diag_2

lines = raw_input.splitlines()

word_search = tuple(tuple(line) for line in lines)

total = 0

for y in range(1, len(word_search) - 1):
    for x in range(1, len(word_search[0]) - 1):
        if x_mas(word_search, x, y):
            total += 1

print(total)