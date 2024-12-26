from dataclasses import dataclass
from math import log10

@dataclass
class StoneCollection:
    stones: dict[int, 'Stones']

    def __init__(self):
        self.stones = {}
    
    def add_stones(self, number, count):
        if number in self.stones:
            self.stones[number].count += count
        else:
            self.stones[number] = Stones(count, number)

    def transform_all(self):
        new_stones: list['Stones'] = []
        for stone in self.stones.values():
            new_stones += stone.transform()
        
        self.stones = {}

        for stone in new_stones:
            self.add_stones(stone.number, stone.count)
    
    def total_count(self):
        return sum(stone.count for stone in self.stones.values())

    def __str__(self) -> str:
        return ", ".join([f"{stone.number} (x{stone.count})" for stone in self.stones.values()])

@dataclass
class Stones:
    count: int
    number: int

    def transform(self):
        if self.number == 0:
            return [Stones(self.count, 1)]
        elif int(log10(self.number)) % 2 == 1:
            return self.split()
        else:
            return [Stones(self.count, self.number * 2024)]
    
    def split(self):
        digits = int(log10(self.number)) + 1
        midpoint = int(10 ** (digits // 2))

        left = Stones(self.count, self.number // midpoint)
        right = Stones(self.count, self.number % midpoint)

        return [left, right]

with open("input.txt") as f:
    raw_input = f.read().rstrip()

collection = StoneCollection()

for stone in raw_input.split(" "):
    collection.add_stones(int(stone), 1)

for i in range(25):
    collection.transform_all()

print(f"25: {collection.total_count()}")

for i in range(50):
    collection.transform_all()

print(f"75: {collection.total_count()}")