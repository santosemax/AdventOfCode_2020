#!/usr/bin/python3

seat = "FBFBBFFRLR"

# Split first 7 chars and the rest
#row = seat[:7] # 0 - 127
#column = seat[-3:] # 0-7

with open("data/day05_data.txt") as file:
    data = file.read()
    data = data.splitlines() 

for line in data:
    row = line[:7]
    column = line[-3:]


    # Finding row for current line
    for alpha in line:
        

