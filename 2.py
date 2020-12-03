import re

data = open('2.txt', 'r').readlines()
# data = ["1-3 a: abcde",
# "1-3 b: cdefg",
# "2-9 c: ccccccccc"]
count = 0
for line in data:
    # print(line)
    rules = re.compile('(\d*)-(\d*) ([a-z]): ([a-z]*)')
    m = rules.search(line)
    nfrom = int(m.group(1))
    nto = int(m.group(2))
    letter = m.group(3)
    word = m.group(4)
    # print(word.count(letter))

    # Part 1:
    # if (word.count(letter) >= nfrom and word.count(letter) <= nto):
    #     print(line)
    #     count+=1
    try:
        if ((word[nfrom-1] == letter or word[nto-1] == letter) and (word[nfrom-1] != word[nto-1])):
            print(line)
            print(word[nfrom-1])
            print(word[nto-1])
            count+=1
    except:
        pass


print(count)