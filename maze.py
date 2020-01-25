import shapes
import color
import random
import pygame
import math
import animation

class Maze :

    map = []
    animatedMap = []
    # retraceAnimation = animation.Animation()
    # mazeAnimation = animation.Animation()
    # fillAnimation = animation.Animation()
    mainAnimation = animation.Animation()

    def retraceSolution(self, hashMap, end):

        currentParent = hashMap[end]
        self.mainAnimation.queueStep((end[0], end[1], "s"))

        while (True):
            self.mainAnimation.queueStep((currentParent[0], currentParent[1], "s"))
            currentParent = hashMap[currentParent]

            if (hashMap[currentParent] == (-1, -1)):
                # self.map[currentParent[0]][currentParent[1]] = "s"
                self.mainAnimation.queueStep((0,0, "s"))
                return True


    def generateMap(self, rows):

        for row in range(rows):
            self.map.append([])

        for row in range(rows):

            if ((row + 1) % 2 != 0):
                for column in range(rows):
                    if ((column + 1) % 2 != 0) :
                        self.map[row].append("-")
                    else :
                        self.map[row].append("|")

            else :
                for column in range(rows):
                    self.map[row].append("|")

            for row in range(rows):
                self.animatedMap.append([])

            for row in range(rows):

                if ((row + 1) % 2 != 0):
                    for column in range(rows):
                        if ((column + 1) % 2 != 0) :
                            self.animatedMap[row].append("-")
                        else :
                            self.animatedMap[row].append("|")

                else :
                    for column in range(rows):
                        self.animatedMap[row].append("|")

    def printMap(self, display, WINDOW_SIZE):

        tileColor = color.BLACK
        wallColor = color.WHITE
        fillColor = color.PINK
        solColor = color.BABY_BLUE

        x = 0
        y = 0
        sizeIncrement = WINDOW_SIZE[0]/len(self.map[:])

        for row in range(len(self.map)):

            if (row + 1) % 2 != 0 :
                for column in range(len(self.map)):

                    if (self.animatedMap[row][column] == "-" or self.animatedMap[row][column] == "o"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, tileColor)
                        x += sizeIncrement
                    elif (self.animatedMap[row][column] == "X"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, fillColor)
                        x += sizeIncrement
                    elif (self.animatedMap[row][column] == "s"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, solColor)
                        x += sizeIncrement
                    else :
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, wallColor)
                        x += sizeIncrement

                y += sizeIncrement
                x = 0

            else :
                for column in range(len(self.map)):

                    if (self.animatedMap[row][column] == "o" or self.animatedMap[row][column] == "-"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, tileColor)
                        x += sizeIncrement
                    elif (self.animatedMap[row][column] == "X"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, fillColor)
                        x += sizeIncrement
                    elif (self.animatedMap[row][column] == "s"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, solColor)
                        x += sizeIncrement
                    else :
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, wallColor)
                        x += sizeIncrement

                y += sizeIncrement
                x = 0

    def generateMaze(self, display, WINDOW_SIZE): # TRAVELED == o, direction; (1:top), (2:bottom), (3:left), (4:right)
      print("entered")
      backStack = [(0,0)]
      current = backStack[-1]
      direction = []

      while (len(backStack) != 0):

        current = backStack[-1]

        row = current[0]
        column = current[1]

        self.map[row][column] = "o"

        checkTop = checkDown = checkLeft = checkRight = False

        if (row + 2 < len(self.map[:])): #checks bottom index
          checkDown = (self.map[row + 2][column] == "-")
          if checkDown:
            direction.append((2, 0, 1, 0))

        if (column + 2 < len(self.map[0][:])): #checks the right index
          checkRight = (self.map[row][column + 2] == "-")
          if checkRight:
              direction.append((0, 2, 0, 1))

        if (column - 2 > -1): #checks the left index
          checkLeft = (self.map[row][column - 2] == "-")
          if checkLeft:
              direction.append((0, -2, 0, -1))

        if (row - 1 > -1): #checks the top index
          checkTop = (self.map[row - 2][column] == "-")
          if checkTop:
              direction.append((-2, 0, -1, 0))

        if (not (checkDown or checkRight or checkLeft or checkTop)):
          backStack.pop()
        else :
          direc = random.sample(direction, 1)[0]

          backStack.append((row + direc[0], column + direc[1]))
          self.map[row + direc[2]][column + direc[3]] = "o"
          self.mainAnimation.queueStep((row + direc[2], column + direc[3], "o"))

          direction = []

    def solve(self):

        # hashMap tile; parent

        queue = [(0,0)]
        end = (len(self.map[:]) - 1, len(self.map[:]) - 1)
        parentHash = {(0,0):(-1,-1)}

        while (True):

            if len(queue) == 0:
                return False;
            else :
                current = queue.pop(0)

            row = current[0]
            column = current[1]

            self.map[row][column] = "X"
            self.mainAnimation.queueStep((row, column, "X"))

            if (row == end[0] and column == end[1]):
                return parentHash, end

            checkTop = checkDown = checkLeft = checkRight = False

            if (row + 1 < len(self.map[:])): #checks bottom index
                checkDown = (self.map[row + 1][column] == "o")

            if (column + 1 < len(self.map[0][:])): #checks the right index
                checkRight = (self.map[row][column + 1] == "o")

            if (column - 1 > -1): #checks the left index
                checkLeft = (self.map[row][column - 1] == "o")

            if (row - 1 > -1): #checks the top index
                checkTop = (self.map[row - 1][column] == "o")

            if (checkDown): # if down index for example is empty and equals '-' then append the coord tuple
                queue.append((row + 1, column))
                parentHash[(row + 1, column)] = (row, column)

            if (checkRight):
                queue.append((row, column + 1))
                parentHash[(row, column + 1)] = (row, column)

            if (checkTop):
                queue.append((row - 1, column))
                parentHash[(row - 1, column)] = (row, column)

            if (checkLeft):
                queue.append((row, column - 1))
                parentHash[(row, column - 1)] = (row, column)
