inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = int(inp[i].rstrip())

preamb = 25
preambWin = [inp[x] for x in range(i, preamb)]

for i in range(preamb, len(inp)):
	sumFound = False
	for x in range(0, preamb - 1):
		for y in range(x + 1, preamb):
			if inp[i - preamb + x] + inp[i - preamb + y] == inp[i]:
				sumFound = True
	if not sumFound:
		print(inp[i])