def parseFile(filename):
    ranges = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if "-" in line:
                start, end = map(int, line.split("-"))
                ranges.append((start, end))
    return ranges

def mergeRanges(ranges):
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged

def countIDs(merged):
    count = 0
    for start, end in merged:
        count += (end - start + 1)
    return count

parsedfile = parseFile("Day 5/input.txt")
merged = mergeRanges(parsedfile)
print(countIDs(merged))
