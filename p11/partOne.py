import os

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()
        inp[i] = [x for x in inp[i]]

def countSurroundings(row, col):
    surround = 0
    rows = [row - 1, row, row + 1]
    cols = [col - 1, col, col + 1]
    for r in rows:
        for c in cols:
            if (0 <= r < len(inp)) and (0 <= c < len(inp[0])):
                if r == row and c == col:
                    continue
                if inp[r][c] == '#':
                    surround += 1
    return surround

def visualize():
    os.system('cls')
    for x in inp:
        for c in x:
            print(c, end='')
        print()

changed = True
while changed:
    #input('next')
    visualize()
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
                if countSurroundings(row, col) >= 4:
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