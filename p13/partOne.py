inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

inp[1] = inp[1].split(',')
depTime = int(inp[0])

busses = []
for i in range(1, len(inp[1])):
    if inp[1][i] == 'x':
        continue
    busses.append(int(inp[1][i]))

print(busses)
shortestId = -1
shortestTime = -1
for bus in busses:
    time = 0
    while time < depTime:
        time += bus
    print(str(time) + ' ' + str(bus))
    curDif = time - depTime
    if curDif < shortestTime or shortestTime == -1:
        shortestTime = curDif
        shortestId = bus
print(shortestId * shortestTime)