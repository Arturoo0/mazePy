
import pygame
import maze
import color
import varSizing
import sys
import animation

pygame.init()

clock = pygame.time.Clock()

GRID_SIZE = 31
if GRID_SIZE > 1500: sys.exit();

WINDOW_SIZE = varSizing.adjustSize(GRID_SIZE)
display = pygame.display.set_mode(WINDOW_SIZE)
print(WINDOW_SIZE)

pygame.display.set_caption("MazePy")

animate = animation.Animation()

mazeObj = maze.Maze()
mazeObj.generateMap(GRID_SIZE)
mazeObj.generateMaze(display, WINDOW_SIZE)


hashMap, end = mazeObj.solve()
mazeObj.retraceSolution(hashMap, end)

timer = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(color.BLACK)

    #if timer ...
    timer += clock.tick(60)

    animate.startAnimation(mazeObj, timer)
    timer = 0

    mazeObj.printMap(display, WINDOW_SIZE)

    pygame.display.update()
