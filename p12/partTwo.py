import os

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

wp = [10, 1]
pos = [0, 0]

def moveBearing(val):
    global pos, wp
    pos[0] += val * wp[0]
    pos[1] += val * wp[1]

def rotate(val):
    global wp
    if val == 0:
        return
    elif val == 1:
        new = [0, 0]
        new[0] = -wp[1]
        new[1] = wp[0]
        wp[0] = new[0]
        wp[1] = new[1]
    elif val == 2:
        wp[0] = 0 - wp[0]
        wp[1] = 0 - wp[1]
    elif val == 3:
        rotate(1)
        rotate(1)
        rotate(1)

for x in inp:
    i = x[0]
    v = int(x[1:])
    oldBear = bearing
    if i == 'F':
        moveBearing(v)
    elif i == 'B':
        moveBearing(-v)
    elif i == 'N':
        wp[1] += v
    elif i == 'S':
        wp[1] -= v
    elif i == 'E':
        wp[0] += v
    elif i == 'W':
        wp[0] -= v
    elif i == 'L':
        rotate((v / 90) % 4)
    elif i == 'R':
        rotate((4 - v / 90) % 4)

print(abs(pos[0]) + abs(pos[1]))