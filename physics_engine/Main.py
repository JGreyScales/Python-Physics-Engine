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


    #gravity
    deltaTime = 0.0
    gravityAcceleration = -9.81 / 3

    font = pygame.font.Font('freesansbold.ttf', 15)
    screen_text = ['Time delta:' + str(deltaTime), 'Gravity Acceleration:' + str(gravityAcceleration)]
    screens = ['Time_delta', 'Gravity Acceleration']




    player = pygame.Rect(WINDOWWIDTH//2, WINDOWHEIGHT//2, 20, 20)

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



    # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))
        
        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, (0, 0, 0), player)
        screens[0] = [font.render('Time delta:' + str(deltaTime), True, (0,0,0)), (0,0)]
        screens[1] = [font.render('Gravity Acceleration:' + str(gravityAcceleration - (gravityAcceleration * 2)), True, (0,0,0)), (0,15)]
        for i in range(len(screens)):
            windowSurface.blit(screens[i][0], screens[i][1])



        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(60)
 
gameloop()