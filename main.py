
import pygame
import maze
import color
import varSizing
import sys

pygame.init()

clock = pygame.time.Clock()

GRID_SIZE = 31
if GRID_SIZE > 1500: sys.exit();

WINDOW_SIZE = varSizing.adjustSize(GRID_SIZE)
display = pygame.display.set_mode(WINDOW_SIZE)
print(WINDOW_SIZE)

pygame.display.set_caption("MazePy")

mazeObj = maze.Maze()
mazeObj.generateMap(GRID_SIZE)
mazeObj.generateMaze(display, WINDOW_SIZE)

print(mazeObj.map)
print(mazeObj.animatedMap)
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

    if (timer > 1 and len(mazeObj.mainAnimation.animationQueue) > 0):

        currentAnimation = mazeObj.mainAnimation.dequeStep()
        print(currentAnimation)
        if (currentAnimation[2] == "o"):
            mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "o"
        elif (currentAnimation[2] == "s"):
            mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "s"
        elif (currentAnimation[2] == "X") :
            mazeObj.animatedMap[currentAnimation[0]][currentAnimation[1]] = "X"

        timer = 0

    mazeObj.printMap(display, WINDOW_SIZE)

    pygame.display.update()
