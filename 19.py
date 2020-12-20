import pprint

data = open('19.txt').read().splitlines()
data = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''.split("\n\n")

# parse rules. index is the rule number
rules = {}

# EXAMPLE
# rules = {'0': [['4', '1', '5']],
#          '1': [['2', '3'],
#                ['3', '2']],
#          '2': [['4', '4'],
#                ['5', '5']],
#          '3': [['4', '5'],
#                ['5', '4']],
#          '4': [['a']],
#          '5': [['b']]}

for line in data[0].splitlines():

    # one day ill learn regex enough to want to use it instead of this:
    split = line.split(": ")
    parts = list(split[1].split(" | "))
    ruleNum = split[0]

    for part in parts:
        nums = part.strip('"').strip(" ").split(" ")
        for num in nums:
            if num.isnumeric():
                nums[nums.index(num)] = int(num)
        parts[parts.index(part)] = nums
    rules[int(ruleNum)] = parts


def checkRule(ruleNum, char, index):

    print(f"comparing {char} and {ruleNum} at index {index} ")
    if ruleNum in ['a', 'b']:
        return ruleNum == char

    ruleOr = rules[ruleNum]
    if ruleOr[0] in ['a', 'b']:
        return True
    # print(f"checking {char} == {ruleOr}")

    for rule in ruleOr:
        if checkRule(rule[index], char, index):
            return True
    return False


pprint.pprint(rules)
# print(checkRule(0, 'a', 0))
# print(rules)
for line in data[1].splitlines():
    print(f"CHECKING {line}")
    for i in range(len(line)):
        print(f"CHECKING CHAR {line[i]}")
        if checkRule(0,line[i], i):
            pass
        else:
            print(f"{line} NOT IT")
        print(f"{i} is TRUE")
