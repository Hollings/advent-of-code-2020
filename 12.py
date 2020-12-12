class Ship:
    def __init__(self):
        self.facing = 0 # directionValues east
        self.pos = [1, 10]
        self.shipPos = [0,0]

    def manhattanDist(self):
        return abs(self.shipPos[0]) + abs(self.shipPos[1])

    def forward(self, value):
        # part 1:
        # self.pos = [self.shipPos[0] + directionValues[self.facing][0] * value, self.shipPos[1] + directionValues[self.facing][1] * value]

        movementAmount = [self.pos[0] * value,
                          self.pos[1] * value]
        self.shipPos = [self.shipPos[0] + (movementAmount[0]), self.shipPos[1] + (movementAmount[1])]

    def turn(self, dir, value):
        # part 1
        # if dir == "L":
        #     facing = self.facing - (value / 90);
        # if dir == "R":
        #     facing = self.facing + (value / 90);
        # self.facing = int((facing % 4))

        # part 2
        for i in range(int(value / 90)):
            if dir == "R":
                self.pos = [self.pos[1] * -1, self.pos[0]]
            if dir == "L":
                self.pos = [self.pos[1], self.pos[0] * -1]


    def info(self):
        print(f"FACING: {self.facing}")
        print(f"POSITION: {self.pos}")
        print(f"SHIP POSITION: {self.shipPos}")
        print("---")

    def parseInput(self, inp):
        print(inp)
        command = inp[0]
        value = int(inp[1:])
        cardinalDirections = "ENWS"
        if command in cardinalDirections:
            movement = directionValues[cardinalDirections.index(command)]
            self.pos = [self.pos[0] + movement[0] * value,
                        self.pos[1] + movement[1] * value]
        if command in "RL":
            self.turn(command, value)
        if command == "F":
            self.forward(value)
inp = open('12.txt', 'r').read().splitlines()

# turn inputs are only 90 degree increments
directionValues = [
   [0, 1],   # e
   [1, 0],  # n
   [0, -1],  # w
   [-1, 0]  # s
]

s = Ship()
s.info()
for val in inp:
    s.parseInput(val)
    s.info()

print(s.pos)
print(s.shipPos)
print(s.manhattanDist())