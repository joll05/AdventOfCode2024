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

safe_reports = list(filter(is_safe, reports))

print(len(safe_reports))