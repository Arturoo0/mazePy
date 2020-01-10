
import pygame
import maze
pygame.init()

WINDOW_SIZE = (1400, 700)
display = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("MazePy")
mazeObj = maze.Maze()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill((255,255,255))
    mazeObj.generateMap(display, 30, 15, WINDOW_SIZE)
    # shapes.drawRec(display,50,50, 40, 40, (0,0,0))

    pygame.display.update()
