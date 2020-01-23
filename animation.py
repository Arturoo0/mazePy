
class Animation :

    animationQueue = []

    def queueStep(self, tile):
        self.animationQueue.append(tile)

    def dequeStep(self):
        return self.animationQueue.pop(0)
