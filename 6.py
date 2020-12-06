# This code is trash. Going to record timestamps here because I'm trying to speedrun these
# 11:17 PM - 11:39 PM

dataset = open('6.txt', 'r').read()
groups = dataset.split("\n\n")

groupqcount = 0
answernum = 0
for i in range(len(groups)):
    count = len(groups[i].split("\n"))
    groups[i] = groups[i].replace("\n", "")
    print("GROUP: " + groups[i])
    answer = {}
    for letter in groups[i]:
        if letter in answer.keys():
            answer[letter] += 1
        else:
            answer[letter] = 1
    # print(sum(answer.values()))
    for key, value in answer.items():
        if value == count:
            answernum += 1
            print("sum " + str(answernum))


print(answernum)

# print(groupqcount)
# print(groups)
#
#
# answer = {}
# for group in groups:
#     for letter in group:
#         if letter in answer.keys():
#             answer[letter] += 1
#         else:
#             answer[letter] = 1
#
#
# print(len(answer.keys()))