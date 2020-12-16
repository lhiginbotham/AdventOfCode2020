inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

rules = dict()
myTick = []
otherTicks = []
step = 0
for line in inp:
    if 'your ticket' in line:
        step = 1
        continue
    elif 'nearby tickets' in line:
        step = 2
        continue

    if step == 0:
        if not len(line):
            continue
        rule, ranges = line.split(': ')
        ranges = ranges.split(' or ')
        rangesObjs = []
        for r in ranges:
            low, high = r.split('-')
            rangesObjs.append((int(low), int(high)))
        rules[rule] = rangesObjs
    elif step == 1:
        if not len(line):
            continue
        myTick = [int(x) for x in line.split(',')]
    else:
        if not len(line):
            continue
        otherTicks.append([int(x) for x in line.split(',')])

invalidValue = 0
for other in otherTicks:
    isInvalid = False
    for val in other:
        fieldSolvesAnyRule = False
        for rule in rules:
            for r in rules[rule]:
                print(r)
                if val >= r[0] and val <= r[1]:
                    fieldSolvesAnyRule = True
                    break

        if not fieldSolvesAnyRule:
            isInvalid = True
            invalidValue += val


print(invalidValue)
