import pygame
from sys import exit

# display surface is the main window the player can see, only can have one and always visable
# use regular surfaces to put images on the display surface (imported image, color, text)
# regular surfaces can have multiple regular surfaces, only visable when on display surface

pygame.init() # run this before any other pygame code, starts pygame and initiates sub-parts
screen = pygame.display.set_mode((800,400)) # display surface, window player will see, needs a tuple (width, height)
pygame.display.set_caption('Runner') # adds title to game window
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200)) # regular surface, needs tuple (width, height)
RED = (255,0,0)
test_surface.fill(RED)

# use while true loop so window doesn't disappear right away
# use clock object so there is a consistant frame rate

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # closes any kind of code when called

    # origin point (0,0) is in top left, increase x goes right, increase y goes down
    screen.blit(test_surface,(0,0)) # Block Image Transfer, put one surface on another suface, (surface, position)

    # draw all our elements
    # update everything
    pygame.display.update() # updates display surface made before loop
    clock.tick(60) # while loop shouldn't run faster than 60 times per second