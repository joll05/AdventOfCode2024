import re

def calculate_cost(prize_x: int, prize_y: int, delta_x_a: int, delta_y_a: int, delta_x_b: int, delta_y_b: int):
    n_A = (prize_y * delta_x_b - prize_x * delta_y_b) / (delta_y_a * delta_x_b - delta_x_a * delta_y_b)
    n_B = (prize_x - delta_x_a * n_A) / delta_x_b

    if not n_A.is_integer() or not n_B.is_integer():
        # no solution
        return 0

    return int(3 * n_A + n_B)

with open("input.txt") as f:
    raw_input = f.read().rstrip()

PATTERN = r"^Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)$"

total_cost_1 = 0
total_cost_2 = 0

for machine in raw_input.split("\n\n"):
    pattern_match = re.match(PATTERN, machine)
    delta_x_a, delta_y_a, delta_x_b, delta_y_b, prize_x, prize_y = map(int, [pattern_match[i] for i in range(1, 7)])
    total_cost_1 += calculate_cost(prize_x, prize_y, delta_x_a, delta_y_a, delta_x_b, delta_y_b)
    total_cost_2 += calculate_cost(prize_x + 10_000_000_000_000, prize_y + 10_000_000_000_000, delta_x_a, delta_y_a, delta_x_b, delta_y_b)

print(f"Original: {total_cost_1}")
print(f"Plus 10^13: {total_cost_2}")