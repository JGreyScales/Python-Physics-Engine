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
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Physics engine')
 
 
def movements():
    player = pygame.Rect(WINDOWWIDTH/2, WINDOWHEIGHT/2, 20, 20)

    #gravity
    player_mass = 250
    speed = 0
    old_position = (0, 0)
    final_position = player.center
    time_old = 0
    time_current = float('0.' + datetime.now().strftime('%f'))
    velocity = 0

    while True:
    # Check for events.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            #updates cube onto mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.center = pygame.mouse.get_pos()
 

        # very basic gravity script
        if player.bottom < WINDOWHEIGHT:
            player.y += 1


        if float('0.'+datetime.now().strftime('%f')) - time_old > 0.00000001 or time_old - float('0.'+datetime.now().strftime('%f')) > 0.00000001:
            final_position = player.center
            time_current = float('0.' + datetime.now().strftime('%f'))

            print(round((final_position[0] - old_position[0])  / (float('0.'+datetime.now().strftime('%f')) - time_old), 2))

        time_old = time_current
        old_position = final_position
    # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))
 
        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, (0, 0, 0), player)
        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(120)
 
if __name__ == "__main__":
    movements()