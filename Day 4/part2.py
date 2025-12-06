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

def remove(grid):
    removed = 0
    while True:
        to_remove = []
        for r in range(len(grid)): ## Find all accessible rolls
            for c in range(len(grid[0])):
                if is_accessible(grid, r, c):
                    to_remove.append((r, c))

        if not to_remove: ## If no more accessible rolls, stop
            break
        
        for r, c in to_remove: ## Remove all accessible rolls
            grid[r][c] = '.' 
            print("Removed:", (r, c)) ## Debug line

        removed += len(to_remove) ## Count removed rolls

    return removed 

total = remove(grid)

print(total)
