import re

data = open('20.txt').read().split("\n\n")


class Tile:
    def __init__(self, tile: list, id):
        self.tile = tile
        self.id = id
        self.matchedBorders = 0
        self.connections = [None, None, None, None]
        self.placed = False

        # [U D R L]
        self.setupBorders()

    def rotate(self):
        rotatedTile = list(zip(*self.tile[::-1]))
        for i in range(len(rotatedTile)):
            rotatedTile[i] = "".join(rotatedTile[i])
        self.tile = rotatedTile
        self.setupBorders()

    def setupBorders(self):
        self.borders = []

        for vert in [0, -1]:
            vertStr = ""

            for horiz in range(len(self.tile[0])):
                vertStr += self.tile[vert][horiz]
            self.borders.append(vertStr)

        for horiz in [0, -1]:
            horizStr = ""
            for vert in range(len(self.tile[0])):
                horizStr += self.tile[vert][horiz]
            self.borders.append(horizStr)

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.id

    # For every border of every tile
    def findBorders(self):
        # matchedBorders = []
        for p in range(len(self.borders)):
            for tile in tiles:
                if tile == self or tile.placed or tile.id in self.connections:
                    continue
                for i in range(4):
                    for b in range(len(tile.borders)):
                        if tile.borders[b] == self.borders[p]:
                            self.connections[p] = tile.id
                    tile.rotate()


tiles = []
for tString in data:
    tString = tString.splitlines()
    id = tString[0].split(" ")[1][:-1]
    values = tString[1:]
    tiles.append(Tile(values, id))

for tile in tiles:
    print(tile.id)
    print("\n".join(tile.tile))
    print("---")

for tile in tiles:
    # print(tile.id)
    # print(tile.borders)
    tile.findBorders()

print("====")
answer = 1
for tile in tiles:
    n = 0
    for connection in tile.connections:
        if connection:
            n+=1
    if n == 2:
        answer *= int(tile.id)
        print(f"{tile.id} - {tile.connections}")
# any tile that has two borders left after connecting them all must be the corner
print(answer)

def findTileById(id):
    print(f"finding {id}")
    for tile in tiles:
        if tile.id == str(id):
            return tile
# Join them

finalPhoto = ""
nextTile = findTileById(1951)
arr = [[]]
while nextTile:
    if nextTile.connections[3]:
        nextTile = findTileById(nextTile.connections[3])
        arr[-1].append(nextTile.id)

    else:
        # print(arr)
        nextTile = findTileById(findTileById(arr[-1][0]).connections[0])
        arr.append([nextTile.id])
    print(arr)
