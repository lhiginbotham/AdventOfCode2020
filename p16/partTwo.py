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
validTickets = [myTick]
for other in otherTicks:
    isInvalid = False
    for val in other:
        fieldSolvesAnyRule = False
        for rule in rules:
            for r in rules[rule]:
                #print(r)
                if val >= r[0] and val <= r[1]:
                    fieldSolvesAnyRule = True
                    break

        if not fieldSolvesAnyRule:
            isInvalid = True
            invalidValue += val
    if not isInvalid:
        validTickets.append(other)

ruleToPotentialFields = dict()
for rule in rules:
    ruleToPotentialFields[rule] = set(x for x in range(len(rules)))

print(ruleToPotentialFields)
print()


for other in validTickets:
    for rule in rules:
        potentialFields = ruleToPotentialFields[rule]
        if len(potentialFields) > 1:
            # still need to figure this rule out
            whittledPotentialFields = set()
            for index in potentialFields:
                fieldVal = other[index]
                isValid = False
                for r in rules[rule]:
                    if fieldVal >= r[0] and fieldVal <= r[1]:
                        isValid = True
                if isValid:
                    whittledPotentialFields.add(index)
            if len(whittledPotentialFields) < 1:
                print("booo")
                print(whittledPotentialFields)
                print(rule)
                exit()
            ruleToPotentialFields[rule] = whittledPotentialFields

def allRulesDecided():
    for rule in rules:
        if len(ruleToPotentialFields[rule]) > 1:
            return False
    return True

iterNum = 0
while not allRulesDecided():
    for rule in rules:
        potentialFields = ruleToPotentialFields[rule]
        if len(potentialFields) == 1:
            for otherRule in ruleToPotentialFields:
                if rule is not otherRule:
                    ruleToPotentialFields[otherRule].discard([x for x in potentialFields][0])
    iterNum += 1
    #print(iterNum)

multUp = 1
for rule in ruleToPotentialFields:
    if len(ruleToPotentialFields[rule]) != 1:
        print(ruleToPotentialFields)
        print("Ahhh!")
        exit()

    if 'departure' in rule:
        indices = [x for x in ruleToPotentialFields[rule]]
        #print('indices')
        #print(indices)
        multUp *= myTick[indices[0]]

print(multUp)
