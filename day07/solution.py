data = open("input.in", "r")
lines = [line.strip() for line in data.readlines()]

initialState = [int(x) for x in lines[0].split(',')]

def countToPos(x, initialState):
    counter = 0
    for i in initialState:
        counter += abs(i - x)

    return counter


minCounter = -1
for x in range(0, len(initialState)):
    v = countToPos(x, initialState.copy())

    if (minCounter == -1 or minCounter > v):
        minCounter = v

print("Part 1: ", minCounter)

def countToPos2(x, initialState):
    counter = 0
    for i in initialState:
        numbers = [n for n in range(0, abs(i - x))]
        for n in numbers:
            counter += (n + 1)

    return counter

minCounter = -1
for x in range(0, len(initialState.copy())):
    v = countToPos2(x, initialState.copy())

    if (minCounter == -1 or minCounter > v):
        minCounter = v

print("Part 2: ", str(minCounter))