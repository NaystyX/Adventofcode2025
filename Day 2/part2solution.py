def read_moves(filename): ## Read moves from file
    with open(filename, 'r') as file:
        data = file.read().strip()
    return data

data = read_moves("Day 2/input.txt")

ranges = data.split(",")

numbers = [tuple(map(int, a.split("-"))) for a in ranges]

def is_invalidID(number) -> bool:
    a = str(number)
    b = len(a)

    for block in range(1, b // 2 + 1):
        if b % block != 0: ## If not divisible, skip
            continue
        
        repeat = b // block ## Number of times block repeats

        if repeat < 2: ## Must repeat atleast 2 times
            continue

        block = a[:block] ## get block

        if block * repeat == a: ## Check if repeating blocks form number
            return True
    return False


invalidIDs = []

for x, y in numbers:
    for n in range(x, y + 1):
        if is_invalidID(n):
            invalidIDs.append(n)

print(sum(invalidIDs))