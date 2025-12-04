def read_moves(filename): ## Read moves from file
    with open(filename, 'r') as file:
        moves = [line.strip() for line in file.readlines()]
    return moves

moves = read_moves("Day 1/input.txt")

def get_direction(move): ## Get direction from the first character of the move
    if move[0] == 'R':
        return 1
    elif move[0] == 'L':
        return -1
    else:
        return 0
    
def get_steps(move): ## Get number of steps from the move
    return int(move[1:])

i = 0
count = 0
dial = 50
while i < len(moves): ## Go through every move
    direction = get_direction(moves[i])
    steps = get_steps(moves[i])
    for step in range(steps): ## Move the dial step by step so can check if it goes under 0 or over 99
        dial += direction
        if dial < 0:
            dial = 99
        elif dial > 99:
            dial = 0
        if dial == 0: ## If dial is at 0 during steps increase count
            count += 1
    print("Dial position:", dial) ## Debug print
    i += 1

""" Part 1
while i < len(moves): ## Go through every move
    direction = get_direction(moves[i])
    steps = get_steps(moves[i])
    for step in range(steps): ## Move the dial step by step so can check if it goes under 0 or over 99
        dial += direction
        if dial < 0:
            dial = 99
        elif dial > 99:
            dial = 0
    print("Dial position:", dial) ## Debug print
    if dial == 0: ## If dial is at 0 after steps increase count
        count += 1
    i += 1
"""


print("The dial was at 0 for", count, "times.") 
