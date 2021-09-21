import pygame
import math
import random


# create color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
colors = [RED, BLUE, GREEN, BLACK]

# create math constants
PI = math.pi

# to convert from degrees to radians angle * (pi / 180)
# 60* pi / 180 = pi / 3

# game constants
SIZE = (500, 500)           # (W, H)
FPS = 60                    # frames per second

##########################################################################
##########################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My First Pygame")

clock = pygame.time.Clock()

running = True

while running:

    # get all keyboard, mouse, joystick, etc events
    for event in pygame.event.get():

        # check for specific user event
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print("You pressed a key down")
            elif event.type == pygame.KEYUP:
                print("You pressed a key up")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("You clicked the mouse down")

    # game logic (objects fired, thrown, movement) goes here

    screen.fill(WHITE)

    # add drawings here
    pygame.draw.rect(screen, RED, [50,55, 200, 250], border_radius = 5)
    pygame.draw.arc(screen, RED, [275,55, 200, 250], 0, 5*PI/4, width = 5)
    for multiplier in range(10):
        color = random.choice(colors)
        pygame.draw.line(screen, color, (10 + 15*multiplier, 10), (75, 50), 5)

    pygame.display.flip()

    clock.tick(FPS)


# to be run after the main game loop
pygame.quit()
