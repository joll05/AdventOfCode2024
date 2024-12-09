from math import gcd

with open("input.txt") as f:
    raw_input = f.read().rstrip()

lines = raw_input.splitlines()

WIDTH = len(lines[0])
HEIGHT = len(lines)

antenna_frequencies = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            antenna_frequencies[char] = antenna_frequencies.get(char, tuple()) + ((x, y),)

antinodes = set()

for antennas in antenna_frequencies.values():
    for antenna_1 in antennas:
        for antenna_2 in antennas:
            if antenna_1 == antenna_2: continue

            a1_x, a1_y = antenna_1
            a2_x, a2_y = antenna_2

            diff_x, diff_y = a1_x-a2_x, a1_y-a2_y

            antinode = (a1_x, a1_y)

            while 0 <= antinode[0] < WIDTH and 0 <= antinode[1] < HEIGHT:
                antinodes.add(antinode)
                antinode = (antinode[0] + diff_x, antinode[1] + diff_y)

print(len(antinodes))