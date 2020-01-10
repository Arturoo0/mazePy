import shapes

class Maze :

    map = []

    def generateMap(self, display, rows, columns, WINDOW_SIZE):

        x = 0
        y = 0
        parityCountY = 1
        parityCountX = 1
        incrementY =  WINDOW_SIZE[1]/ rows
        incrementX = WINDOW_SIZE[0]/ columns

        for column in range(columns):

            parityCountX += 1

            for row in range(rows):

                if parityCountY % 2 == 0 :

                    shapes.drawRec(display, x, y, incrementY, incrementY, (255,255,255))
                    self.map.append((x,y))

                else :
                    if parityCountX % 2 != 0:
                        shapes.drawRec(display, x, y, incrementY, incrementY, (255,255,255))
                        self.map.append((x,y))
                    else :
                        shapes.drawRec(display, x, y, incrementY, incrementY, (255,0,0))
                        self.map.append((x,y))

                y += incrementY
                parityCountY += 1

            y = 0
            x += incrementY


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
