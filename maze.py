import shapes
import color

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

                    if (self.map[row][column] == "-"):
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.ORANGE)
                        x += sizeIncrement
                    else :
                        shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.WHITE)
                        x += sizeIncrement

                y += sizeIncrement
                x = 0

            else :
                for column in range(len(self.map)):
                    shapes.drawRec(display, x, y, sizeIncrement, sizeIncrement, color.WHITE)
                    x += sizeIncrement

                y += sizeIncrement
                x = 0

        # for row in range(rows):
        #
        #     if ((row + 1) % 2 != 0) :
        #         for column in range(columns):
        #             if((column + 1) % 2 != 0):
        #                 shapes.drawRec(display, x, y, incrementY, incrementY, (255,0,0))
        #                 x += incrementX
        #             else :
        #                 shapes.drawRec(display, x, y, incrementY, incrementY, (255,255,255))
        #                 x += incrementX
        #
        #         x = 0
        #         y += incrementY
        #
        #     else :
        #         for column in range(columns):
        #
        #             shapes.drawRec(display, x, y, incrementY, incrementY, (255,255,255))
        #             x += incrementX
        #
        #         x = 0
        #         y += incrementY


# def drawRec(x, y, sizeX, sizeY): # easier way of creating new rectangles
#     pygame.draw.rect(display, (0,0,0), [x, y, sizeX, sizeY], 1)
#
# def drawGrid(rows, columns): # creates the grid to the display
#
#     x = 0
#     y = 0
#     incrementY =  WINDOW_SIZE[1]/ rows
#     incrementX = WINDOW_SIZE[0]/ columns
#
#     for column in range(columns):
#
#         for row in range(rows):
#             drawRec(x, y, incrementY, incrementY)
#             y += incrementY
#
#         y = 0
#         x += incrementY
