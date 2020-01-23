
import pygame
import maze
import color
import varSizing
import sys

pygame.init()

clock = pygame.time.Clock()

GRID_SIZE = 47
if GRID_SIZE > 1500: sys.exit();

WINDOW_SIZE = varSizing.adjustSize(GRID_SIZE)
display = pygame.display.set_mode(WINDOW_SIZE)
print(WINDOW_SIZE)

pygame.display.set_caption("MazePy")

mazeObj = maze.Maze()
mazeObj.generateMap(GRID_SIZE)
mazeObj.generateMaze(display, WINDOW_SIZE)
mazeObj.solve()

timer = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(color.BLACK)
    dt = 2 * (clock.tick(60))

    #if timer ...
    timer += dt
    print(dt)

    if (timer > .005 and mazeObj.retraceAnimation.animationQueue):
        currentAnimation = mazeObj.retraceAnimation.dequeStep()
        mazeObj.map[currentAnimation[0]][currentAnimation[1]] = "s"
        timer = 0

    mazeObj.printMap(display, WINDOW_SIZE)

    pygame.display.update()
