with open("input.txt") as f:
    raw_input = f.read().rstrip()

def is_safe(report: tuple[int]):
    previous = report[0]
    direction = 0

    for number in report[1:]:
        change = number - previous

        if not 1 <= abs(change) <= 3:
            return False
        
        if (direction > 0 and change < 0) or (direction < 0 and change > 0):
            return False
        elif direction == 0:
            direction = change

        previous = number
    
    return True

lines = raw_input.splitlines()

reports = [tuple(map(int, line.split(" "))) for line in lines]

total = 0

for report in reports:
    if is_safe(report):
        total += 1
    else:
        dampened = False
        for removed in range(len(report)):
            if is_safe(report[:removed] + report[removed+1:]):
                dampened = True
                break
        if dampened:
            total += 1

print(total)