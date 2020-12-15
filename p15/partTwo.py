inp = [0, 13, 1, 8, 6, 15]
# with open('input.txt') as f:
    # inp = f.readlines()
    # for i in range(len(inp)):
        # inp[i] = inp[i].rstrip()

lastTwoVisits = dict()
for i in range(len(inp)):
    lastTwoVisits[inp[i]] = [i]

while len(inp) < 30000001:
    searchNum = inp[-1]
    visits = lastTwoVisits[searchNum]
    if len(visits) < 2:
        lastTwoVisits[0].append(len(inp))
        if (len(lastTwoVisits[0]) > 2):
            lastTwoVisits[0].pop(0)
        inp.append(0)
    else:
        oldDist = visits[1] - visits[0]
        if (visits[1] - visits[0]) not in lastTwoVisits:
            lastTwoVisits[visits[1] - visits[0]] = []
        lastTwoVisits[visits[1] - visits[0]].append(len(inp))
        if (len(lastTwoVisits[visits[1] - visits[0]]) > 2):
            lastTwoVisits[visits[1] - visits[0]].pop(0)
        inp.append(oldDist)

print(inp[30000000 - 1])