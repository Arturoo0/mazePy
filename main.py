
import pygame
import maze
import color
pygame.init()

WINDOW_SIZE = (700, 700)
display = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("MazePy")
mazeObj = maze.Maze()

GRID_SIZE = 51
mazeObj.generateMap(GRID_SIZE)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(color.WHITE)
    mazeObj.generateMaze(display, WINDOW_SIZE)

    # shapes.drawRec(display,50,50, 40, 40, (0,0,0))
    # mazeObj.generateMap(display, 7, 7, WINDOW_SIZE)

    pygame.display.update()
