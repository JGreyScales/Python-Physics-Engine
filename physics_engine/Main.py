from typing import final
import pygame, sys, math, tkinter
import time as time2
from datetime import *
from pygame.locals import *

from Assets.forumulas import formulas as formula

print(
    'all code can be found on https://github.com/JGreyScales/School-11/tree/main/physics_engine',
    '\n\n' + '-' * 50 +
    '\nTo use this program just left click the screen or left click and drag the screen to move the box, you can' +
    '\nclick the buttons on the right side to change variables inside the program and see how they affect the physics object'
)

formula = formula()

root = tkinter.Tk()
root.withdraw()


# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
start_width, start_height = round(root.winfo_screenwidth() * 0.9), round(root.winfo_screenheight() * 0.9)
windowSurface = pygame.display.set_mode((start_width, start_height), pygame.RESIZABLE)
pygame.display.set_caption('Physics engine')
current_width = start_width
current_height = start_height


def gameloop():
    global current_height, current_width
    ## defines player start position and size (Width, Height)
    player = pygame.Rect(current_width // 2, current_height // 2, 20, 20)
    # UI
    width_size, height_size = 1,1

    #velocity
    movement_vectors = (0, 0)

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
    mass = 300  #
    deltaTime = 0.0
    gravityAcceleration = 9.81  #
    velocity = 0
    air_density = 1.225  #
    projected_area = math.sqrt(list(player)[2] * list(player)[3])
    terminal_velocity = formula.calculate_terminal_velocity(
        mass, gravityAcceleration, 1.05, air_density, projected_area)

    #font to use for entire game
    font = pygame.font.Font('freesansbold.ttf', 15)
    button_font = pygame.font.Font('freesansbold.ttf', 10)

    # temp strings to increase range of list
    screens = [
        'Time_delta', 'Gravity Acceleration', 'Displacement', 'acceleration',
        'GA', 'MS', 'AD'
    ]

    # these screens in milliseconds not in frames so must be redefined before the render is called
    screens[2] = [
        font.render('Displacement between frames:' + str(displacement), True,
                    (0, 0, 0)), (0, 30)
    ]
    screens[3] = [
        font.render(f'Average Velocity is: {acceleration}pixels/2.5seconds',
                    True, (128, 45, 45)), (0, 45)
    ]

    # gets the amount of ticks that occured last frame
    getTicksLastFrame = pygame.time.get_ticks()

    #main gameloop
    while True:

        # Check for events.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.WINDOWSIZECHANGED:
                width_size, height_size = windowSurface.get_size()[0] / start_width, windowSurface.get_size()[1] / start_height
                if height_size < 0:
                    height_size = formula.inverse(10 / height_size)
                if width_size < 0:
                    width_size = formula.inverse(10 / width_size)
                    width_size += 1
                current_width = windowSurface.get_size()[0]
                current_height = windowSurface.get_size()[1]
                font = pygame.font.Font('freesansbold.ttf', round(15 * (width_size * height_size)))
                button_font = pygame.font.Font('freesansbold.ttf', round(10 * (width_size * height_size)))
                print(width_size * height_size)
            #updates cube onto mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                #updates variable and recalculates terminal_velocity
                if b1.collidepoint(event.pos):
                    try:
                        gravityAcceleration = float(
                            input(
                                "What do you want the Gravity Acceleration to be? "
                            ))
                        terminal_velocity = formula.calculate_terminal_velocity(
                            mass, gravityAcceleration, 1.05, air_density,
                            projected_area)
                    except (ValueError):
                        print('Please use a float')
                elif b2.collidepoint(event.pos):
                    try:
                        mass = float(
                            input("What do you want the Mass to be? "))
                        terminal_velocity = formula.calculate_terminal_velocity(
                            mass, gravityAcceleration, 1.05, air_density,
                            projected_area)
                    except (ValueError):
                        print('please use a float')
                elif b3.collidepoint(event.pos):
                    try:
                        mass = float(
                            input("What do you want the Air Density to be? "))
                        terminal_velocity = formula.calculate_terminal_velocity(
                            mass, gravityAcceleration, 1.05, air_density,
                            projected_area)
                    except (ValueError):
                        print('please use a float')
                # physics object or "player" will move to mouse position and resets the velocity on object
                else:
                    player.center = pygame.mouse.get_pos()
                    velocity = 0
            # checks if player is holding down left click
        if pygame.mouse.get_pressed()[0]:
            player.center = pygame.mouse.get_pos()
            velocity = 0
            if pygame.mouse.get_rel()[0] + pygame.mouse.get_rel()[1] != 0:
                movement_vectors = displacement
        else:
          if movement_vectors != 0:
            #code to throw object base on stored values
            #avg of movement vectors in past frame displacement = velocity.
            # 
            # also need to add a ticker so item loses velocity after
            #being held still
            pass

          movement_vectors = []
          

        # if the player is not on the bottom of the screen
        if player.bottom < current_height:
            # if velocity has hit or is equal to terminal_velocity
            if velocity <= -terminal_velocity:
                velocity = -terminal_velocity * deltaTime
                player.y -= velocity
                # if velocity is less then terminal_velocity
            elif velocity > -terminal_velocity:
                velocity -= gravityAcceleration * deltaTime / 1.05
                player.y -= velocity
        # is a check to stop clipping through the bottom of the screen
        elif player.bottom > current_height:
            player.bottom = current_height

        if player.right > current_width:
            player.right = current_width
        elif player.left < 0:
            player.left = 0

        # basic time delta script to calculate the delta between frames
        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        tick_count_displacement += deltaTime
        acceleration_count += deltaTime

        # Draw the white background onto the surface.
        windowSurface.fill((255, 255, 255))

        # calculates the displacement between frames
        current_pos = player.center
        displacement = math.sqrt((current_pos[0] - old_pos[0])**2 +
                                 (current_pos[1] - old_pos[1])**2)
        if displacement != 0:
            if displacement < -0:
                acceleration_list.append(formula.inverse(displacement))
            else:
                acceleration_list.append(displacement)
        old_pos = current_pos

        # every 2.5 seconds will update the average accelearation the physiscs object has moved in pixels
        if acceleration_count > 2.5:
            for displacement in acceleration_list:
                acceleration += displacement
            if len(acceleration_list) != 0:
                acceleration /= len(acceleration_list)
                acceleration = round(acceleration / 2.5, 2)
            else:
                acceleration = 0

            screens[3] = [
                font.render(
                    f'Average Acceleration is: {acceleration}pixels/2.5seconds',
                    True, (128, 0, 0)), (0, round(45 * (width_size * height_size)))
            ]

            acceleration_list = []
            acceleration_count = 0

            #button creation
        bd1 = pygame.Rect((current_width - 65), 5, 60, 30)
        b1 = pygame.Rect(current_width - 63, 7, 56, 26)

        bd2 = pygame.Rect(current_width - 65, 40, 60, 30)
        b2 = pygame.Rect(current_width - 63, 42, 56, 26)

        bd3 = pygame.Rect(current_width - 65, 75, 60, 30)
        b3 = pygame.Rect(current_width - 63, 77, 56, 26)

        # Draw the player onto the surface.
        pygame.draw.rect(windowSurface, (0, 0, 0), player)
        #updates text on screen blits
        screens[0] = [
            font.render('Delta Time:' + str(deltaTime), True, (0, 0, 0)),
            (0, 0)
        ]
        screens[1] = [
            font.render('Gravity Acceleration:' + str(gravityAcceleration),
                        True, (0, 0, 0)), (0, round(15 * (width_size * height_size)))
        ]

        #updates displacement on change or every 0.35 seconds
        if displacement > 3 or displacement < 0 or tick_count_displacement > 0.35:
            screens[2] = [
                font.render(
                    'Displacement between frames:' +
                    str(round(displacement, 2)), True, (0, 0, 0)), (0, round(30 * (width_size * height_size)))
            ]

            tick_count_displacement = 0

    # font rendering for buttons
        screens[4] = [
            button_font.render('Gravity', True, (0, 0, 0)),
            (b1.centerx - 15, b1.centery - 5)
        ]
        screens[5] = [
            button_font.render(f'Mass: {round(mass)} ', True, (0, 0, 0)),
            (b2.centerx - 24, b2.centery - 5)
        ]
        screens[6] = [
            button_font.render('Air Drag', True, (0, 0, 0)),
            (b3.centerx - 20, b3.centery - 5)
        ]

        #renders buttons on the screen
        pygame.draw.rect(windowSurface, (0, 0, 0), bd1)
        pygame.draw.rect(windowSurface, (255, 255, 255), b1)

        pygame.draw.rect(windowSurface, (0, 0, 0), bd2)
        pygame.draw.rect(windowSurface, (255, 255, 255), b2)

        pygame.draw.rect(windowSurface, (0, 0, 0), bd3)
        pygame.draw.rect(windowSurface, (255, 255, 255), b3)

        # render loop (will iterate through all items that need to be rendered and render them)
        for i in range(len(screens)):
            windowSurface.blit(screens[i][0], screens[i][1])

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:

            # Draw the window onto the screen.
            pygame.display.update()
        mainClock.tick(144)
            



# init of gameloop
gameloop()
