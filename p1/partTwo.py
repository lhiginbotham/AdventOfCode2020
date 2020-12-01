expenseLines = []

with open('input.txt') as f:
	expenseLines = [int(x) for x in f.readlines()]


for x in range(len(expenseLines) - 2):
	for y in range(x + 1, len(expenseLines) - 1):
		for z in range(y + 1, len(expenseLines)):
			if expenseLines[x] + expenseLines[y] + expenseLines[z] == 2020:
				print(expenseLines[x] * expenseLines[y] * expenseLines[z])