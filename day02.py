#!/usr/bin/python3

import re

# Initializing Lists
amount, letter, string, least, most = [], [], [], [], []
valid, valid2 = 0, 0

with open("data/day02_data.txt", "r") as file:
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


# Need to find least and most range for i
for i in range(len(amount)):
  temp = re.findall(r'\d+', amount[i])
  least = int(temp[0])
  most = int(temp[1])
  
  # Now that we have the least and most of each letter, iterate thru strings
  counter = 0
  for char in string[i]:
    if char == letter[i]:
      counter += 1
  
  if counter >= least and counter <= most:
    valid += 1
          
  # Part 2 Calcs (Subtract 1 b/c 0 based index)
  if string[i][least-1] == letter[i] or string[i][most-1] == letter[i]:
    valid2 += 1
  if string[i][least-1] == letter[i] and string[i][most-1] == letter[i]:
    valid2 -= 1

# Print # of Passwords for Part 1
print("Part 1:")
print(valid)

# Print # of Passwords for Part 2
print("Part 2:")
print(valid2)
