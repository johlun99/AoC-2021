data = open("input.in", "r")
lines = [line.strip() for line in data.readlines()]

gammaBinary, epsilonBinary = "0b", "0b"

for i in range(0, len(lines[0])):
    count0, count1 = 0, 0

    for x in range(0, len(lines)):
        if (lines[x][i] == "0"):
            count0 += 1
        elif(lines[x][i] == "1"):
            count1 += 1
        
    mostCommon, leastCommon = "", ""
    if (count1 > count0):
        gammaBinary += "1"
        epsilonBinary += "0"
    else:
        gammaBinary += "0"
        epsilonBinary += "1"

res = int(gammaBinary, 2) * int(epsilonBinary, 2)

print("Part 1 ", str(res))

def findValues(arr, pos, common):
    count0, count1 = 0, 0

    for line in arr:
        if (line[pos] == '0'):
            count0 += 1
        elif (line[pos] == '1'):
            count1 += 1
    
    if (count0 > count1 and common == True):
        return 0

    elif (count1 > count0 and common == True):
        return 1
    
    if (count0 > count1 and common == False):
        return 1

    if (count0 > count1 and common == False):
        return 0
    
    return 0

def getAllValues(arr, pos, val, keep):
    myArr = []

    if (len(arr) == 2):
        if (arr[0][pos] == str(keep)):
            return arr[0]
        return arr[1]

    for line in arr:
        if (line[pos] == str(val)):
            myArr.append(line)

    return myArr

def oxygenRating(lines):
    index = 0
    while (len(lines) > 1):
        common = findValues(lines, index, True)
        lines = getAllValues(lines, index, common, 1)
        index += 1

        if (isinstance(lines, list) == False):
            return lines


def co2Rating(lines):
    index = 0
    while (len(lines) > 1):
        common = findValues(lines, index, False)
        lines = getAllValues(lines, index, common, 0)
        index += 1

        if (isinstance(lines, list) == False):
            return lines


res = int('0b' + oxygenRating(lines), 2) * int('0b' + co2Rating(lines), 2)
print("Part 2 ", str(res))