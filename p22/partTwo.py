import sys
sys.setrecursionlimit(3000) # to deal with my terrible recursion method, please just burn this file after reading it (trying to get a good score)

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

def recurseCombat(playerOneDeck, playerTwoDeck, historyOne, historyTwo):
    global playAnotherRound
    print('new game')
    print(playerOneDeck)
    print(playerTwoDeck)
    
    if len(playerOneDeck) == 0:
        return 2
    if len(playerTwoDeck) == 0:
        return 1
    
    doAnotherRound = False
    for i in range(1):
        sameAsPast = False
        for deck in historyOne:
            if len(deck) == len(playerOneDeck):
                match = True
                for i in range(len(deck)):
                    if deck[i] != playerOneDeck[i]:
                        match = False
                        break
                if match:
                    sameAsPast = True
                    break
        if sameAsPast:
            return 1

        sameAsPast = False
        for deck in historyTwo:
            if len(deck) == len(playerTwoDeck):
                match = True
                for i in range(len(deck)):
                    if deck[i] != playerTwoDeck[i]:
                        match = False
                        break
                if match:
                    sameAsPast = True
                    break
        if sameAsPast:
            return 1

        historyOne.append(playerOneDeck[:])
        historyTwo.append(playerTwoDeck[:])

        v1 = playerOneDeck[0]
        v2 = playerTwoDeck[0]
        if v1 < len(playerOneDeck) and v2 < len(playerTwoDeck):
            res = recurseCombat(playerOneDeck[1:v1 + 1], playerTwoDeck[1:v2 + 1], [], [])
            if res == 1:
                playerOneDeck.append(v1)
                playerOneDeck.append(v2)
            else:
                playerTwoDeck.append(v2)
                playerTwoDeck.append(v1)
            del playerOneDeck[0]
            del playerTwoDeck[0]
            doAnotherRound = True

        else:
            res = None
            if v1 >= v2:
                playerOneDeck.append(v1)
                playerOneDeck.append(v2)
                res = (1, playerOneDeck)
            else:
                playerTwoDeck.append(v2)
                playerTwoDeck.append(v1)
                res = (2, playerTwoDeck)
            del playerOneDeck[0]
            del playerTwoDeck[0]
            doAnotherRound = True

    if doAnotherRound:
        return recurseCombat(playerOneDeck, playerTwoDeck, historyOne, historyTwo)


histOne = []
histTwo = []

recurseCombat(playerOne, playerTwo, [], [])

score1 = 0
for i in range(len(playerOne)):
    score1 += playerOne[i] * (len(playerOne) - i)
    
score2 = 0
for i in range(len(playerTwo)):
    score2 += playerTwo[i] * (len(playerTwo) - i)
    
print(score1)
print(score2)