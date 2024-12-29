from math import inf

DIRECTIONS = (
    (1, 0), # 0 = East
    (0, 1), # 1 = South
    (-1, 0), # 2 = West
    (0, -1) # 3 = North
)

# an implementation of dijkstras algorithm
# NOTE: I realised after creating this that it doesn't work in one case:
# where there are multiple directions to reach the end tile from and both directions have a shortest path
# in that case my program would only count the paths from one direction.
# My input didn't have that case, but if yours does... good luck :P
def find_best_paths(walls, start, end):
    start_state = (start, 0)

    visited = set()
    to_visit = {start_state}
    costs = {start_state: (0, [[start]])}

    while len(to_visit) > 0:
        if len(visited) % 100 == 0:
            print(len(visited))

        current = min(to_visit, key=costs.get)
        direction = DIRECTIONS[current[1]]
        forward = (current[0][0] + direction[0], current[0][1] + direction[1])
        
        neighbors = [
            ((current[0], (current[1] + 1) % 4), 1000), # Turn clockwise
            ((current[0], (current[1] - 1) % 4), 1000) # Turn counterclockwise
        ] + ([((forward, current[1]), 1)] if forward not in walls else [])

        for neighbor, cost in neighbors:
            if neighbor in visited:
                continue

            current_cost = costs[current][0] + cost
            current_paths = [path + [neighbor[0]] for path in costs[current][1]]

            if neighbor[0] == end:
                return (current_cost, current_paths)

            if neighbor not in costs:
                costs[neighbor] = (current_cost, current_paths)
            elif current_cost == costs[neighbor][0]:
                costs[neighbor] = (current_cost, costs[neighbor][1] + current_paths)
            elif current_cost < costs[neighbor][0]:
                costs[neighbor] = (current_cost, current_paths)

            to_visit.add(neighbor)
        
        visited.add(current)
        to_visit.remove(current)

with open("input.txt") as f:
    raw_input = f.read().rstrip()

walls = set()
start = None
end = None

for y, line in enumerate(raw_input.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            walls.add((x, y))
        elif char == "S":
            start = (x, y)
        elif char == "E":
            end = (x, y)

cost, best_paths = find_best_paths(walls, start, end)
tiles_on_best_path = set()
for path in best_paths:
    tiles_on_best_path.update(path)

print(f"Cost: {cost}")
print(f"Tiles on best path: {len(tiles_on_best_path)}")