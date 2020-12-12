import os

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

bearing = 0
pos = [0, 0]

def moveBearing(val):
    if bearing == 0: #east
        pos[0] += val
    elif bearing == 2: #west
        pos[0] -= val
    elif bearing == 1: #north
        pos[1] += val
    else:
        pos[1] -= val

for x in inp:
    i = x[0]
    v = int(x[1:])
    oldBear = bearing
    if i == 'F':
        moveBearing(v)
    elif i == 'B':
        moveBearing(-v)
    elif i == 'N':
        bearing = 1
        moveBearing(v)
        bearing = oldBear
    elif i == 'S':
        bearing = 3
        moveBearing(v)
        bearing = oldBear
    elif i == 'E':
        bearing = 0
        moveBearing(v)
        bearing = oldBear
    elif i == 'W':
        bearing = 2
        moveBearing(v)
        bearing = oldBear
    elif i == 'L':
        bearing = ((v / 90) + bearing) % 4
    elif i == 'R':
        bearing = ((4 - v / 90) + bearing) % 4

print(abs(pos[0]) + abs(pos[1]))