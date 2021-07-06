#!/usr/bin/python3


def findRow(passport):
    lower, upper = 0, 127
    for alpha in range(6):
        mid = (lower + upper) // 2
        if passport[alpha] == "F":
            upper = mid
        elif passport[alpha] == "B":
            lower = mid + 1

    if passport[6] == 'F':
        return lower
    else:
        return upper

def findColumn(passport):
    lower, upper = 0, 7
    for i in range(2):
        mid = (lower + upper) // 2
        if passport[i] == "L":
            upper = mid
        elif passport[i] == "R":
            lower = mid + 1

    if passport[2] == 'L':
        return lower
    else:
        return upper
        
            
largestID = 0
ids = []
with open("data/day05_data.txt") as file:
    data = file.read()
    data = data.splitlines() 

for line in data:
    row = findRow(line[:7])
    column = findColumn(line[7:])

    id = row * 8 + column
    ids.append(id)

print(max(ids))

for id in ids:
    if id+1 not in ids and id+2 in ids:
        missing = id + 1

print(missing)









