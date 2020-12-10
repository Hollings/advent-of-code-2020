# ABANDON ALL HOPE
# ABANDON ALL HOPE
# ABANDON ALL HOPE
# ABANDON ALL HOPE
# ABANDON ALL HOPE
# ABANDON ALL HOPE

def getValidAdapters(current):
    returnVal = []
    for adapter in adapters:
        # print(f"{current} - {adapter}")
        if adapter <= current + 3 and adapter > current:
            returnVal.append(adapter)
    return returnVal


def getAdapterTree(current, total):
    valid = getValidAdapters(current)

    for x in valid:
        if x == adapters[-1]:
            total += 1
            # print("YEE" + str(total))
        else:
            total = getAdapterTree(x, total)
    return total


import time

start = time.time()
adapters = [0]
for line in open('10.txt', 'r').read().splitlines():
    adapters.append(int(line))
adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)
differences = {}
print(adapters)
# print(getValidAdapters(0))
total = 0
print(adapters[-1])
print("runniung")
# print(getAdapterTree(0, 0))
# print("TIME: " + str(time.time()-start))
# print(total)


# part 1
changes = []
for i in range(len(adapters)):
    if i == 0:
        continue
    if adapters[i] <= adapters[i - 1] + 3:
        change = (adapters[i] - adapters[i - 1])
        print(str(change))
        changes.append(change)
        if change in differences.keys():
            differences[change] += 1
        else:
            differences[change] = 1

print(differences)
lastnum = 0
print("----")
answer = 1
import math

# print(changes)
power = 0
n = 0
answer = 0
# while n < len(changes):
#     print(changes[n])
#     if changes[n] == 1:
#         i = 0
#         while changes[n+i] == 1:
#             i+=1
#         n+=i
#         print("I = " + str(i))
#         answer += math.factorial(i)
#     n+=1

seen = {}
for a in adapters:

    poss = getValidAdapters(a)
    if len(poss) > 1:
        seen[a] = poss
total = 0
#
# def recCountNodes(current, tot):
#     tot += len(seen[current])
#     for item in seen[current]:
#         recCo
# for key, val in seen.items():
#     total += len(val)
# print(total + 1)
# # print(power)
# # print(pow(2, power))
# print(answer)

import collections

count = collections.defaultdict(int)

# store array where each index is a count of the previous three
# to be honest i have no idea whats going on here, i just used hints from reddit
arrange = [1] + [0] * adapters[-1]
for i in adapters[1:]:
    arrange[i] = arrange[i - 3] + arrange[i - 2] + arrange[i - 1]
print(arrange[-1])
