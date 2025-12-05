
with open("Day 3/input.txt", "r") as f:
    inputdata = f.read().strip().split("\n")


def largestnumber(data, n):
    s = str(data)
    numbers = [] 
    skips = len(s) - n

    for i in s:
        while numbers and skips > 0 and numbers[-1] < i: ## If current number is larger than last in list
            numbers.pop() ## Remove last number
            skips -= 1 ## Decrease skips
        numbers.append(i) 

    return int(''.join(numbers[:n])) ## Join only first n numbers

total = 0
for data in inputdata:
    print(largestnumber(data, 12)) ## Debug line
    total += largestnumber(data, 12)

print(total)