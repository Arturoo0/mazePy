
class Animation :

    animationQueue = []

    def queueStep(self, tile):
        self.animationQueue.append(tile)

    def dequeStep(self):
        return self.animationQueue.pop(0)


    def startAnimation(self, mazeObj, timer):

        if (timer > 0.05 and len(mazeObj.mainAnimation.animationQueue) > 0):

            currentAnimation = mazeObj.mainAnimation.dequeStep()

            if (currentAnimation[2] == "o"):
                mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "o"
            elif (currentAnimation[2] == "s"):
                mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "s"
            elif (currentAnimation[2] == "X") :
                mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "X"
