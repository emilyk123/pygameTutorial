import pygame
from sys import exit

pygame.init() # run this before any other pygame code, starts pygame and initiates sub-parts
screen = pygame.display.set_mode((800, 400)) # display surface, window player will see

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # closes any kind of code when called
    # draw all our elements
    # update everything
    pygame.display.update() # updates display surface made before loop