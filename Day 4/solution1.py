with open("input.txt") as f:
    raw_input = f.read().rstrip()

DIRECTIONS = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

def string_in_search(word_search, string, x, y, direction):
    dx, dy = direction

    for i, char in enumerate(string):
        target_x, target_y = x + dx * i, y + dy * i
        
        if target_x < 0 or target_y < 0 or target_x >= len(word_search[0]) or target_y >= len(word_search):
            return False # outside of bounds, the word can't be found
        
        if word_search[target_y][target_x] != char:
            return False # word doesn't match
    
    return True

lines = raw_input.splitlines()

word_search = tuple(tuple(line) for line in lines)

total = 0

for y, line in enumerate(word_search):
    for x, char in enumerate(line):
        if char == "X":
            for dir in DIRECTIONS:
                if string_in_search(word_search, "XMAS", x, y, dir):
                    total += 1

print(total)