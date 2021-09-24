from typing import final
import pygame, sys, math
import time as time2
from datetime import *
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()
 

# Set up the window.
WINDOWWIDTH = 500
WINDOWHEIGHT = 300
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Physics engine')
 

def calculate_terminal_velocity(m, g, c, p, a): #Mass, Gravity, Coefficent, Density of air, Projected area
    return math.sqrt((2*m*g)/(c*p*a))

    #print("Terminal Velocity  Calculated:   ", terminal_velocity)
 
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
    mass = 300 #
    deltaTime = 0.0
    gravityAcceleration = 9.81 / 2 #
    velocity = 0
    air_density = 1.225 #
    projected_area = math.sqrt( list(player)[2] * list(player)[3])
    terminal_velocity = calculate_terminal_velocity(mass, gravityAcceleration, 1.05, air_density, projected_area)


    font = pygame.font.Font('freesansbold.ttf', 15)

    screens = ['Time_delta', 'Gravity Acceleration', 'Displacement', 'acceleration', 'GA','MSB','AD']

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
              #button #1 event
                if b1.collidepoint(event.pos):
                    try:
                        gravityAcceleration = float(input("What do you want the Gravity Acceleration to be? "))
                        terminal_velocity = calculate_terminal_velocity(mass,gravityAcceleration, 1.05, air_density, projected_area)
                    except(ValueError):
                        print('Please use a float')
                elif b2.collidepoint(event.pos):
                    try:
                        mass = float(input("What do you want the Mass to be? "))
                        terminal_velocity = calculate_terminal_velocity(mass,gravityAcceleration, 1.05, air_density, projected_area)
                    except(ValueError):
                        print('please use a float')
                elif b3.collidepoint(event.pos):
                    try:
                        mass = float(input("What do you want the Air Density to be? "))
                        terminal_velocity = calculate_terminal_velocity(mass,gravityAcceleration, 1.05, air_density, projected_area)
                    except(ValueError):
                        print('please use a float')
                else:
                  player.center = pygame.mouse.get_pos()
                  velocity = 0
 

        # very basic gravity script
        if player.bottom < WINDOWHEIGHT:
          if velocity <= -terminal_velocity:
            velocity = -terminal_velocity
            player.y -= velocity
          elif velocity > -terminal_velocity:
            velocity -= gravityAcceleration * deltaTime / 1.05 
            player.y -= velocity
        elif player.bottom > WINDOWHEIGHT:
            player.bottom = WINDOWHEIGHT

        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        tick_count_displacement += deltaTime
        acceleration_count += deltaTime




    # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))


        # calculates the displacement between frames
        current_pos = player.center
        displacement = math.sqrt((current_pos[0] - old_pos[0])** 2 + (current_pos[1] - old_pos[1])**2)
        print(displacement)
        if displacement < -0:
            acceleration_list.append(displacement - (displacement * 2))
        else:
            acceleration_list.append(displacement)
        old_pos = current_pos


        # every 2.5 seconds will update the average accelearation the physiscs object has moved in pixels
        if acceleration_count > 2.5:
            for displacement in acceleration_list:
                acceleration += displacement
            acceleration /= len(acceleration_list)
            acceleration = round(acceleration /  2.5, 2)



            ## to be removed with terminal velocity added
            if acceleration == 0:
              velocity = 0
            ## to be removed with terminal velocity added

            

            screens[3] = [font.render(f'Average Acceleration is: {acceleration}pixels/2.5seconds', True, (128,0,0)), (0,45)]

            acceleration_list = []
            acceleration_count = 0
            
            #button creation
        bd1 = pygame.Rect(WINDOWWIDTH - 65, 5, 60, 30)
        b1 = pygame.Rect(WINDOWWIDTH - 63, 7, 56, 26)

        bd2 = pygame.Rect(WINDOWWIDTH - 65, 40, 60, 30)
        b2 = pygame.Rect(WINDOWWIDTH - 63, 42, 56, 26)

        bd3 = pygame.Rect(WINDOWWIDTH - 65, 75, 60, 30)
        b3 = pygame.Rect(WINDOWWIDTH - 63, 77, 56, 26)


        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, (0, 0, 0), player)
        screens[0] = [font.render('Delta Time:' + str(deltaTime), True, (0,0,0)), (0,0)]
        screens[1] = [font.render('Gravity Acceleration:' + str(gravityAcceleration), True, (0,0,0)), (0,15)]

        if displacement > 3 or displacement < 0 or tick_count_displacement > 0.35:
            screens[2] = [font.render('Displacement between frames:' +str(displacement), True, (0,0,0)), (0,30)]

            tick_count_displacement = 0

      
        screens[4] = [font.render('GA', True,(0,0,0)),(b1.centerx-20, b1.centery-5)]
        screens[5] = [font.render('MS', True, (0,0,0)),(b2.centerx-20, b2.centery-5)]
        screens[6] = [font.render('AD', True, (0,0,0)),(b3.centerx-20, b3.centery-5)]

        #draws buttons on the screen
        pygame.draw.rect(windowSurface, (0, 0, 0), bd1)
        pygame.draw.rect(windowSurface, (255, 255, 255), b1)

        pygame.draw.rect(windowSurface, (0, 0, 0), bd2)
        pygame.draw.rect(windowSurface, (255, 255, 255), b2)

        pygame.draw.rect(windowSurface, (0, 0, 0), bd3)
        pygame.draw.rect(windowSurface, (255, 255, 255), b3)

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