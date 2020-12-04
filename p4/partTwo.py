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
			print((f, v))
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
		else:
			if f == 'byr' and not (len(pp[f]) == 4 and pp[f].isnumeric() and int(pp[f]) >= 1920 and int(pp[f]) <= 2002):
				isvalid = False
				break
			elif f == 'iyr' and not (len(pp[f]) == 4 and pp[f].isnumeric() and int(pp[f]) >= 2010 and int(pp[f]) <= 2020):
				isvalid = False
				break
			elif f == 'eyr' and not (len(pp[f]) == 4 and pp[f].isnumeric() and int(pp[f]) >= 2020 and int(pp[f]) <= 2030):
				isvalid = False
				break
			elif f == 'hgt':
				unit = pp[f][len(pp[f]) - 2 : ]
				val = pp[f][0 : len(pp[f]) - 2]
				if not (unit == 'cm' and val.isnumeric() and int(val) >= 150 and int(val) <= 193) and not (unit == 'in' and val.isnumeric() and int(val) >= 59 and int(val) <= 76):
					isvalid = False
					break
			elif f == 'hcl':
				print("yodel " + str(len(pp[f])))
				if len(pp[f]) != 7:
					print("ah")
					isvalid = False
					break
				
				if pp[f][0] != '#':
					isvalid = False
					break
				id = pp[f][1:]
				match = 0
				for c in id:
					if c in 'abcdef0123456789':
						match += 1
				if match != 6:
					isvalid = False
					break
			elif f == 'ecl':
				if len(pp[f]) != 3 or (pp[f] not in ['amb','blu','brn','gry','grn','hzl','oth']):
					isvalid = False
					break
			elif f == 'pid':
				if len(pp[f]) != 9:
					isvalid = False
					break
				for c in pp[f]:
					if c not in '0123456789':
						isvalid = False
						break
			#elif f == 'cid':
			#	pass

	if isvalid:
		valid += 1

print(valid)