#!/usr/bin/python3

with open("data/day03_data.txt", "r") as file:
    reader = file.read()
    reader_list = reader.splitlines()
    
    # Part 1
    # total = trees | x = Increment Value 
    total, x = 0, 0

    for line in reader_list:
        # Iterate through each line in increments of 3
        if line[x] == "#":
            total += 1
        x += 3
        
        # Find remainder to use for next line
        x %= len(line)

    print("Part 1: ", end="")
    print(total)


    # Part 2 - Use this function
    def tree(right: int, down: int):
        total = 0
        x = 0
        y = 0

        while y < len(reader_list):
            line = reader_list[y]
            

            # Iterate through each line in increments of 3
            if line[x] == "#":
                total += 1
            x += right
        
            # Find remainder to use for next line
            x %= len(line)

            y += down

        return total
    

    def computeTotal():
        return tree(1, 1) * tree(3, 1) * tree(5, 1) * tree(7, 1) * tree(1, 2)
    
    print("Part 2: ", end="")
    print(computeTotal())
