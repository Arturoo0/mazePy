import shapes
import color
import random
import pygame

class Maze :

    map = []

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


    def printMap(self, display, WINDOW_SIZE):

        x = 0
        y = 0
        sizeIncrement =  WINDOW_SIZE[0]/ len(self.map)

        for row in range(len(self.map)):

            if (row + 1) % 2 != 0 :
                for column in range(len(self.map)):

                    if (self.map[row][column] == "-" or self.map[row][column] == "o"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.ORANGE)
                        x += sizeIncrement
                    else :
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.WHITE)
                        x += sizeIncrement

                y += sizeIncrement
                x = 0

            else :
                for column in range(len(self.map)):

                    if (self.map[row][column] == "o"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.ORANGE)
                        x += sizeIncrement
                    else :
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.WHITE)
                        x += sizeIncrement

                y += sizeIncrement
                x = 0

    def generateMaze(self, display, WINDOW_SIZE): # TRAVELED == o, direction; (1:top), (2:bottom), (3:left), (4:right)

      backStack = [(0,0)]
      current = backStack[-1]
      direction = []

      while (len(backStack) != 0):

        row = current[0]
        column = current[1]

        self.map[row][column] = "o"


        if (row + 2 < len(self.map[:])): #checks bottom index
          checkDown = (self.map[row + 2][column] == "-")
          direction.append(3)
        else:
          checkDown = False

        if (column + 2 < len(self.map[0][:])): #checks the right index
          checkRight = (self.map[row][column + 2] == "-")
          direction.append(2)
        else :
          checkRight = False

        if (column - 2 > -1): #checks the left index
          checkLeft = (self.map[row][column - 2] == "-")
          direction.append(4)
        else :
          checkLeft = False

        if (row - 1 > -1): #checks the top index
          checkTop = (self.map[row - 2][column] == "-")
          direction.append(1)
        else :
          checkTop = False

        if (checkDown == False and checkRight == False and checkLeft == False and checkTop == False):
          current = backStack.pop()

        else :
          direc = random.sample(direction, 1)[0]

          self.map[row][column] = "o"

          if direc == 1 and checkTop : current = (row - 2, column); backStack.append((row, column)); self.map[row - 1][column] = "o"
          if direc == 2 and checkRight : current = (row, column + 2); backStack.append((row, column)); self.map[row][column + 1] = "o"
          if direc == 3 and checkDown : current = (row + 2, column); backStack.append((row, column)); self.map[row + 1][column] = "o"
          if direc == 4 and checkLeft : current = (row, column - 2); backStack.append((row, column)); self.map[row][column - 1] = "o"
          direction = []

        direction = []
        self.printMap(display, WINDOW_SIZE)
