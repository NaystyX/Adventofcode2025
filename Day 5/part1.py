def parse_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    ranges = []
    listofnums = []
    for line in lines:
        line = line.strip()
        
        if not line:
            continue

        if "-" in line:
            ranges.append(tuple(map(int, line.split("-"))))
        else:
            listofnums.append(int(line))
    return ranges, listofnums

ranges, listofnums = parse_input("Day 5/input.txt")

def IsFresh(num, ranges):
    for start, end in ranges:
        if start <= num <= end:
            return True
    return False

count = sum(IsFresh(num, ranges) for num in listofnums)

print(count)