inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()
sumList = 0
lowestSeatId = -1
highestSeatId = -1
for p in inp:
	low = 0
	high = 127
	for i in range(0, 6):
		inc = 2 ** (6 - i)
		if p[i] == 'F':
			high = high - inc
		else:
			low = low + inc

	print(str(low) + " " + str(high))
	rowN = low if p[6] == 'F' else high

	rlow = 0
	rhigh = 7
	for i in range(7, 9):
		inc = 2 ** (9 - i)
		print(inc)
		if p[i] == 'L':
			rhigh = rhigh - inc
		else:
			rlow = rlow + inc

	seatN = rlow if p[9] == 'L' else rhigh
	print(seatN)
	seatId = rowN * 8 + seatN
	sumList += seatId
	if highestSeatId  < seatId or highestSeatId == -1:
		highestSeatId = seatId
	if lowestSeatId > seatId or lowestSeatId == -1:
		lowestSeatId = seatId

sumTrue = 0
for i in range(lowestSeatId, highestSeatId + 1):
	sumTrue += i

print(sumTrue - sumList)