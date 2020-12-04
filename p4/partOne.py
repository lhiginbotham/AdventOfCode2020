inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

pports = []
pport = None
for x in inp:
	if len(x) < 3:
		pports.append(pport)
		pport = None
	else:
		if pport == None:
			pport = dict()
		fields = x.split(" ")
		print(fields)
		for y in fields:
			f, v = y.split(':')
			pport[f] = v

print(pports)

if pport is not None:
	pports.append(pport)
	pport = None

valid = 0
a = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
for pp in pports:
	isvalid = True
	for f in a:
		if f not in pp and f != 'cid':
			isvalid = False
			break
	if isvalid:
		valid += 1

print(valid)