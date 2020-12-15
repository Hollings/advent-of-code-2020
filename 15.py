# real data
data = '1,20,8,12,0,14'.split(',')

# test data
# data = "0,3,6".split(',')

numbers = {}
for num in data:
    numbers[int(num)] = [int(data.index(num)) + 1]

print(numbers)

lastNumber = int(data[-1])
turnNumber = len(data) +1
while turnNumber <= 30000000:
    if len(numbers[lastNumber]) == 1:
        if 0 in numbers.keys():
            if len(numbers[0]) > 1:
                numbers[0].pop(0)
            numbers[0].append(turnNumber)
        else:
            numbers[0] = [turnNumber]
        lastNumber = 0
    else:
        lastTurns = numbers[lastNumber]
        diff = lastTurns[-1] - lastTurns[-2]
        if diff in numbers:
            if len(numbers[diff]) > 1:
                numbers[diff].pop(0)
            numbers[diff].append(turnNumber)
        else:
            numbers[diff] = [turnNumber]
        lastNumber = diff
    turnNumber += 1
print(lastNumber)
