import pprint
data = open('19.txt').read()

class Rule:
    def __init__(self, rules):
        self.rules = rules
    def __repr__(self):
        return str(self.rules)

def findRule(id):
    for rule in rules:
        pass

ruleLines = data.split("\n\n")[0].splitlines()
rules = list([None] for _ in range(len(ruleLines)))

for line in ruleLines:
    splitRules = line.split(": ")[1].split(" | ")
    for i in range(len(splitRules)):
        splitRules[i] = splitRules[i].split(" ")
    newRule = Rule(splitRules)
    rules[int(line.split(": ")[0])] = newRule
print("----")
pprint.pprint(rules)

def getRule(char, index)


for char in rules[0].rules:
    print(char)
