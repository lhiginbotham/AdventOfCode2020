inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

print(inp)
def a(r, d):
	treeCount = 0
	curH = 0
	for i in range(0, len(inp) - 1, d):
		curH = (curH + r) % len(inp[0])
		if inp[i + d][curH] == '#':
			treeCount += 1
	return treeCount

ans = 1
ans *= a(1, 1)
ans *= a(3, 1)
ans *= a(5, 1)
ans *= a(7, 1)
ans *= a(1, 2)
print(ans)