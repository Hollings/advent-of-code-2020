import copy

data = open('17.txt').read().splitlines()


# Test data

# data = """.#.
# ..#
# ###""".splitlines()


class Cube:
    def __init__(self, x, y, z, w, active):
        self.location = [x, y, z, w]
        self.active = active
        self.activeNeighbors = 0

    def findNeighbors(self):
        neighbors = 0
        for x in range(self.x() - 1, self.x() + 2):
            for y in range(self.y() - 1, self.y() + 2):
                for z in range(self.z() - 1, self.z() + 2):
                    for w in range(self.w() - 1, self.w() + 2):

                        if x == self.x() and y == self.y() and z == self.z() and w == self.w():
                            continue
                        cube = getOrCreateCube(x, y, z, w)
                        if cube.active:
                            neighbors += 1
        self.activeNeighbors = neighbors

    def tick(self):
        if self.active and self.activeNeighbors not in [2, 3]:
            self.active = False
        if (not self.active) and self.activeNeighbors == 3:
            self.active = True

    def x(self):
        return self.location[0]

    def y(self):
        return self.location[1]

    def z(self):
        return self.location[2]

    def w(self):
        return self.location[3]

    def __str__(self):
        return f"{','.join(str(x) for x in self.location)} - {self.active}"

    def __repr__(self):
        return f"{self.active}"


def initCubes():
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "#":
                getOrCreateCube(x, y, 0, 0, True)
    for pos, cube in list(cubes.items()):
        cube.findNeighbors()


def getCubeAtLocation(x, y, z, w):
    if f"{x},{y},{z},{w}" in cubes.keys():
        return cubes[f"{x},{y},{z},{w}"]
    return False


def getOrCreateCube(x, y, z, w, default=False):
    cube = getCubeAtLocation(x, y, z, w)
    if not cube:
        cube = Cube(x, y, z, w, default)
        cubes[f"{x},{y},{z},{w}"] = cube
    return cube


def countActiveCubes():
    n = 0
    for pos, cube in cubes.items():
        if cube.active:
            n += 1
    return n


def tick():
    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
    for pos, cube in list(cubes.items()):
        cube.findNeighbors()
    cacheCubes = copy.deepcopy(cubes)
    for pos, cacheCube in cacheCubes.items():
        cacheCube.tick()
        cube = getCubeAtLocation(cacheCube.x(), cacheCube.y(), cacheCube.z(), cacheCube.w())
        cube.active = cacheCube.active


cubes = {}
initCubes()
print(cubes)
print("----")
for i in range(6):
    tick()
    print(countActiveCubes())
