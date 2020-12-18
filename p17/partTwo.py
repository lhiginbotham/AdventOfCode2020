import json

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

zPlane = []
zPlane.append([[[y for y in x] for x in inp]]) # encased the x-array in another array to simulate initial w plane

print(zPlane)

def countNeighbors(plane, z, w, x, y):
    count = 0
    points = []
    for _z in range(-1, 2):
        for _w in range(-1, 2):
            for _x in range(-1, 2):
                for _y in range(-1, 2):
                    points.append((z + _z, w + _w, x + _x, y + _y))
    for p in points:
        if p[0] == z and p[1] == w and p[2] == x and p[3] == y:
            continue
        if p[0] < 0 or p[0] >= len(plane) or p[1] < 0 or p[1] >= len(plane[p[0]]) or p[2] < 0 or p[2] >= len(plane[p[0]][p[1]]) or p[3] < 0 or p[3] >= len(plane[p[0]][p[1]][p[2]]):
            continue
        if plane[p[0]][p[1]][p[2]][p[3]] == '#':
            count += 1

    return count

iterCount = 6
for i in range(iterCount):
    # expand each dimension by 1 just in case we need it
    
    # print('-pre-expand-')
    # print(len(zPlane))
    # for z in zPlane:
        # print('  ' + str(len(z)))
        # for x in z:
            # print('    ' + str(len(x)))
            # print('      ', end='')
            # for y in x:
                # print(str(len(y)) + ' ', end='')
            # print()
    # print('-end-pre-expand-')
    
    for plane in zPlane:
        for w in plane:
            for x in w:
                x.insert(0, '.')
                x.append('.')
            
            yDim = len(w[0])
            w.insert(0, ['.' for y in range(yDim)])
            w.append(['.' for y in range(yDim)])
        xDim = len(plane[0])
        yDim = len(plane[0][0])
        plane.insert(0, [['.' for y in range(yDim)] for x in range(xDim)])
        plane.append([['.' for y in range(yDim)] for x in range(xDim)])

    wDim = len(zPlane[0])
    xDim = len(zPlane[0][0])
    yDim = len(zPlane[0][0][0])
    
    zPlane.insert(0, [[['.' for y in range(yDim)] for x in range(xDim)]for w in range(wDim)])
    zPlane.append([[['.' for y in range(yDim)] for x in range(xDim)]for w in range(wDim)])

    # print('-post-expand-')
    # print(len(zPlane))
    # for z in zPlane:
        # print('  ' + str(len(z)))
        # for x in z:
            # print('    ' + str(len(x)))
            # print('      ', end='')
            # for y in x:
                # print(str(len(y)) + ' (' + str(y) + ') ', end='')
            # print()
    # print('-end post-expand-')

    # copy plane for update
    newZPlane = json.loads(json.dumps(zPlane))

    for zi in range(len(zPlane)):
        for wi in range(len(zPlane[zi])):
            for xi in range(len(zPlane[zi][wi])):
                for yi in range(len(zPlane[zi][wi][xi])):
                    count = countNeighbors(zPlane, zi, wi, xi, yi)
                    if zPlane[zi][wi][xi][yi] == '#':
                        if count != 2 and count != 3:
                            newZPlane[zi][wi][xi][yi] = '.'
                    elif zPlane[zi][wi][xi][yi] == '.':
                        if count == 3:
                            newZPlane[zi][wi][xi][yi] = '#'

    zPlane = newZPlane

activeCount = 0
for z in zPlane:
    for w in z:
        for x in w:
            for y in x:
                if y == '#':
                    activeCount += 1

print(activeCount)