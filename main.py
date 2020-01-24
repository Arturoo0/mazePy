
import pygame
import maze
import color
import varSizing
import sys

pygame.init()

clock = pygame.time.Clock()

GRID_SIZE = 37
if GRID_SIZE > 1500: sys.exit();

WINDOW_SIZE = varSizing.adjustSize(GRID_SIZE)
display = pygame.display.set_mode(WINDOW_SIZE)
print(WINDOW_SIZE)

pygame.display.set_caption("MazePy")

mazeObj = maze.Maze()
mazeObj.generateMap(GRID_SIZE)
mazeObj.generateMaze(display, WINDOW_SIZE)

timer = 0
solved = False
solvedMap, end = {}, ()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill(color.BLACK)
    dt = 2 * (clock.tick(60))

    #if timer ...
    timer += dt

    if (timer > .005 and len(mazeObj.mazeAnimation.animationQueue) > 0 and not solved):
        currentAnimation = mazeObj.mazeAnimation.dequeStep()
        mazeObj.map[currentAnimation[0]][currentAnimation[1]] = "o"
        timer = 0

    if (len(mazeObj.mazeAnimation.animationQueue) == 0 and solved == False):
        solvedMap, end = mazeObj.solve()
        solved = True
        mazeObj.retraceSolution(solvedMap, end)

    if (solved and timer > .005 and len(mazeObj.retraceAnimation.animationQueue) > 0):
        currentAnimation = mazeObj.retraceAnimation.dequeStep()
        mazeObj.map[currentAnimation[0]][currentAnimation[1]] = "s"
        timer = 0

    mazeObj.printMap(display, WINDOW_SIZE)

    pygame.display.update()
