# This is just part 2

adapters = [0]
for line in open('10.txt', 'r').read().splitlines():
    adapters.append(int(line))
adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)
changes = []

# array of differences for each
for i in range(len(adapters)):
    if i == 0:
        continue
    changes.append(adapters[i] - adapters[i-1])
print(changes)

# split into groups of contiguous 1s
groups = []
trib = [1,1,2,4,7]
group = 0
answer = 1
for i in range(len(changes)):
    if changes[i] == 1:
        group+=1
    else:
        groups.append(group)
        answer *= trib[group]
        group = 0
print(answer)