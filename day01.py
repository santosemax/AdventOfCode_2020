#!/usr/bin/python3

from sys import exit

with open("data/day01_data.txt", "r") as file:
    # Array to store numbers
    nums = []

    # Iterate through file and store each number in array
    for line in file:
        nums.append(int(line.strip()))
    
    print("Part 1:")
    # Iterate through array to find sum of 2020. Once found, print.
    for i in range(len(nums)):
        for ii in range(len(nums)):
            total = nums[i] + nums[ii]
    
            if total == 2020:
                print(f"Num 1: {nums[i]}")
                print(f"Num 2: {nums[ii]}")
                print(f"Solution: {nums[i] * nums[ii]}")
                break
            else:
                total = 0
        if total == 2020:
            break
    
    print("Part 2:")
    for i in range(len(nums)):
        for ii in range(len(nums)):
            for iii in range(len(nums)):
                total = nums[i] + nums[ii] + nums[iii]

                if total == 2020:
                    print(f"Num 1: {nums[i]}")
                    print(f"Num 2: {nums[ii]}")
                    print(f"Num 3: {nums[iii]}")
                    print(f"Solution: {nums[i] * nums[ii] * nums[iii]}")
                    exit(0)
                else:
                    total = 0
        if total == 2020:
            break
