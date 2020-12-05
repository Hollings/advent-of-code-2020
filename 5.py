# Little cleaner today but i probably could do with less duplicated code for col/row

dataset = open('5.txt', 'r').read().splitlines()
import math

class BinaryBoarding:
    def __init__(self, code):
        self.code = code
        self.rows = [0, 127]
        self.cols = [0, 7]
        # print(self.code)

    def newRows(self, dir):
        if dir == "F":
            self.rows[1] = math.floor((self.rows[1] + self.rows[0]) / 2)
        if dir == "B":
            self.rows[0] = math.ceil((self.rows[1] + self.rows[0]) / 2)
        # print(self.rows)

    def newCols(self, dir):
        if dir == "L":
            self.cols[1] = math.floor((self.cols[1] + self.cols[0]) / 2)
        if dir == "R":
            self.cols[0] = math.ceil((self.cols[1] + self.cols[0]) / 2)
        # print(self.cols)

    def findRow(self):
        for char in self.code:
            if char in ['L', 'R']:
                return True
            self.newRows(char)

    def findCol(self):
        for char in self.code[-3:]:
            self.newCols(char)

    def getSeatId(self):
        self.findRow()
        self.findCol()
        return (self.rows[0] * 8) + self.cols[0]


# part 1
highest = 0
seats = []
for row in dataset:
    b = BinaryBoarding(row)
    id = b.getSeatId()
    seats.append(id)
    if id > highest:
        highest = id
print("Highest Seat ID: " + str(highest))

# part 2
seats.sort()
for i in range(0,len(seats)):
    if seats[i] - seats[i-1] == 2:
        print("Your Seat: " + (str(seats[i] - 1)))


