# Okay this time i was trying to finish first in my group of friends so I rushed it out.
# Pls ignore the mess

import re

dataset = open('4.txt', 'r').read()
passports = dataset.split("\n\n")
print(passports)

requiredFields = [
'byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid'
# 'cid',
]


def checkRequiredFields(requiredFields, fields):
    for requiredField in requiredFields:
        if requiredField not in fields.keys():
            return False

    for key, field in fields.items():
        # print(key + " " + field)
        if key == 'byr':
            if int(field) < 1920 or int(field) > 2002:
                print(key + " " + field)
                return False
        if key == 'iyr':
            if int(field) < 2010 or int(field) > 2020:
                print(key + " " + field)
                return False
        if key == 'eyr':
            if int(field) < 2020 or int(field) > 2030:
                print(key + " " + field)
                return False
        if key == 'hgt':
            if field[-2:] == 'cm':
                if int(field[:-2]) < 150 or int(field[:-2]) > 193:
                    print(key + " " + field)
                    return False
            elif field[-2:] == 'in':
                if int(field[:-2]) < 59 or int(field[:-2]) > 76:
                    print(key + " " + field)
                    return False
            else:
                return False
        if key == 'hcl':
            reg = re.compile('^#[0-9a-f]{6}$')
            matched = reg.match(field)
            if not matched:
                print(key + " " + field)
                return False
        if key == 'ecl':
            if field not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                print(key + " " + field)
                return False
        if key == 'pid':
            reg = re.compile('^[0-9]{9}$')
            matched = reg.match(field)
            if not matched:
                print(key + " " + field)
                return False

    return True

answer = 0
for data in passports:
    data = data.replace("\n", " ")
    fieldvalues = data.split(" ")
    fields = {}
    for fieldvalue in fieldvalues:
        fields[(fieldvalue.split(":")[0])] = fieldvalue.split(":")[1]
    valid = checkRequiredFields(requiredFields, fields)
    if valid:
        answer +=1

print(answer)


