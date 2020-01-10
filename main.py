
import pygame
import maze
pygame.init()

WINDOW_SIZE = (1400, 700)
display = pygame.display.set_mode(WINDOW_SIZE)
mazeObj = maze.Maze()

pygame.display.set_caption("MazePy")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill((255,255,255))
    mazeObj.generateMap(30, 15, WINDOW_SIZE)

    pygame.display.update()
