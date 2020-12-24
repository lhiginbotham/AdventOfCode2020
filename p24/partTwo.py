import copy

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

tilemap = dict()
#ref = (0,0)

for line in inp:
    print(line)
    tilePos = [0,0]
    prefixDir = ''
    for c in line:
        if c == 'e':
            if len(prefixDir) == 0:
                tilePos[0] += 10
            else:
                tilePos[0] += 5
                prefixDir = ''
        elif c == 'w':
            if len(prefixDir) == 0:
                tilePos[0] -= 10
            else:
                tilePos[0] -= 5
                prefixDir = ''
        elif c == 'n':
            tilePos[1] += 10
            prefixDir = 'n'
        else:
            tilePos[1] -= 10
            prefixDir = 's'
    if (tilePos[0], tilePos[1]) not in tilemap:
        tilemap[(tilePos[0], tilePos[1])] = 0
    tilemap[(tilePos[0], tilePos[1])] += 1

black = 0

minX = 0
maxX = 0
minY = 0
maxY = 0
for k in tilemap:
    if k[0] < minX:
        minX = k[0]
    if k[0] > maxX:
        maxX = k[0]
    if k[1] < minY:
        minY = k[1]
    if k[1] > maxY:
        maxY = k[1]
    if tilemap[k] % 2 == 1:
        black += 1
        
def countBlack():
    b = 0
    for k in tilemap:
        if tilemap[k] % 2 == 1:
            b += 1
    return b

def getMinMax():
    global minX, maxX, minY, maxY
    for k in tilemap:
        if k[0] < minX:
            minX = k[0]
        if k[0] > maxX:
            maxX = k[0]
        if k[1] < minY:
            minY = k[1]
        if k[1] > maxY:
            maxY = k[1]
    if (minX // 10 * 10 != minX):
        minX = minX // 10 * 10
    if (minY // 10 * 10 != minY):
        minY = minY // 10 * 10
    if (maxX // 10 * 10 != maxX):
        maxX = (maxX // 10 + 1) * 10
    if (maxY // 10 * 10 != maxY):
        maxY = (maxY // 10 + 1) * 10

def countAdjBlackWhite(loc):
    positions = []
    positions.append([loc[0] - 5, loc[1] + 10])
    positions.append([loc[0] + 5, loc[1] + 10])
    positions.append([loc[0] - 10, loc[1]])
    positions.append([loc[0] + 10, loc[1]])
    positions.append([loc[0] - 5, loc[1] - 10])
    positions.append([loc[0] + 5, loc[1] - 10])
    adjBlack = 0
    adjWhite = 0
    for pos in positions:
        if (pos[0], pos[1]) in tilemap and tilemap[(pos[0], pos[1])] % 2 == 1:
            adjBlack += 1
        else:
            adjWhite += 1
    return (adjBlack, adjWhite)

for i in range(100):
    #print(tilemap)
    copymap = copy.deepcopy(tilemap)
    for y in range(minY - 10, maxY + 20, 10):
        for _x in range(minX - 30, maxX + 30, 10):
            x = _x
            if int(abs(y) // 10) % 2 == 1:
            #    print(y)
             #   print('aaaaaaaa')
                x -= 5
            cntbw = countAdjBlackWhite((x, y))
            #print(str((x,y)) + ' cntbw = ' + str(cntbw))
            if (x, y) not in tilemap or tilemap[(x, y)] % 2 == 0:
                # white
                if cntbw[0] == 2:
                    copymap[(x, y)] = 1
            else:
                # black
                if cntbw[0] == 0 or cntbw[0] > 2:
                    copymap[(x, y)] = 0
    tilemap = copymap
    getMinMax()
    if i < 6 or i > 95:
        print(str(i) + ": count " + str(countBlack()))