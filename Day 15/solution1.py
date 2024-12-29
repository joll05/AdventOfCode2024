from dataclasses import dataclass

class Map:
    def __init__(self, map_input: str):
        self.walls: set[tuple[int]] = set()
        self.movables: dict[tuple[int], MovableObject] = {}
        self.robot: MovableObject = None

        for y, line in enumerate(map_input.splitlines()):
            for x, char in enumerate(line):
                if char == "#":
                    self.walls.add((x, y))
                elif char == "O" or char == "@":
                    new_object = MovableObject(x, y, self)
                    self.movables[x, y] = new_object

                    if char == "@":
                        self.robot = new_object
    
    def set_movable_position(self, x, y, new_x, new_y):
        self.movables[new_x, new_y] = self.movables.pop((x, y))

@dataclass
class MovableObject:
    x: int
    y: int
    map: Map

    def attempt_move(self, dx, dy) -> bool:
        new_pos = (self.x + dx, self.y + dy)

        if new_pos in self.map.walls:
            return False
        
        if new_pos in self.map.movables:
            success = self.map.movables[new_pos].attempt_move(dx, dy)
            if success:
                self.change_position(*new_pos)
            
            return success

        # no wall or object

        self.change_position(*new_pos)
        return True

    def change_position(self, x, y):
        self.map.set_movable_position(self.x, self.y, x, y)
        self.x = x
        self.y = y

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

print(sum(100 * obj.y + obj.x for obj in map_object.movables.values() if obj is not robot))