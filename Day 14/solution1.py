import re

with open("input.txt") as f:
    raw_input = f.read().rstrip()

WIDTH = 101
HEIGHT = 103
STEPS = 100

PATTERN = r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$"

quarters = [0, 0, 0, 0]

for line in raw_input.splitlines():
    match = re.match(PATTERN, line)
    x, y, vx, vy = map(int, [match[i] for i in range(1, 5)])
    
    new_x = (x + vx * STEPS) % WIDTH
    new_y = (y + vy * STEPS) % HEIGHT
    
    if new_x < WIDTH // 2:
        if new_y < HEIGHT // 2:
            quarters[0] += 1
        elif new_y > HEIGHT // 2:
            quarters[1] += 1
    elif new_x > WIDTH // 2:
        if new_y < HEIGHT // 2:
            quarters[2] += 1
        elif new_y > HEIGHT // 2:
            quarters[3] += 1

print(quarters[0] * quarters[1] * quarters[2] * quarters[3])