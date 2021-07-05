#!/usr/bin/python3


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Func to find valid passport
def validPass(passport):
    for field in fields:
        # If field is not in passport
        if field not in passport:
            return False
    return True

with open('data/day04_data.txt') as file:
    data = file.readlines()
    data = [index.strip() for index in data]
    
valid, validPasses = 0, []

currentPass = ''
for index in data:
    if index != '':
        currentPass += ' ' + index
    else:
        if validPass(currentPass):
            valid += 1
            validPasses.append(currentPass)
        currentPass = ''

if validPass(currentPass):
    validPasses.append(currentPass)
    valid += 1

print(valid)



# Part 2


# Check each field
def valid_byr(byr):
    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return False
    return True

def valid_iyr(iyr):
    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False
    return True

def valid_eyr(eyr):
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False
    return True

def valid_hgt(hgt):
    measurement = hgt[-2:]
    if measurement not in ['in', 'cm']:
        return False

    hgt = int(hgt[:-2])
    
    if measurement == 'in':
        if hgt < 59 or hgt > 76:
            return False
    elif measurement == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    return True

def valid_hcl(hcl):
    if hcl[0] != '#':
        return False
    if (len(hcl[1:])) != 6:
        return False
    return True

def valid_ecl(ecl):
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    return True

def valid_pid(pid):
    if len(pid) != 9:
        return False
    return True


# Create dictionary of each field and their value for all valid passes
def validData(passport):
    passport = passport.split()
    data = {}

    for item in passport:
        key = item[:3]
        value = item[4:]
        data[key] = value
   
    if not valid_byr(data['byr']):
        return False
    if not valid_iyr(data['iyr']):
        return False
    if not valid_eyr(data['eyr']):
        return False
    if not valid_hgt(data['hgt']):
        return False
    if not valid_hcl(data['hcl']):
        return False
    if not valid_ecl(data['ecl']):
        return False
    if not valid_pid(data['pid']):
        return False

    return True


valid = 0
for passports in validPasses:
    if validData(passports):
        valid += 1


print(valid)
