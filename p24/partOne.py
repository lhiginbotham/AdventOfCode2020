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
for k in tilemap:
    print(k)
    if tilemap[k] % 2 == 1:
        black += 1
print(black)