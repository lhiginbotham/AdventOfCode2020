inp = [0,13,1,8,6,15]
# with open('input.txt') as f:
    # inp = f.readlines()
    # for i in range(len(inp)):
        # inp[i] = inp[i].rstrip()

while len(inp) < 2021:
    searchNum = inp[-1]
    found = 0
    firstFindAge = 0
    secondFindAge = 0
    for i in range(len(inp) - 1, -1, -1):
        if inp[i] == searchNum:
            found += 1
            if found == 1:
                firstFindAge = i
            if found > 1:
                secondFindAge = i
                break
    if found < 2:
        inp.append(0)
    else:
        inp.append(firstFindAge - secondFindAge)

print(inp[2019])