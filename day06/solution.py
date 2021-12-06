from collections import Counter
import time

data = open("input.in", "r")
lines = [line.strip() for line in data.readlines()]
initialState = [int(i) for i in lines[0].split(',')]

def countFish(fish, days):
    c = Counter(fish)

    for day in range(days):
        temp = [c[i] for i in range(9)]
        c[8] = c[0]; temp[7] += c[0]
        for i,x in list(enumerate(temp))[1:]: c[i - 1] = x

    sum = c
    c = sum.values()
    value = 0
    for i in c:
        value += i

    return value

start1 = time.time()
print("Part 1: ", str(countFish(initialState, 80)))
end1 = time.time()

start2 = time.time()
print("Part 2: ", str(countFish(initialState, 256)))
end2 = time.time()

print("Exec 1: ", end1 - start1)
print("Exec 2: ", end2 - start2)