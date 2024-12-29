from dataclasses import dataclass
from collections import deque

class Map:
    def __init__(self, map_input: str):
        self.walls: set[tuple[int]] = set()
        self.movables: list[MovableObject] = []
        self.robot: MovableObject = None

        for y, line in enumerate(map_input.splitlines()):
            for x, char in enumerate(line):
                if char == "#":
                    self.walls.add((2 * x, y))
                    self.walls.add((2 * x + 1, y))
                elif char == "O":
                    new_object = MovableObject(2 * x, y, 2, self)
                    self.movables.append(new_object)
                elif char == "@":
                    self.robot = MovableObject(2 * x, y, 1, self)
    
    def find_movable(self, x, y):
        for movable in self.movables:
            if movable.contains_position(x, y):
                return movable
        
        return None

@dataclass
class MovableObject:
    x: int
    y: int
    width: int
    map: Map

    def contains_position(self, x, y):
        return self.y == y and self.x <= x < self.x + self.width
    
    def get_push_intrusion(self, dx, dy):
        intrusion = [(x + dx, self.y + dy) for x in range(self.x, self.x + self.width)]
        return list(filter(lambda pos: not self.contains_position(*pos), intrusion))
    
    def attempt_move(self, dx, dy):
        movables_to_push = [self]
        positions_to_check = deque(self.get_push_intrusion(dx, dy))

        while len(positions_to_check) > 0:
            pos = positions_to_check.pop()
            
            if pos in self.map.walls:
                return False
            
            movable = self.map.find_movable(*pos)
            if movable != None:
                if movable not in movables_to_push:
                    movables_to_push.append(movable)
                positions_to_check.extendleft(movable.get_push_intrusion(dx, dy))
        
        for movable in movables_to_push:
            movable.x += dx
            movable.y += dy
        
        return True


with open("input.txt") as f:
    raw_input = f.read().rstrip()

map_input, movement_input = raw_input.split("\n\n")

map_object = Map(map_input)
robot = map_object.robot

for char in movement_input:
    match char:
        case ">":
            robot.attempt_move(1, 0)
        case "v":
            robot.attempt_move(0, 1)
        case "<":
            robot.attempt_move(-1, 0)
        case "^":
            robot.attempt_move(0, -1)

print(sum(100 * obj.y + obj.x for obj in map_object.movables))