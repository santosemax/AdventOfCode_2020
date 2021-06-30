#!/usr/bin/python3

# Initializing Lists
amount, letter, string, least = [], [], [], []

with open("text.txt", "r") as file:
    reader = file.read().split()

    # Filling the Lists from file
    for i in range(len(reader)): 
        # Range
        if i % 3 == 0:
            amount.append(reader[i])
                        
        # Letter
        if i % 3 == 1:
            letter.append(reader[i].strip(":"))

        # String
        if i % 3 == 2:
            string.append(reader[i])

# Need to find least range for i
for i in range(len(amount)):
    print(amount[i][:1])
        
# Need to find most range for i


