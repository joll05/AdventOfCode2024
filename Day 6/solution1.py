with open("input.txt") as f:
    raw_input = f.read().rstrip()

lines = raw_input.splitlines()

DIRECTIONS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

blockades: set[tuple[int]] = set()

position = None
direction = UP

for y, line in enumerate(raw_input.splitlines()):
    for x, tile in enumerate(line):
        if tile == "#":
            blockades.add((x, y))
        elif tile == "^":
            position = (x, y)

visited = set()

while 0 <= position[0] < len(lines[0]) and 0 <= position[1] < len(lines):
    x, y = position
    
    visited.add(position)

    movement_x, movement_y = DIRECTIONS[direction]

    next_position = (x + movement_x, y + movement_y)

    if next_position not in blockades:
        position = next_position
    else:
        direction = (direction + 1) % 4

print(len(visited))