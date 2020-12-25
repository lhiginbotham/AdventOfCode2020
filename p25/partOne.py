loopsize = 0 # secret
div = 20201227

doorPub = 2959251
cardPub = 4542595

def getLoopSize(subject, key):
    val = 1
    loopSize = 0
    while val != key:
        val *= subject
        val = val % div
        loopSize += 1
    return loopSize

doorloopsize = getLoopSize(7, doorPub)
cardloopsize = getLoopSize(7, cardPub)
print(doorloopsize)
print(cardloopsize)

# too lazy to get this out of the other method
def getEncrypt(subject, loopsize):
    val = 1
    for i in range(loopsize):
        val *= subject
        val = val % div
    return val

print(getEncrypt(doorPub, cardloopsize))
print(getEncrypt(cardPub, doorloopsize))