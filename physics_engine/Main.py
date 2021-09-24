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
WINDOWHEIGHT = 425
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Physics engine')
 


 
def gameloop():    
    player = pygame.Rect(WINDOWWIDTH//2, WINDOWHEIGHT//2, 20, 20)

    #acceleration
    acceleration_count = 0
    acceleration_list = []
    acceleration = 0

    #displacement
    current_pos = player.center
    old_pos = (0, 0)
    displacement = 0.1
    tick_count_displacement = 0

    #gravity
    deltaTime = 0.0
    gravityAcceleration = -9.81 / 3
    velocity = 0

    font = pygame.font.Font('freesansbold.ttf', 15)
    screens = ['Time_delta', 'Gravity Acceleration', 'Displacement', 'acceleration']
    screens[2] = [font.render('Displacement between frames:' +str(displacement), True, (0,0,0)), (0,30)]
    screens[3] = [font.render(f'Average Velocity is: {acceleration}pixels/5seconds', True, (128,45,45)), (0,45)]





    getTicksLastFrame = pygame.time.get_ticks()

    while True:
        
    # Check for events.
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #updates cube onto mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.center = pygame.mouse.get_pos()
                velocity = 0
 

        # very basic gravity script
        if player.bottom < WINDOWHEIGHT:
            velocity -= gravityAcceleration * deltaTime
            player.y += velocity

        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        tick_count_displacement += deltaTime
        acceleration_count += deltaTime




    # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))


        # calculates the displacement between frames
        current_pos = player.center
        displacement = (current_pos[0] - old_pos[0]) + (current_pos[1] - old_pos[1])
        if displacement < 0:
            acceleration_list.append(abs(displacement))
        else:
            acceleration_list.append(displacement)
        old_pos = current_pos


        # every 2.5 seconds will update the average accelearation the physiscs object has moved in pixels
        if acceleration_count > 2.5:
            for displacement in acceleration_list:
                acceleration += displacement
            acceleration /= len(acceleration_list)
            acceleration = round(acceleration /  5, 2)



            ## to be removed with terminal velocity added
            if acceleration == 0:
              velocity = 0
            ## to be removed with terminal velocity added

            

            screens[3] = [font.render(f'Average Acceleration is: {acceleration}pixels/2.5seconds', True, (128,0,0)), (0,45)]

            acceleration_list = []
            acceleration_count = 0

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
        else:

        # Draw the window onto the screen.
            pygame.display.update()
        mainClock.tick(60)
 
gameloop()