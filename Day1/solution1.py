with open("input.txt") as f:
    raw_input = f.read().rstrip()

lines = raw_input.splitlines()
# create a list of rows with the numbers from the respective columns
rows = [tuple(int(i) for i in line.split()) for line in lines]

# zip the rows together to get 2 lists with the columns
left, right = zip(*rows)

left, right = sorted(left), sorted(right)

pairs = zip(left, right)

differences = [abs(a - b) for a, b in pairs]

print(sum(differences))