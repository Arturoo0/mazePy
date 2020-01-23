
import pygame
import maze
import color
import varSizing
import sys

pygame.init()

GRID_SIZE = 133
if GRID_SIZE > 1500: sys.exit();

WINDOW_SIZE = varSizing.adjustSize(GRID_SIZE)
display = pygame.display.set_mode(WINDOW_SIZE)
print(WINDOW_SIZE)

pygame.display.set_caption("MazePy")

mazeObj = maze.Maze()
mazeObj.generateMap(GRID_SIZE)
mazeObj.generateMaze(display, WINDOW_SIZE)
mazeObj.solve()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    display.fill(color.BLACK)
    mazeObj.printMap(display, WINDOW_SIZE)

    pygame.display.update()
