from dataclasses import dataclass

@dataclass(eq=False)
class Node:
    height: int
    connections: list['Node']

    def __init__(self, height: int):
        self.height = height
        self.connections = []
        self.score = None
    
    def reachable_peaks(self):
        if self.height == 9:
            return [self]
        
        result = []
        for connection in self.connections:
            for peak in connection.reachable_peaks():
                if peak not in result:
                    result.append(peak)
        
        return result

    def rating(self):
        if self.height == 9:
            return 1
        
        return sum(connection.rating() for connection in self.connections)


with open("input.txt") as f:
    raw_input = f.read().rstrip()

NEIGHBORS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

grid: list[list[Node]] = []

trailheads: list[Node] = []

for line in raw_input.splitlines():
    new_row = []
    for char in line:
        height = int(char)
        
        node = Node(height)
        new_row.append(node)

        if height == 0:
            trailheads.append(node)

    grid.append(new_row)

for y, row in enumerate(grid):
    for x, node in enumerate(row):
        for dx, dy in NEIGHBORS:
            tx, ty = x + dx, y + dy
            
            if 0 <= tx < len(row) and 0 <= ty < len(grid):
                neighbor = grid[ty][tx]
                if neighbor.height == node.height + 1:
                    node.connections.append(neighbor)

print(f"Score: {sum(len(node.reachable_peaks()) for node in trailheads)}")
print(f"Rating: {sum(node.rating() for node in trailheads)}")