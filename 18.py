data = open('18.txt').read().splitlines()

def calculatePart1(line: str):
    line = line.split(" ")
    answer = int(line[0])
    for i in list(range(1, len(line)))[::2]:
        val = int(line[i + 1])
        if line[i] == '+':
            answer += val
        if line[i] == '*':
            answer *= val
        i += 1
    return answer

def calculatePart2(line: str):
    for op in ["+", "*"]:
        while op in line:
            lineArr = line.split(" ")
            for i in range(len(lineArr)):
                if lineArr[i] == op:
                    if op == "+":
                        calculated = int(lineArr[i-1]) + int(lineArr[i+1])
                    else:
                        calculated = int(lineArr[i-1]) * int(lineArr[i+1])
                    line = line.replace(f"{lineArr[i-1]} {op} {lineArr[i+1]}", str(calculated), 1)
                    break
    return line

def splitParenPart1(line):
    string = ""
    firstParen = line.find("(") + 1
    for char in line[firstParen:]:
        if char == "(":
            string = ""
            continue
        if char == ")":
            line = line.replace("(" + string + ")", str(calculatePart1(string)))
            return line
        string += char

def splitParenPart2(line):
    p = 0
    string = ""
    firstParen = line.find("(") + 1
    for char in line[firstParen:]:
        if char == "(":
            string = ""
            continue
        if char == ")":
            line = line.replace("(" + string + ")", str(calculatePart2(string)), 1)
            return line
        string += char

answer1 = 0
for line in data:
    while "(" in line:
        line = splitParenPart1(line)
    answer1 += calculatePart1(line)

answer2 = 0
for line in data:
    while "(" in line:
        line = splitParenPart2(line)

    # calculate each parenthesis until there are no more left
    while "(" in line:
        line = splitParenPart2(line)

    # calculate the last one
    ans = calculatePart2(line)
    answer2 += int(ans)

print(f"PART 1 {answer1}")
print(f"PART 1 {answer2}")