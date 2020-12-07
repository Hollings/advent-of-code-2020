# Recursion is really hard at nearly midnight on a sunday... but I got it
# I ended up just deleting a ton of my part 1 code, so this just solves part 2
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

class Bag:
    def __init__(self, color):
        self.color = color
        self.children = []
        self.populateChildren()
        self.childCount = 0

    def populateChildren(self):
        """
        Recursively create child tree
        """
        for key, value in rules.items():
            if self.color == key:
                for color, quantity in value.items():
                    self.children.extend(Bag(color) for _ in range(quantity))

    def countChildren(self, count = 0):
        for child in self.children:
            count += child.countChildren() + 1
        return count

bag = Bag('shiny gold')
print(bag.countChildren())
