from dataclasses import dataclass
from collections import deque

NEIGHBORS = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)

class Region:
    def __init__(self, letter):
        self.letter = letter

        self.area = 0
        self.perimeter = 0
        self.tiles = set()
        self.corners = set()
    
    def construct(self, start: tuple[int], available_tiles: set[tuple[int]]):
        tiles_to_check = deque([start])

        while len(tiles_to_check) != 0:
            tile = tiles_to_check.popleft()

            if tile in available_tiles:
                self.tiles.add(tile)
                available_tiles.remove(tile)
                self.area += 1
                self.perimeter += 4

                for dx, dy in NEIGHBORS:
                    neighbor = (tile[0] + dx, tile[1] + dy)

                    if neighbor in self.tiles:
                        self.perimeter -= 2
                    else:
                        tiles_to_check.append(neighbor)
    
    def count_corners(self):
        count = 0
        for x, y in self.tiles:
            for i, (dx1, dy1) in enumerate(NEIGHBORS):
                (dx2, dy2) = NEIGHBORS[(i + 1) % len(NEIGHBORS)] # get the next neighbor clockwise
                neighbor1, neighbor2 = (x + dx1, y + dy1), (x + dx2, y + dy2)
                if neighbor1 not in self.tiles and neighbor2 not in self.tiles:
                    # if a tile has no tile on 2 adjacent neighbors, that's a corner
                    count += 1
                elif neighbor1 in self.tiles and neighbor2 in self.tiles:
                    if (x + dx1 + dx2, y + dy1 + dy2) not in self.tiles:
                        # if both adjacent neighbors have tiles, and there is no tile joining them, that's an inner corner
                        count += 1
        
        return count


with open("input.txt") as f:
    raw_input = f.read().rstrip()

available_tiles: dict[str, set[tuple[int]]] = {}

for y, line in enumerate(raw_input.splitlines()):
    for x, char in enumerate(line):
        if char in available_tiles:
            available_tiles[char].add((x, y))
        else:
            available_tiles[char] = {(x, y)}

regions: list[Region] = []

for letter, area in available_tiles.items():
    while len(area) != 0:
        new_region = Region(letter)
        new_region.construct(next(iter(area)), area)
        regions.append(new_region)

print(f"Area * Perimeter: {sum(region.area * region.perimeter for region in regions)}")
# number of corners = number of sides
print(f"Area * Number of Sides: {sum(region.area * region.count_corners() for region in regions)}")