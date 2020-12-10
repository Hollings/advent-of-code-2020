import math

class Xmas():
    def __init__(self, data, preambleLength):
        self.preLen = preambleLength
        self.data = data
        print(self.data)

    def checkValue(self, index):
        checkNums = self.data[index-self.preLen:index]
        for z in range(self.preLen):
            for y in range(self.preLen):
                if y == z:
                    continue
                if checkNums[z] + checkNums[y] == self.data[index]:
                    return True

        return False

    def checkContig(self, sumFind):
        for z in range(len(self.data)):
            for y in range(z, len(self.data)):
                # print(self.data[z:y])
                # print(sumFind)
                if sum(self.data[z:y]) == sumFind:
                    answer = sorted(self.data[z:y])
                    return answer[0] + answer[-1]


data = []
for num in open('9.txt', 'r').read().splitlines():
    data.append(int(num))
prelen = 25
x = Xmas(data, prelen)
found = True
i = prelen
while found and i < len(data) -1:
    found = x.checkValue(i)
    if found:
        i+=1
part1 = x.data[i]
print(part1)
print("---")
print(x.checkContig(part1))

