inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

playerOne = []
playerTwo = []

dest = playerOne
for line in inp:
    if 'Player 1' in line:
        continue
    if 'Player 2' in line:
        dest = playerTwo
        continue
    if len(line) > 0:
        dest.append(int(line))

while len(playerOne) > 0 and len(playerTwo) > 0:
    print()
    print(playerOne)
    print(playerTwo)
    v1 = playerOne[0]
    v2 = playerTwo[0]
    if playerOne[0] >= playerTwo[0]:
        playerOne.append(v1)
        playerOne.append(v2)
    else:
        playerTwo.append(v2)
        playerTwo.append(v1)
    del playerOne[0]
    del playerTwo[0]

score1 = 0
for i in range(len(playerOne)):
    score1 += playerOne[i] * (len(playerOne) - i)
    
score2 = 0
for i in range(len(playerTwo)):
    score2 += playerTwo[i] * (len(playerTwo) - i)
    
print(score1)
print(score2)