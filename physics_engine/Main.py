import pygame, sys, random
from pygame.locals import *
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
 
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
 
    MOVESPEED = 1
    while True:
    # Check for events.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #updates cube onto mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.center = pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())
 
        if player.bottom < WINDOWHEIGHT:
            player.y += 1
    # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))
 
        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, (0, 0, 0), player)
        # Draw the window onto the screen.
        pygame.display.update()
        mainClock.tick(120)
 
if __name__ == "__main__":
    movements()