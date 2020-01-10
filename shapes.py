
import pygame
import main

#color should be a tuple
def drawRec(x, y, sizeX, sizeY, color): # easier way of creating new rectangles
    pygame.draw.rect(main.display, color, [x, y, sizeX, sizeY], 1)
