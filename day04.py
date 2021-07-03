#!/usr/bin/python3

# Fields (Don't include cid b/c doesn't count)
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("test.txt", "r") as file:
    reader = file.readlines()
    
    for i in range(len(reader)):
        print(reader[i])    


    # Iterate through each line in file -> If first letter of line == '' then go next
     
