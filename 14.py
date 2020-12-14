# testData
data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".splitlines()

# real data
data = open('14.txt').read().splitlines()


def applyMaskPart1(mem, mask):
    """
    Replaces mask "X"s with digits
    :param mem:
    :param mask:
    :return:
    """
    memBinary = padZeroes(decToBin(mem), len(mask))
    newValue = ""
    for i in range(len(memBinary)):
        if mask[i] != 'X':
            newValue += mask[i]
        else:
            newValue += memBinary[i]
    return newValue


def applyMask(mem, mask):
    """
    Replaces mask "X"s with digits

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.

    :param mem:
    :param mask:
    :return:
    """
    memBinary = padZeroes(decToBin(mem), len(mask))

    newValue = ""
    for i in range(len(memBinary)):
        if mask[i] == '1':
            newValue += mask[i]
        elif mask[i] == '0':
            newValue += memBinary[i]
        else:
            newValue += "X"
    return newValue


def decToBin(num):
    return "{0:b}".format(int(num))


def binToDec(bin):
    return int(bin, 2)


def padZeroes(str, length):
    return ("0" * (length - len(str))) + str


def sumValues(dict):
    s = 0
    for val in dict.values():
        s += val
    return s


def getPermutedValues(data, value, mem):
    floating_bit_count = data.count('X')

    # Counting up in binary is an easy way to find all permutations of 0 and 1
    i = 0
    while i <= binToDec('1' * floating_bit_count):
        variation = str(padZeroes(decToBin(i), floating_bit_count))
        final_mem = ""
        m = 0
        # For each character of the mask string, replace each X with the next value in the binary
        for y in range(len(data)):
            if data[y] == "X":
                final_mem += variation[m]
                m += 1
            else:
                final_mem += data[y]
        mem[binToDec(final_mem)] = value
        i += 1
    return mem


savedMem = {}
for line in data:
    line = line.split(" = ")
    if line[0] == 'mask':
        mask = line[1]
    else:
        # Part 1
        # savedMem[line[0][4:-1]] = binToDec(applyMaskPart1(line[1], mask))

        # Part 2
        baseMem = line[0][4:-1]
        savedMem = getPermutedValues(applyMask(baseMem, mask), int(line[1]), savedMem)

print(sumValues(savedMem))
