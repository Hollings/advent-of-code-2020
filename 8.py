
# acc - increases 'acc' value. starts at 0
# jmp - jumps to an instruction relative to itself. e.g. +2 means skip the next one
# nop - no operation


class Console:
    def __init__(self):
        self.originalLines = open('8.txt', 'r').read().splitlines()
        self.lines = self.originalLines[:] # make a copy so we dont reload the file every time
        self.cursor = 0
        self.accumulator = 0
        self.linesRan = []
        self.finished = False

    def reset(self):
        self.lines = self.originalLines[:] # make a copy so we dont reload the file every time
        self.cursor = 0
        self.accumulator = 0
        self.linesRan = []
        self.finished = False

    def doInstruction(self):
        line = self.currentLine().split(" ")
        instruction = line[0]
        sign = line[1][0]
        amount = int(line[1][1:])

        self.linesRan.append(self.cursor)
        if sign == "-":
            amount *= -1

        if instruction == 'acc':
            self.accumulator += amount
            self.cursor += 1
        if instruction == 'jmp':
            self.cursor += amount
        if instruction == 'nop':
            self.cursor += 1

    def currentLine(self):
        return self.lines[self.cursor]

    def checkDupLine(self):
        if self.cursor in self.linesRan:
            return False
        return True

    def checkFinished(self):
        # print(cursor)
        if self.cursor >= len(self.lines):
            self.finished = True
            return True
        return False

    def flipNopJmp(self, i):

        found = False
        index = i
        for line in self.lines[i:]:
            if 'nop' in line:
                line = line.replace("nop", "jmp")
                found = True
                break
            if 'jmp' in line:
                line = line.replace("jmp", "nop")
                found = True
                break

        # meh could be cleaner
        if found:
            self.lines[index] = line
            return index
        index += 1

    def run(self):
        while self.checkDupLine() and not self.checkFinished():
            self.doInstruction()

# part 1
console = Console()
console.run()
print("PART 1 ANSWER: " + str(console.accumulator))

# part 2
currentFlip = 0
console = Console()

while True:
    currentFlip = console.flipNopJmp(currentFlip)
    console.run()
    if console.finished:
        break
    currentFlip += 1
    console.reset()

print("PART 2 ANSWER: " + str(console.accumulator))
