# Recursion is really hard at nearly midnight on a sunday... but I got it
# 10:00 PM - 11:40 PM

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

def parseinput():
    finalRules = {}
    dataset = open('7.txt', 'r').read().splitlines()
    for line in dataset:
        # too annoying to regex
        bagColor, line = line.split(' bags contain')[0].strip(), line.split(' bags contain')[1].strip()

        finalRules[bagColor] = {}
        for ruleText in line.split(", "):
            if ruleText == "no other bags.":
                continue
            words = ruleText.replace(".", "").split(" ")
            q = words[0]
            color = " ".join(words[1:3])
            finalRules[bagColor][color] = int(q)
    return finalRules

rules = parseinput()
print("parsed rulse")
class Bag:
    def __init__(self, color, depth = 0):
        self.color = color
        self.depth = depth
        self.children = []
        self.populateChildren()
        self.childCount = 0
        # self.countChildren()
        # self.parents = []
        # self.populateParents()
        # if self.depth > 10:
        #     return
        # else:
        self.depth+=1

    def populateParents(self):
        for color, rule in rules.items():
            for bag, quantity in rule.items():

                if bag == self.color:
                    self.parents.append(color)
        self.parents = list(dict.fromkeys(self.parents))



    def listPossibleParents(self, depth, colorList = [], bag = None):
        depth += 1
        if depth > 20:
            return colorList
        if bag == None:
            bag = self
        colorList.append(bag.color)

        for parentColor in bag.parents:
            if parentColor not in colorList:
                parent = Bag(parentColor, depth)
                newColors = self.listPossibleParents(depth, colorList, parent)
                if newColors != None:
                    colorList.extend(newColors)
        return list(dict.fromkeys(colorList))

    def populateChildren(self):
        for key, value in rules.items():
            if self.color == key:
                for color, quantity in value.items():
                    self.children.extend(Bag(color, self.depth) for _ in range(quantity))

    def countChildren(self, count = 0):
        for child in self.children:
            count += child.countChildren() + 1
        return count

    def hasGold(self):
        for bag in self.children:
            if bag.color == 'sg':
                return True
        return False

    def canContainGold(self, depth = 0):

        for bag in self.children:
            if bag.hasGold():
                return True
            if bag.children == []:
                return False
            if depth > 10:
                return False
            depth+=1
            bag.canContainGold(depth)

bag = Bag('shiny gold', 0)
# print(len(bag.listPossibleParents(0)))
print(bag.countChildren())
# answer = 0
# for color in colors:
#     bag = Bag(color, 0)
#     if bag.canContainGold():
#         answer+=1
