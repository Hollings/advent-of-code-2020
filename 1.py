dataset = open('1.txt', 'r').readlines()

for datum in dataset:
    for datum2 in dataset:
        for datum3 in dataset:
            if int(datum)+int(datum2)+int(datum3) == 2020:
                print(int(datum) * int(datum2) * int(datum3))