# Feast your eyes upon the most overdone sloppy code i've written

data = open('16.txt').read()
# data = """class: 0-1 or 4-19
# departure row: 0-5 or 8-19
# departure seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9"""

data = data.split("\n\n")


def parseRules(text):
    textLines = text.splitlines()

    for line in textLines:
        ruleName = line.split(": ")[0]
        ruleValue = line.split(": ")[1]
        for numRange in ruleValue.split(" or "):
            nums = numRange.split("-")
            for i in range(int(nums[0]), int(nums[1]) + 1):
                validNumbers.append(i)
                if ruleName in rules.keys():
                    rules[ruleName].append(i)
                else:
                    rules[ruleName] = [i]


# part 2
def validNumberForRule(num, rule):
    return num in rules[rule]



ruleText = data[0]
nearbyTickets = data[2].splitlines()[1:]
myTicket = data[1].splitlines()[1].split(",")

rules = {}
validNumbers = []
invalidRules = []

parseRules(data[0])

print(myTicket)
for line in nearbyTickets:
    # print(line)
    values = line.split(",")
    for value in values:
        value = int(value)
        if value not in validNumbers:
            invalidRules.append(value)

print(f"PART 1: {sum(invalidRules)}")

nearbyTickets.append(",".join(myTicket))
# print(nearbyTickets)
print(rules)
possibleRuleArray = {}
possibleValues = list(range(0, len(myTicket)))

for currentRow in range(len(myTicket)):
    # print("----")
    # print(currentRow)
    for rule in rules.keys():
        # print(f"=={rule}==")
        if rule not in possibleRuleArray:

            possibleRuleArray[rule] = possibleValues[:]

        for ticket in nearbyTickets:
            checkNum = int(ticket.split(",")[currentRow])
            if checkNum not in validNumbers:
                continue
            # print(f"checking if {checkNum} in {rule}")
            if not validNumberForRule(checkNum, rule):
                # print(f"ROW {currentRow} IS NOT {rule}. {checkNum} NOT in {rules[rule]}")
                if currentRow in possibleValues:
                    possibleRuleArray[rule].pop(possibleRuleArray[rule].index(currentRow))
        print(possibleRuleArray)
# print("--")
answer = {}
# print(possibleRuleArray)

# I did the part above wrong.. but narrow down possibilities to find the answer
for x in range(0,100):
    for key, value in possibleRuleArray.items():
        # [1, 2]
        if len(value) == 1:
            # print(f"REMOVING ALL {value[0]}s")
            for key2, value2 in possibleRuleArray.items():
                # print(key2, key)
                if key2 != key and value[0] in possibleRuleArray[key2]:
                    possibleRuleArray[key2].pop(possibleRuleArray[key2].index(value[0]))
print(possibleRuleArray)
print("what")

answer = 1
for key, value in possibleRuleArray.items():
    if "departure" in key:
        # print(myTicket[value[0]])
        answer *= int(myTicket[value[0]])
print(answer)


