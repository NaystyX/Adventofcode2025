
with open("Day 3/input.txt", "r") as f:
    inputdata = f.read().strip().split("\n")

""" ## Wrong approach but kept for learning
def get_maxnumber(data):
    s = str(data)
    maxnumber = 0
    secondmax = 0

    for number in s:
        number = int(number)

        if number > maxnumber:
            secondmax = maxnumber
            maxnumber = number
        
        elif number > secondmax and number != maxnumber:
            secondmax = number

    return int(str(maxnumber) + str(secondmax))
"""

def largestnumber(data):
    s = str(data)

    max_num = 0

    for i in range(len(s)): ## First number
        for j in range(i + 1, len(s)): ## Second number
            num = int(s[i] + s[j]) ## Form the total number
            if num > max_num: ## Compare with current maximum
                max_num = num ## Update if larger
    return max_num

total = 0
for data in inputdata:
    print(largestnumber(data)) ## Debug line
    total += largestnumber(data)

print(total)