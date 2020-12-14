from math import gcd

data = open('13.txt').read().splitlines()
# data = ["939", "17,x,13,19"]


# Second day of attempting this...
########
########
########
def lcm(a, b):
    return a * b / gcd(a, b)

busData = data[1].split(",")
busPosVals = {}

for b in busData:
    # part 1
    # if b != "x":
    if b.isnumeric():
        busPosVals[int(busData.index(b))] = int(b)

print(busPosVals)
position, currentTime = 1, 0
for busId, busTime in busPosVals.items():
    print(f"{busId}, {busTime}")
    while True:
        if (busId + currentTime) % busTime == 0: break
        print(f"{currentTime} {position}")
        currentTime += position
    position *= busTime
print('Part 2:', currentTime)

exit()
########
########
########


# 54
earliestDepart = int(data[0])
latestBus = 0
buses = []
for b in data[1].split(","):
    # part 1
    # if b != "x":
    if b.isdecimal() and int(b) > latestBus:
        buses.append(b)
        latestBus = int(b)

busNums = []
i = 0
for bus in buses:
    if bus.isnumeric():
        busNums.append(int(bus) + i)
    i += 1

print(busNums)

print(lcm(busNums))
# print(lcm(busNums) / 2)


# 3,5,7    -> 54   (108) -> LCM 105
# 3 5 7 13 -> 894 (1365) -> 1365


1 * 1
2 * 1


# 1,2 -> 1
# 1,5 -> 4
# 1,10 -> 9
# 1,x,10 -> 8
# 2,3,4 -> 2


# buses = sorted(buses)
# print(latestBus)
# print(buses)

# PART 1
# def findEarliestBus():
#     i = earliestDepart
#     while True:
#         for bus in buses:
#             if i % bus == 0:
#                 return ((i - earliestDepart) * bus)
#         i+=1
# print(findEarliestBus())


# part 2
def part2():
    time = 0
    found = False
    while time < 999999999999 and not found:
        # print("--------")
        # print(time)
        b = 0
        found = True
        for i in range(time, time + len(buses)):
            # print(f"Checking if {i} % {buses[b]} is 0")
            if buses[b] == 'x' or (buses[b].isnumeric() and i % int(buses[b])) == 0:
                # print(buses[b])
                pass
            else:
                # print("NO " + str(buses[b]))
                found = False
            b += 1
        time += 1
    print(time - 1)


part2()
