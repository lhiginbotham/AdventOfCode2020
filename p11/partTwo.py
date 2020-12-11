import os

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()
        inp[i] = [x for x in inp[i]]

def personSpotted(positions):
    if len(positions) < 1:
        return 0

    # iterable = []
    # if checkEnd:
        # iterable = range(len(positions) - 1, -1)
    # else:
        # iterable = range(0, len(positions))

    for i in range(0, len(positions)):
        posVal = inp[positions[i][0]][positions[i][1]]
        if posVal == '#':
            return 1
        elif posVal == 'L':
            return 0
    return 0

def countSurroundings(row, col):
    surround = 0

    # up
    surround += personSpotted([(i, col) for i in range(row - 1, -1, -1)])
    # down
    surround += personSpotted([(i, col) for i in range(row + 1, len(inp), +1)])
    # left
    surround += personSpotted([(row, i) for i in range(col - 1, -1, -1)])
    # right
    surround += personSpotted([(row, i) for i in range(col + 1, len(inp[0]), +1)])

    toCheck = []

    # up-left
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        toCheck.append((i, j))
        i -= 1
        j -= 1

    if (len(toCheck)):
        surround += personSpotted(toCheck)

    toCheck = []

    # down-left
    i = row + 1
    j = col - 1
    while i < len(inp) and j >= 0:
        toCheck.append((i, j))
        i += 1
        j -= 1

    if (len(toCheck)):
        surround += personSpotted(toCheck)

    toCheck = []

    # up-right
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(inp[0]):
        toCheck.append((i, j))
        i -= 1
        j += 1

    if (len(toCheck)):
        surround += personSpotted(toCheck)

    toCheck = []

    # down-right
    i = row + 1
    j = col + 1
    while i < len(inp) and j < len(inp[0]):
        toCheck.append((i, j))
        i += 1
        j += 1

    if (len(toCheck)):
        surround += personSpotted(toCheck)

    #print("row " + str(row) + " col " + str(col) + " surround " + str(surround))
    #input()
    return surround

def visualize():
    os.system('cls')
    for x in inp:
        for c in x:
            print(c, end='')
        print()

changed = True
while changed:
    visualize()
    #input('next')
    changed = False
    newInp = []
    for row in range(0, len(inp)):
        newInp.append([])
        for col in range(0, len(inp[0])):
            if inp[row][col] == 'L':
                if countSurroundings(row, col) == 0:
                    changed = True
                    newInp[row].append('#')
                else:
                    newInp[row].append('L')
            elif inp[row][col] == '#':
                if countSurroundings(row, col) >= 5:
                    changed = True
                    newInp[row].append('L')
                else:
                    newInp[row].append('#')
            else:
                newInp[row].append('.')
    inp = newInp

visualize()
count = 0
for x in inp:
    for y in x:
        if y == '#':
            count += 1
print(count)