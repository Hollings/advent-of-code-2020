# OH GOD I WAY OVERDID THIS

import random


class Toboggan:
    def __init__(self, x, y, slope):
        self.location = [x, y]
        self.slope = slope
        self.trees = open('3.txt', 'r').read().splitlines()
        self.width = len(self.trees[0])
        self.length = len(self.trees)
        self.treeCount = 0

    def getCharAtCurrentLocation(self):
        return self.trees[self.location[0]][self.location[1]]

    def checkBottom(self):
        if self.location[0] >= self.length - 1:
            return True
        return False

    def checkTree(self):
        if self.checkBottom():
            pass
        if self.getCharAtCurrentLocation() == "#":
            self.treeCount += 1

    def slide(self, direction):
        for i in range(self.slope[0]):
            if direction == 'r':
                self.move('r')
            if direction == 'l':
                self.move('l')
        for i in range(self.slope[1]):
            self.move('d')

        self.checkTree()

    def move(self, direction):
        if (direction == "r"):
            self.location[1] += 1
        if (direction == "l"):
            self.location[1] -= 1
        if (direction == "u"):
            self.location[0] -= 1
        if (direction == "d"):
            self.location[0] += 1

        self.location[1] = self.location[1] % self.width  # deal with wrapping horizontally

        if self.checkBottom():
            return False
        return True

    def wheeee(self):
        while not (self.checkBottom()):
            self.slide('r')
        return self.treeCount


slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

num = 1
for slope in slopes:
    tob = Toboggan(0, 0, slope)
    trees = tob.wheeee()
    num *= trees
print(num)
