def read_moves(filename): ## Read moves from file
    with open(filename, 'r') as file:
        data = file.read().strip()
    return data

data = read_moves("Day 2/input.txt")

ranges = data.split(",")

numbers = [tuple(map(int, a.split("-"))) for a in ranges]

def is_invalidID(number) -> bool:
    a = str(number)

    if len(a) % 2 != 0:
        return False
    
    midpoint = len(a) // 2

    return a[midpoint:] == a[:midpoint]

invalidIDs = []

for x, y in numbers:
    for n in range(x, y + 1):
        if is_invalidID(n):
            invalidIDs.append(n)

print(sum(invalidIDs))