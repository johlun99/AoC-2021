data = open("../inputs/day01.txt", "r")
lines = [int(line.strip()) for line in data.readlines()]

counter = 0
for i in range(0, len(lines) - 1):
    if (lines[i] < lines[i + 1]):
        counter += 1

print("Part1: " + str(counter))

counter = 0
for i in range(0, len(lines) - 3):
    a = lines[i] + lines[i + 1] + lines[i + 2]
    b = lines[i + 1] + lines[i + 2] + lines[i + 3]

    if (a < b):
        counter += 1

print("Part 2: " + str(counter))