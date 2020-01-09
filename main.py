
import pygame
pygame.init()

WINDOW_SIZE = (700, 700)
display = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("MazePy")

def drawRec(x, y, sizeX, sizeY): # easier way of creating new rectangles
    pygame.draw.rect(display, (0,0,0), [x, y, sizeX, sizeY], 1)

def drawGrid(rows, columns): # creates the grid to the display

    x = 0
    y = 0
    incrementX = WINDOW_SIZE[0]/ columns
    incrementY =  WINDOW_SIZE[1]/ rows

    for column in range(columns):

        for row in range(rows):
            drawRec(x, y, incrementX, incrementY)
            y += incrementY

        y = 0
        x += incrementX

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill((255,255,255))

    drawGrid(20,20)

    pygame.display.update()
