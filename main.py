
import pygame
import maze
import color
import varSizing
import sys
import animation
import config

timer = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    config.display.fill(color.BLACK)

    #if timer ...
    timer += config.clock.tick(60)

    config.animate.startAnimation(config.mazeObj, timer, config.GRID_SIZE)
    timer = 0

    config.mazeObj.printMap(config.display, config.WINDOW_SIZE)

    pygame.display.update()
