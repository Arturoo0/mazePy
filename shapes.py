
import pygame

#color should be a tuple
def drawRec(display, x, y, sizeX, sizeY, color): # easier way of creating new rectangles
    pygame.draw.rect(display, color, [x, y, sizeX, sizeY])
