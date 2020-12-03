inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

print(inp)
treeCount = 0
curH = 0
for i in range(0, len(inp) - 1):
	curH = (curH + 3) % len(inp[0])
	if inp[i + 1][curH] == '#':
		treeCount += 1
print(treeCount)