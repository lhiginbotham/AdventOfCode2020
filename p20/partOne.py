import copy
import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

tileOrientedImages = dict()
currTileId = -1
baseImage = []
for line in inp:
    if 'Tile' in line: 
        currTileId = int(line.split(' ')[1][:-1])
    elif len(line) == 0:
        tileOrientedImages[currTileId] = [baseImage]
        currTileId = -1
        baseImage = []
    else:
        baseImage.append([c for c in line])

def getRotArray(arr):
    rotArr = [['' for j in range(len(arr[0]))] for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            rotArr[j][len(arr) - 1 - i] = arr[i][j]
    return rotArr

def getFlippedArray(arr, direction):
    flippedArr = copy.deepcopy(arr)
    if direction == 'horizontal' or direction == 'both':
        copy2 = copy.deepcopy(flippedArr)
        for i in range(len(flippedArr)):
            for j in range(len(flippedArr[0])):
                flippedArr[i][j] = copy2[i][len(flippedArr) - 1 - j]
    if direction == 'vertical' or direction == 'both':
        copy2 = copy.deepcopy(flippedArr)
        for i in range(len(flippedArr)):
            for j in range(len(flippedArr[0])):
                flippedArr[i][j] = copy2[len(flippedArr) - 1 - i][j]
    return flippedArr

def genOrientation(tileId):
    base = tileOrientedImages[tileId]
    images = []
    images.append(base)
    images.append(getFlippedArray(base, 'horizontal'))
    images.append(getFlippedArray(base, 'vertical'))
    images.append(getFlippedArray(base, 'both'))

    for i in range(4):
        images.append(getRotArray(images[i]))
        images.append(getRotArray(images[len(images)]))
        images.append(getRotArray(images[len(images)]))
        images.append(getRotArray(images[len(images)]))

    tileOrientedImages[tileId] = images

def findImageConnections

for tileId in tileOrientedImages:
    genOrientation(tileOrientedImages)

hexChars = [c for c in '0123456789abcdef']

idxToTileId = dict()
tileIdx = 0
for tileId in tileOrientedImages:
    idxToTileId[tileIdx] = tileId
    tileIdx += 1

imageOrientationIndices = [[hexChars for i in range(len(tileOrientedImages.keys()))]]


for combo in itertools.product(*imageOrientationIndices):
    