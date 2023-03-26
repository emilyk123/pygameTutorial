import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time # give time in milliseconds
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)

# display surface is the main window the player can see, only can have one and always visable
# use regular surfaces to put images on the display surface (imported image, color, text)
# can have multiple regular surfaces, only visable when on display surface

pygame.init() # run this before any other pygame code, starts pygame and initiates sub-parts
screen = pygame.display.set_mode((800,400)) # display surface, window player will see, needs a tuple (width, height)
pygame.display.set_caption('Runner') # adds title to game window
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50) # (font type, font size), None - default font
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert() # converts image into something pygame can use more easily
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surface = test_font.render('My game', False, (64,64,64)) # (text, anti aliasing, color), anti aliasing - smooth edges of text
# score_rectangle = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # removes the alpha values
snail_rectangle = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# rectangles making positioning images on game window easier, set origin point in different spot, not just top left
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

# use while true loop so window doesn't disappear right away
# use clock object so there is a consistant frame rate

while True:
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # closes any kind of code when called
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.collidepoint(event.pos): # only triggers when mouse button is pressed
                    if player_rectangle.bottom == 300:
                        player_gravity = -20

            # Player input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom == 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        # Background
        # origin point (0,0) is in top left, increase x goes right, increase y goes down
        # put surfaces on screen in order of when it is called, ex: sky not visible if sky and ground in same position and same size
        screen.blit(sky_surface,(0,0)) # Block Image Transfer, put one surface on another suface, (surface, position)
        screen.blit(ground_surface,(0,300))

        # Score text
        # pygame.draw.rect(screen,(169,211,219),score_rectangle) # arguments - surface, color, rectangle (optional - width and others)
        # pygame.draw.rect(screen,(169,211,219),score_rectangle,6) # only draws border and not the middle too
        # screen.blit(score_surface,score_rectangle)
        display_score()

        #Snail
        snail_rectangle.x -= 4 # move the rectangle that contains the surface
        if snail_rectangle.right <= 0: snail_rectangle.left = 800
        screen.blit(snail_surface,snail_rectangle)

        #Player
        player_gravity += 1
        player_rectangle.y += player_gravity # Moves player down at increasing rate
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300 # prevents player from falling below ground
        screen.blit(player_surface,player_rectangle)

        # Collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill((0,255,0))

        # update everything
    pygame.display.update() # updates display surface made before loop
    clock.tick(60) # while loop shouldn't run faster than 60 times per second