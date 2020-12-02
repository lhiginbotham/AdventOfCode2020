inp = []

with open('input.txt') as f:
	inp = [x for x in f.readlines()]

inp2 = [x.split(": ") for x in inp]

inp3 = [(x[0].split(" "), x[1].rstrip()) for x in inp2]

print(inp3)

valid = 0
for x in inp3:
	low, high = x[0][0].split("-")
	low = int(low)
	high = int(high)
	letter = x[0][1]
	count = 0
	for c in x[1]:
		if c == letter:
			count += 1
	if count >= low and count <= high:
		valid += 1

print(valid)