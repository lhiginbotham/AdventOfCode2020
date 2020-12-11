inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = int(inp[i].rstrip())

inp.sort()
target = 3 + inp[-1] 
inp = [0] + inp + [target]

valToIndex = dict()
for i in range(0, len(inp)):
    valToIndex[inp[i]] = i

ways = [1]
for i in range(1, len(inp)):
    waysToMe = 0
    prevIdxThatLeadToMe = [valToIndex[x] for x in inp if (inp[i] - x <= 3 and inp[i] - x > 0)]
    for prevNodeIdx in prevIdxThatLeadToMe:
        waysToMe += ways[prevNodeIdx]
    ways.append(waysToMe)

print(ways[-1])