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

for y, line in enumerate(raw_input.splitlines()):
    for x, tile in enumerate(line):
        if tile == "#":
            blockades.add((x, y))
        elif tile == "^":
            position = (x, y)

def simulate_movement(start_position, start_direction, blockades):
    position = start_position
    direction = start_direction
    visited = set()
    visited_directions = set()

    while True:
        if not (0 <= position[0] < len(lines[0]) and 0 <= position[1] < len(lines)):
            return (False, visited)

        if (direction, position) in visited_directions:
            return (True, visited)

        x, y = position
        
        visited.add(position)
        visited_directions.add((direction, position))

        movement_x, movement_y = DIRECTIONS[direction]

        next_position = (x + movement_x, y + movement_y)

        if next_position not in blockades:
            position = next_position
        else:
            direction = (direction + 1) % 4

_, possible_blockades = simulate_movement(position, UP, blockades)

total = 0

for i, location in enumerate(possible_blockades, start=1):
    is_loop, _ = simulate_movement(position, UP, blockades | {location})

    if is_loop:
        total += 1
    
    if i % 100 == 0 or i == len(possible_blockades):
        print(f"{i}/{len(possible_blockades)}")

print(total)