import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time # Takes time since program starts and subtracts is from last game ended in milliseconds
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle) # Places current score surface (current time in seconds) on screen
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list: # If statement will not run if the list is empty
        for obstacle_rectangle in obstacle_list: # Looks through every obstacle in the obstacle list
            obstacle_rectangle.x -= 5 # Moving the rectangle to the right

            if obstacle_rectangle.bottom == 300: screen.blit(snail_surface,obstacle_rectangle) # Drawing snail surface if x is 300
            else: screen.blit(fly_surface,obstacle_rectangle) # Else draw fly surface

        # Only copy and existing object in list if x is greater than 0, deletes obstacles that go off screen
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list # Returns the obstacles that are still of screen
    else: return [] # Allows .append to work when obstacle list is empty

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rectangle in obstacles:
            if player.colliderect(obstacle_rectangle): return False
    return True

# Display surface is the main window the player can see, only can have one and always visable
# Use regular surfaces to put images on the display surface (imported image, color, text)
# Can have multiple regular surfaces, only visable when on display surface

pygame.init() # Run this before any other pygame code, starts pygame and initiates sub-parts
screen = pygame.display.set_mode((800,400)) # Display surface, window player will see, needs a tuple (width, height)
pygame.display.set_caption('Runner') # Adds title to game window
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50) # (font type, font size), None - default font
game_active = False
start_time = 0 # 0 or the amount of seconds that have passed from previous game
score = 0 # Amount of seconds current game has been running

sky_surface = pygame.image.load('graphics/Sky.png').convert() # Converts image into something pygame can use more easily
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surface = test_font.render('My game', False, (64,64,64)) # (text, anti aliasing, color), anti aliasing - smooth edges of text
# score_rectangle = score_surface.get_rect(center = (400,50))

# Obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # Removes the alpha values

fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rectangle_list = [] # Holds list of obstacles that are currently on screen

# Player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# Rectangles making positioning images on game window easier, set origin point in different spot, not just top left
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2) # Arguments - surface, angle, scale
player_stand_rectangle = player_stand.get_rect(center = (400,200))

game_title = test_font.render('Pixel Runner',False,(111,196,169))
game_title_rectangle = game_title.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rectangle = game_message.get_rect(center = (400,320))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # There are some events reserved for pygame, to avoid conflict, add plus 1 to each event we add
pygame.time.set_timer(obstacle_timer,1500) # Arguments - event we want to trigger, how often we want to trigger it in milliseconds

# Use while true loop so window doesn't disappear right away
# Use clock object so there is a consistant frame rate

while True:
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # Closes any kind of code when called
        if game_active:
            # Player input
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.collidepoint(event.pos): # only triggers when mouse button is pressed
                    if player_rectangle.bottom == 300: # Only allows player to jump when on the ground
                        player_gravity = -20 # Allows player to jump if there is negative gravity

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom == 300:
                        player_gravity = -20
            if event.type == obstacle_timer:
                if randint(0,2): # Randomly triggers true or false, gives values 0 or 1, spawns fly and snail randomly
                    obstacle_rectangle_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300))) # Adds snail to obstacle list
                else:
                    obstacle_rectangle_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210))) # Adds fly to obstacle list
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Checks if key is pressed down and if space bar is pressed
                game_active = True # Starts the game again
                start_time = int(pygame.time.get_ticks() / 1000) # Sets the start time to time since pygame started in milliseconds

    if game_active:
        # Background
        # Origin point (0,0) is in top left, increase x goes right, increase y goes down
        # Put surfaces on screen in order of when it is called, ex: sky not visible if sky and ground in same position and same size
        screen.blit(sky_surface,(0,0)) # Block Image Transfer, put one surface on another suface, (surface, position)
        screen.blit(ground_surface,(0,300))

        # Score text
        # pygame.draw.rect(screen,(169,211,219),score_rectangle) # arguments - surface, color, rectangle (optional - width and others)
        # pygame.draw.rect(screen,(169,211,219),score_rectangle,6) # only draws border and not the middle too
        # screen.blit(score_surface,score_rectangle)
        score = display_score()

        #Snail
        # snail_rectangle.x -= 4 # move the rectangle that contains the surface
        # if snail_rectangle.right <= 0: snail_rectangle.left = 800 # If snail moves off screen from left side, move position to right side
        # screen.blit(snail_surface,snail_rectangle)

        #Player
        player_gravity += 1
        player_rectangle.y += player_gravity # Moves player down at increasing rate
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300 # Prevents player from falling below ground
        screen.blit(player_surface,player_rectangle)

        # Obstacle movment
        # Function moves all rectangles in list to the right on game screen and then override previous list
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)

        # Collision
        game_active = collisions(player_rectangle,obstacle_rectangle_list)
        
    else:
        # Game over / Start Screen
        screen.fill((94,129,162)) # Background color
        screen.blit(player_stand,player_stand_rectangle) # Image of player
        obstacle_rectangle_list.clear() # Removes all obstacles from previous game
        player_rectangle.midbottom = (80,300) # Player always starts on ground
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rectangle = score_message.get_rect(center = (400,330))
        screen.blit(game_title,game_title_rectangle)

        if score == 0: screen.blit(game_message,game_message_rectangle) # If first time opening game, display message
        else: screen.blit(score_message,score_message_rectangle) # Else, display previous score

        # Updates everything
    pygame.display.update() # Updates display surface made before loop
    clock.tick(60) # While loop shouldn't run faster than 60 times per second