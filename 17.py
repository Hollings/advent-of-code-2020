import copy

data = open('17.txt').read()
data = """.#.
..#
###"""



# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
# .#.
# ..#
# ###
def checkNeighbors(z, y, x):
    neighbors = {
        '.':0,
        '#':0
    }
    for z2 in range(z - 1, z + 2):
        for y2 in range(y - 1, y + 2):
            # print(f"y2 {cubes[z2][y2]}")
            for x2 in range(x - 1, x + 2):
                if (z == z2 and y == y2 and x == x2) or z2 < 0 or y2 < 0 or x < 0 or z2 >= len(cubes) or y2 >= len(cubes[z2]) or x2 >= len(cubes[z2][y2]):
                    continue
                neighbors[cubes[z2][y2][x2]] += 1
    return neighbors


newCubes = copy.deepcopy(cubes)
for z in range(len(cubes)):
    print(cubes[z])
    for y in range(len(cubes[z])):
        for x in range(len(cubes[z][y])):
            # howdily doodily
            neighborinos = checkNeighbors(z, y, x)
            if cubes[z][y][x] == "#":
                if neighborinos['#'] not in [2,3]:
                    newCubes[z][y][x] = '.'
            if cubes[z][y][x] == "." and neighborinos['#'] == 3:
                newCubes[z][y][x] = '#'

for j in newCubes:
    for row2 in j:
        print(row2)
    print("----")
