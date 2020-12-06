inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

totalCount = 0
currSet = set()
for i in range(0, len(inp)):
	ans = inp[i]
	if len(ans):
		for c in ans:
			currSet.add(c)
	else:
		totalCount += len(currSet)
		currSet = set()

totalCount += len(currSet)

print(totalCount)