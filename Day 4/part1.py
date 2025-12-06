with open('Day 4/input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

def adjacent_rolls(grid, row, col):
    rolls = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for r, c in directions:
        new_row, new_col = row + r, col + c
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            rolls.append(grid[new_row][new_col])
    return rolls


def is_accessible(grid, row, col):
    if grid[row][col] != '@':
        return False

    rolls = adjacent_rolls(grid, row, col)
    count = rolls.count('@')

    return count < 4

accessible_count = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if is_accessible(grid, row, col):
            accessible_count += 1

print(accessible_count)
