data = open("input.in", "r")
lines = [line.strip() for line in data.readlines()]

x, y = 0, 0

for line in lines:
    direction, steps = line.split(" ")

    if (direction == "forward"):
        x += int(steps)
    elif (direction == "down"):
        y += int(steps)
    elif (direction == "up"):
        y -= int(steps)

print("part1: ", (x * y))

x, y, aim = 0, 0, 0

for line in lines:
    direction, steps = line.split(" ")

    if (direction == "forward"):
        x += int(steps)
        y += (aim * int(steps))
    elif (direction == "down"):
        aim += int(steps)
    elif (direction == "up"):
        aim -= int(steps)

print("part 2 ", (x * y))
