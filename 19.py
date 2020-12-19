import pprint

data = open('19.txt').read().splitlines()
data = '''0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

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
        parts[parts.index(part)] = part.strip('"').strip(" ").split(" ")
    rules[ruleNum] = parts



def fillRules():
    for ruleNum, rule in list(rules.items()):
        print("============")
        pprint.pprint(rules)
        parsedRules = []
        for part in rule:
            parsedPart = []
            for num in part:
                print(f"\t\tPARSED PART + {num}")
                if num not in ["a", "b"]:
                    parsedPart.append(rules[num])
                else:
                    parsedPart.append(num)
            print(f"\tadding {parsedPart} to parsedrules")
            parsedRules.extend(parsedPart)
        # print(parsedPart)
        print(f"adding {parsedRules} to rules")

        rules[str(ruleNum)] = parsedRules


fillRules()
for _ in range(1000):
    fillRules()
print(rules)
