#!/usr/bin/python3
import re

counter, counter2 = 0, 0
passed = []

# Fields (Don't include cid b/c doesn't count)
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
passed = []

with open("data/day04_data.txt", "r") as file:
    reader = file.read()
    reader = reader.split("\n\n")
     
total = len(reader)

# Iterate through each line in file and search for fields
for i in range(len(reader)):
    for ii in range(len(fields)):
        if re.search(fields[ii], reader[i]) == None:
            counter += 1
            break

print(f"Part 1: \n{total-counter}")
