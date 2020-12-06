inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

totalCount = 0
currGroupMemberCount = 0
currSet = dict()
for i in range(0, len(inp)):
	ans = inp[i]
	if len(ans):
		currGroupMemberCount += 1
		for c in ans:
			if c in currSet:
				currSet[c] += 1
			else:
				currSet[c] = 1
	else:
		groupTotalAgreementCount = 0
		for k in currSet.keys():
			if currSet[k] == currGroupMemberCount:
				groupTotalAgreementCount += 1
		totalCount += groupTotalAgreementCount
		currSet = dict()
		currGroupMemberCount = 0

groupTotalAgreementCount = 0
for k in currSet.keys():
	if currSet[k] == currGroupMemberCount:
		groupTotalAgreementCount += 1
totalCount += groupTotalAgreementCount

print(totalCount)