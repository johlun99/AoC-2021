with open("input.in") as file:
	file = file.read()

def parse(s):
	a, b = s.split(" | ")
	return a.split(" "), b.split(" ")

data = list(map(parse, file.split("\n")))

out = 0

for x, y in data:
	for d in y:
		if len(d) in [2, 4, 3, 7]:
			out += 1

print("part 1:", out)

def normalize(s):
	return "".join(sorted(s))

def is_in(x, y):
	return all(q in y for q in x)

def shared(x, y):
	count = 0
	for q in x:
		if q in y:
			count += 1
	return count

def derive_map(digits):
	digits = [normalize(x) for x in digits]

	d1 = next(x for x in digits if len(x) == 2)
	d4 = next(x for x in digits if len(x) == 4)
	d7 = next(x for x in digits if len(x) == 3)
	d8 = next(x for x in digits if len(x) == 7)
	d9 = next(x for x in digits if len(x) == 6 if is_in(d4, x))
	d3 = next(x for x in digits if len(x) == 5 if is_in(d1, x))
	d0 = next(x for x in digits if len(x) == 6 if x != d9 and shared(d1, x) == 2)
	d6 = next(x for x in digits if len(x) == 6 if x != d9 and x != d0)
	d5 = next(x for x in digits if len(x) == 5 if is_in(x, d6))
	d2 = next(x for x in digits if len(x) == 5 if x != d5 if x != d3)

	return {
		d0: "0",
		d1: "1",
		d2: "2",
		d3: "3",
		d4: "4",
		d5: "5",
		d6: "6",
		d7: "7",
		d8: "8",
		d9: "9",
	}

out = 0

for x, y in data:
	map = derive_map(x)
	out += int("".join(map[normalize(d)] for d in y))

print("part 2:", out)