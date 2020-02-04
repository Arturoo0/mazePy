
class Animation :

    animationQueue = []

    def queueStep(self, tile):
        self.animationQueue.append(tile)

    def dequeStep(self):
        return self.animationQueue.pop(0)

    def isEmpty(self):

        if (len(self.animationQueue) == 0):
            return True
        else:
            return False

    def computeSpeed(self, gridSize):

        speed = 0.002 * (gridSize * gridSize)

        return round(speed)

    def startAnimation(self, mazeObj, timer, gridSize):

        dequeAmount = self.computeSpeed(gridSize)

        if (timer > 0.05 and len(mazeObj.mainAnimation.animationQueue) > 0):

            for number in range(dequeAmount):

                if (self.isEmpty() == False):
                    currentAnimation = mazeObj.mainAnimation.dequeStep()
                else:
                    break

                if (currentAnimation[2] == "o"):
                    mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "o"
                elif (currentAnimation[2] == "s"):
                    mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "s"
                elif (currentAnimation[2] == "X") :
                    mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "X"
