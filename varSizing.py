
def adjustSize(gridSize):

    size = (700, 700)
    pixelRange = list(range(700, 901))

    for res in pixelRange:
        if res % gridSize == 0:
            size = (res, res)
            break

    return size
