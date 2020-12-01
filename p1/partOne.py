expenseLines = []

with open('input.txt') as f:
	expenseLines = [int(x) for x in f.readlines()]


for x in range(len(expenseLines) - 1):
	for y in range(x + 1, len(expenseLines)):
		if expenseLines[x] + expenseLines[y] == 2020:
			print(expenseLines[x] * expenseLines[y])