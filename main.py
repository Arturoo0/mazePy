
import pygame
import maze
import color
pygame.init()
WINDOW_SIZE = (700, 700)
display = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("MazePy")
GRID_SIZE = 81

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
