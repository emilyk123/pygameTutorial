import pygame
from sys import exit

# display surface is the main window the player can see, only can have one and always visable
# use regular surfaces to put images on the display surface (imported image, color, text)
# regular surfaces can have multiple regular surfaces, only visable when on display surface

pygame.init() # run this before any other pygame code, starts pygame and initiates sub-parts
screen = pygame.display.set_mode((800,400)) # display surface, window player will see, needs a tuple (width, height)
pygame.display.set_caption('Runner') # adds title to game window
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50) # (font type, font size), None - default font
BLACK = (0,0,0)

sky_surface = pygame.image.load('graphics/Sky.png').convert() # converts image into something pygame can use more easily
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, BLACK) # (text, anti aliasing, color), anit aliasing - smooth edges of text

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # removes the alpha values
snail_rectangle = snail_surface.get_rect(midbottom = (600,300))
snail_x_pos = 600

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# rectangles making positioning images on game window easier, set origin point in different spot, not just top left
player_rectangle = player_surface.get_rect(midbottom = (80,300))

# use while true loop so window doesn't disappear right away
# use clock object so there is a consistant frame rate

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # closes any kind of code when called
        # if event.type == pygame.MOUSEMOTION: # gives mouse position, only triggers when mouse moves
        #     if player_rectangle.collidepoint(event.pos): print('collision')

    # origin point (0,0) is in top left, increase x goes right, increase y goes down
    # put on screen in order of when it is called, ex: sky not visible if sky and ground in same position and same size
    screen.blit(sky_surface,(0,0)) # Block Image Transfer, put one surface on another suface, (surface, position)
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rectangle.x -= 4 # move the rectangle that contains the surface, not the surface
    if snail_rectangle.right <= 0: snail_rectangle.left = 800
    screen.blit(snail_surface,snail_rectangle)
    screen.blit(player_surface,player_rectangle)

    # if player_rectangle.colliderect(snail_rectangle):  # returns a 0 or 1, can trigger multiple times
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos): # tuple with x and y positions, point to measure if it is inside rectangle
    #     print(pygame.mouse.get_pressed())

    # draw all our elements
    # update everything
    pygame.display.update() # updates display surface made before loop
    clock.tick(60) # while loop shouldn't run faster than 60 times per second