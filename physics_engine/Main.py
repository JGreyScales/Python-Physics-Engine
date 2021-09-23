from typing import final
import pygame, sys
import time as time2
from datetime import *
from pygame.locals import *
import math



# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()
 
# Set up the window.
WINDOWWIDTH = 700
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Physics engine')
 


 
def gameloop():    
    player = pygame.Rect(WINDOWWIDTH//2, WINDOWHEIGHT//2, 20, 20)


    #displacement
    current_pos = player.center
    old_pos = (0, 0)
    displacement = 0.0
    tick_count_displacement = 0

    #gravity
    deltaTime = 0.0
    gravityAcceleration = -9.81 / 3

    font = pygame.font.Font('freesansbold.ttf', 15)
    screens = ['Time_delta', 'Gravity Acceleration', 'Displacement']
    screens[2] = [font.render('Displacement between frames:' +str(displacement), True, (0,0,0)), (0,30)]




    getTicksLastFrame = pygame.time.get_ticks()

    while True:
    # Check for events.
        for event in pygame.event.get():


            #updates cube onto mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.center = pygame.mouse.get_pos()
 

        # very basic gravity script
        if player.bottom < WINDOWHEIGHT:
            player.y -= gravityAcceleration

        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        tick_count_displacement += deltaTime



    # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))


        # calculates the displacement between frames
        current_pos = player.center
        displacement = (current_pos[0] - old_pos[0]) + (current_pos[1] - old_pos[1])
        old_pos = current_pos
        
        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, (0, 0, 0), player)
        screens[0] = [font.render('Delta Time:' + str(deltaTime), True, (0,0,0)), (0,0)]
        screens[1] = [font.render('Gravity Acceleration:' + str(gravityAcceleration - (gravityAcceleration * 2)), True, (0,0,0)), (0,15)]

        if displacement > 3 or displacement < 0 or tick_count_displacement > 0.35:
            screens[2] = [font.render('Displacement between frames:' +str(displacement), True, (0,0,0)), (0,30)]
            tick_count_displacement = 0

        for i in range(len(screens)):
            windowSurface.blit(screens[i][0], screens[i][1])



        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(60)
 
gameloop()