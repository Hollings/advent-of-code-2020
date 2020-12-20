import re

data = open('20.txt').read().split("\n\n")


class Tile:
    def __init__(self, tile: list, id):
        self.tile = tile
        self.borders = []
        self.id = id
        self.matchedBorders = 0

        # [U D R L]
        self.setupBorders()
        print(self.borders)

    def setupBorders(self):

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
                if self.id == '2311' and tile.id in ['1951', '1427', '3079']:
                    print(f"Checking if {tile} attaches to {self} index {p}")
                    if tile.id == '3079':
                        print(tile.borders)
                        print(self.borders)
                if tile == self:
                    continue
                for i in range(len(tile.borders)):
                    if i >= 2:
                        checkBorder = tile.borders[i][::-1]
                    else:
                        checkBorder = tile.borders[i]

                    if checkBorder == self.borders[p]:
                        print("MATCHED")
                        print(f"{tile.id} - {checkBorder} ===== {self.borders[p]}")

                        self.matchedBorders += 1
                        self.borders[p] = tile.id
                    #     found = True
                    #     matchedBorders.append( tile.borders[i])
                    #     # print(matchedBorders)
                    #     # print(f"{tile.id} - { tile.borders[i]} ===== {self.borders[p]}")
                    #     tile.borders[i] = self.id
                    #     self.borders[p] = tile.id
        # print(self.matchedBorders)

        # print(len(matchedBorders))



#       ##.#.#....
#       ..##...#..
#       .##..##...e
#       ..#...#...
#       #####...#.
#       #..#.#.#.#
#       ...#.#.#..
#       ##.#...##.
#       ..##.##.##
#       ###.##.#..


tiles = []
for tString in data:
    tString = tString.splitlines()
    id = tString[0].split(" ")[1][:-1]
    values = tString[1:]
    tiles.append(Tile(values, id))
#
tiles[0].findBorders()
# for tile in tiles:
#     print(tile.borders)
#     tile.findBorders()
#
# for tile in tiles:
#     print(f"{tile.id} - {tile.borders}")
# any tile that has two borders left after connecting them all must be the corner
