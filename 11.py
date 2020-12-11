import os


class Position:
    def __init__(self, pos):
        self.pos = pos

    def checkDir(self, dir):
        checkPos = [self.pos[0], self.pos[1]]

        while True:
            checkPos = [checkPos[0] + dir[0], checkPos[1] + dir[1]]
            # print(f"CHECKING {checkPos}")

            if checkPos[0] < 0:
                return False
            if checkPos[0] > len(map) - 1:
                return False
            if checkPos[1] < 0:
                return False
            if checkPos[1] > len(map[1]) - 1:
                return False
            if checkPos[0] == self.pos[0] and checkPos[1] == self.pos[1]:
                return False

            chp = Position(checkPos)
            c = chp.current()
            # print(c)
            if c == "#" or c == "L":
                return c
        return False

    def seenPositions(self):

        seen = False
        adj = {
            "L": 0,
            "#": 0,
            ".": 0
        }

        for i in range(-1,2):
            for q in range(-1,2):
                # print(f"DIRECTION {i} {q}")
                if i == 0 and q == 0:
                    continue
                seen = self.checkDir([i,q])
                if seen:
                    adj[seen] += 1
        # print(adj)
        return adj




    def adjPositions(self):
        # print(f"current pos {self.pos[0]} {self.pos[1]}")
        # start searching one square up and left, then check three right three down for all 9 adjacent
        adj = {
            "L" : 0,
            "#" : 0,
            "." : 0
        }
        checkPos = [self.pos[0] - 1, self.pos[1] -1]
        for x in range(3):
            for y in range(3):
                if checkPos[0] + x < 0:
                    continue
                if checkPos[0] + x > len(map) -1:
                    continue
                if checkPos[1] + y < 0:
                    continue
                if checkPos[1] + y > len(map[1]) -1:
                    continue
                if checkPos[0] + x == self.pos[0] and checkPos[1] + y  == self.pos[1]:
                    continue

                pos = Position([checkPos[0] + x, checkPos[1] + y])
                adj[pos.current()] += 1
        return adj

    def current(self):
        # print(self.pos)
        # print(self.pos)
        # print(self.pos)
        # print(map)
        return map[self.pos[0]][self.pos[1]]

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# # Otherwise, the seat's state does not change.
#
map = open('11.txt', 'r').read().splitlines()
print(map)
# p = Position([4,3])
# print(p.seenPositions())
#
#
# # PART 2
#
# exit()
# PART 1
# -----------------
print("\n".join(map))
print("---")
w, h = len(map[0]), len(map)
lastMap = []
changed = True
while changed:
    changed = False
    newMap = []
    for row in range(len(map)):
        newRow = []
        for col in range(len(map[0])):
            tile = Position([row,col])
            curr = tile.current()
            ####### PART 1
            # adj = tile.adjPositions()
            ###### PART 2
            adj = tile.seenPositions()
            ######
            if curr == "L" and adj['#'] == 0:
                newRow.append("#")
                changed = True
            elif curr == "#" and adj['#'] >= 5:
                newRow.append("L")
                changed = True
            else:
                newRow.append(curr)
        newMap.append("".join(newRow))
    os.system('cls')
    # print("\n".join(newMap))
    map = newMap[:]
    lastMap = map[:]

# Count Ls
countOccu = 0
for col in map:
    for row in col:
        if row == "#":
            countOccu += 1
print(countOccu)
# ---------------------------

