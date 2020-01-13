import shapes

class Maze :

    map = []

    def generateMap(self, display, rows, columns, WINDOW_SIZE):

        x = 0
        y = 0
        incrementY =  WINDOW_SIZE[1]/ rows
        incrementX = WINDOW_SIZE[0]/ columns

        for row in range(rows):
            if ((row + 1) % 2 != 0) :

                for column in range(columns):

                    shapes.drawRec(display, x, y, incrementY, incrementY, (255,0,0))
                    x += incrementX

                x = 0
                y += incrementY

            else :
                for column in range(columns):

                    shapes.drawRec(display, x, y, incrementY, incrementY, (255,255,255))
                    x += incrementX

                x = 0
                y += incrementY


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
