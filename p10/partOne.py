inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = int(inp[i].rstrip())

diffs = dict()
inp.sort()

target = 3 + 0 
last = 0

for i in inp:

    if (i - last) in diffs:
        diffs[i - last] += 1
    else:
        diffs[i - last] = 1
    last = i

print([x for x in diffs.keys()])
print(diffs[1] * (1 + diffs[3]))