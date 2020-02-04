
import maze
import varSizing
import pygame
import animation

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("MazePy")

GRID_SIZE = 31
if GRID_SIZE > 1500: sys.exit();

WINDOW_SIZE = varSizing.adjustSize(GRID_SIZE)
display = pygame.display.set_mode(WINDOW_SIZE)

animate = animation.Animation()

mazeObj = maze.Maze()
mazeObj.generateMap(GRID_SIZE)
mazeObj.generateMaze(display, WINDOW_SIZE)

hashMap, end = mazeObj.solve()
mazeObj.retraceSolution(hashMap, end)
