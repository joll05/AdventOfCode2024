with open("input.txt") as f:
    raw_input = f.read().rstrip()

lines = raw_input.splitlines()

equations = []

for line in lines:
    result, values = line.split(": ")
    
    equations.append((int(result), list(map(int, values.split(" ")))))

def validate(result, values):
    if values[0] > result:
        return False
    
    if len(values) == 1:
        return values[0] == result
    
    return validate(result, [values[0] + values[1]] + values[2:]) or validate(result, [values[0] * values[1]] + values[2:])

total = 0

for result, values in equations:
    if validate(result, values):
        total += result

print(total)
