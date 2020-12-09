inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = int(inp[i].rstrip())

window = []

def sum_up(window):
	sum = 0
	for x in window:
		sum += x
	if sum == 466456641:
		a = [x for x in window]
		a.sort()
		print(a)
		print(a[0] + a[-1])
		return 0
	elif sum < 466456641:
		return -1
	else:
		return 1

left = 0
for x in range(0, len(inp)):
	for y in range(x + 1, len(inp)):
		sum_up([inp[i] for i in range(x, y + 1)])
