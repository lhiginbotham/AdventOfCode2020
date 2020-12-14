inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(len(inp)):
		inp[i] = inp[i].rstrip().split(' = ')


mem = dict()
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

def applyMask2dot0To(loc):
	bStr = [c for c in bin(int(loc))[2:]]
	if len(bStr) < 36:
		for i in range(36 - len(bStr)):
			bStr.insert(0, '0')

	numFloatingLoc = 0
	for i in range(len(bStr)):
		m = mask[i]
		if m == 'X':
			bStr[i] = 'X'
			numFloatingLoc += 1
		elif m == '1':
			bStr[i] = '1'

	base = '0' * numFloatingLoc
	floatBStr = [c for c in base]
	locs = []
	for i in range(2 ** numFloatingLoc):
		bStrCopy = [x for x in bStr]
		floatPos = 0
		for i in range(len(bStrCopy)):
			if bStrCopy[i] == 'X':
				bStrCopy[i] = floatBStr[floatPos]
				floatPos += 1

		locStrBin = ''
		for c in bStrCopy:
			locStrBin += c

		locs.append(int(locStrBin, 2))
		base = bin(int(base, 2) + 1)[2:]
		if len(base) < numFloatingLoc:
			for i in range(numFloatingLoc - len(base)):
				base = '0' + base
		print('base')
		print(base)
		print('end base')
		floatBStr = [c for c in base]

	print("locs")
	print(locs)
	return locs

def putInMem(val, loc):
	locs = applyMask2dot0To(loc)
	for locIdx in locs:
		#if locIdx >= len(mem):
			#for i in range(locIdx - len(mem) + 1):
			#	mem.append('0')
		mem[locIdx] = val

for x in inp:
	print(x)
	if 'mask' in x[0]:
		mask = x[1]
	else:
		loc = x[0].split('mem[')[1].split(']')[0]
		val = x[1]
		putInMem(val, loc)

sum = 0
for key in mem.keys():
	print(type(mem[key]))
	sum += int(mem[key])

print(sum)