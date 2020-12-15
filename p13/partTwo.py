import math

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

inp[1] = inp[1].split(',')

busses = []
for i in range(0, len(inp[1])):
    busses.append(inp[1][i])

print(len(busses))

# (busId * x) % 67 = idx
# x * busId = 67 * n + idx
# x = (67 * n + idx) / busId
# x * busId - idx = 67 * n
# zero must equal (67 * n + idx) mod busId

xs = dict()
idxs = dict()
for i in range(1, len(busses)):
    busId = busses[i]
    if busId == 'x':
        continue
    xs[int(busId)] = 1
    idxs[int(busId)] = i

base = int(busses[0])
baseMult = 1
def allGood():
    keys = [k for k in xs.keys()]
    for key in keys:
        print('c')
        print(key)
        if base * baseMult != xs[key] * int(busses[idxs[key]]) - idxs[key]:
            return False
    return True

incr = True
while not allGood():
    if not incr:
        print('incr base')
        baseMult += 1
        incr = True
        continue

    incr = False
    keys = [k for k in idxs.keys()]
    for key in keys:
        print('a ' + str(int(busses[idxs[key]]) * xs[key] - idxs[key]))
        while base * baseMult > int(busses[idxs[key]]) * xs[key] - idxs[key]:
            incr = True
            #print("{0} {1} {2} {3} {4}".format(base, baseMult, busses[idxs[key]], xs[key], idxs[key]))
            xs[key] += int(math.ceil(1.0 * base * baseMult / (int(busses[idxs[key]]) * xs[key] - idxs[key])))

print(base * baseMult)
