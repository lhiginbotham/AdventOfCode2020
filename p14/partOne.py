inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(len(inp)):
		inp[i] = inp[i].rstrip().split(' = ')


mem = []
mask = 'X' * 36

def applyMaskTo(val):
	bStr = [c for c in bin(int(val))[2:]]
	if len(bStr) < 36:
		for i in range(36 - len(bStr)):
			bStr.insert(0, '0')
			
	for i in range(len(bStr)):
		m = mask[i]
		if m == 'X':
			continue
		else:
			bStr[i] = m

	recbStr = ''
	for c in bStr:
		recbStr += c
	return int(recbStr, 2)

def putInMem(val, loc):
	val = applyMaskTo(val)
	if int(loc) >= len(mem):
		for i in range(int(loc) - len(mem) + 1):
			mem.append('0')
	mem[int(loc)] = val
	
for x in inp:
	print(x)
	if 'mask' in x[0]:
		mask = x[1]
	else:
		loc = x[0].split('mem[')[1].split(']')[0]
		val = x[1]
		putInMem(val, loc)

sum = 0
for x in mem:
	print(x)
	sum += int(x)

print(sum)