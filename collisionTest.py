
# import required libraries 
import pygame 
import random 
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)
import sys
# initialize pygame objects 
pygame.init() 
  
# define the colours 
white = (255, 255, 255) 
red = (255, 0, 0) 
green = (0, 255, 0) 
blue = (0, 0, 255) 
black = (0, 0, 0) 
  
# set the Dimensions 
width = 650
height = 700
  
# size of a block 
pixel = 64
  
# set Screen 
screen = pygame.display.set_mode((width,  
                                  height)) 
  
# set caption 
pygame.display.set_caption("CORONA SCARPER") 
  
# load the image 
gameIcon = pygame.image.load("C:\Games\Random_World\Assets\Sprites\pumpking_walk\walk1.png") 
  
# set icon 
pygame.display.set_icon(gameIcon) 
  
# load the image 
#backgroundImg = pygame.image.load("C:\Games\Random_World\Assets\Textures\wall.png")


# load the image 
playerImage = pygame.image.load("C:\Games\Random_World\Assets\Sprites\pumpking_walk\walk10.png") 
  
# set the position 
playerXPosition = (width/2) - (pixel/2) 
  
# So that the player will be  
# at height of 20 above the base 
playerYPosition = height - pixel - 100     
  
# set initially 0 
playerXPositionChange = 0
  
# define a function for setting 
# the image at particular 
# coordinates 
def player(x, y): 
  # paste image on screen object 
  screen.blit(playerImage, (x, y)) 
  
# load the image 
blockImage = pygame.image.load("C:\Games\Random_World\Assets\Textures\wall.png") 
  
# set the random position 
blockXPosition = 100#random.randint(0, 
                 #               (width - pixel)) 
  
blockYPosition = 150
  
# set the speed of 
# the block 
blockXPositionChange = 0
blockYPositionChange = 20
  
# define a function for setting 
# the image at particular 
# coordinates 
def block(x, y): 
  # paste image on screen object 
  screen.blit(blockImage, 
              (x, y))
playerYPositionChange = 0
playerXPosition_history = 0
playerYPosition_history = 0



#def wall_detect(x1, y1, w1, h1, x2, y2, w2, h2):
#    return (x2+w2>=x1>=x2 or x2+w2>=x1+w1>=x2) and (y2+h2>=y1>=y2 or y2+h2>=y1+h1>=y2)

def is_collision(object_rect):
    #https://gamedev.stackexchange.com/questions/116195/pygame-collide-rect
    collision = False
    #for r in object_rect:
    if (object_rect.colliderect(my_rect)):
        collision = True

    return collision

collided = False
running = True
clock = pygame.time.Clock()

width_player = 150
height_player = 198

width_box = 64
height_box = 64
previous_collision = False

while running: 
# set the image on screen object 
    screen.fill((0,0,0))

    # loop through all events 
    for event in pygame.event.get(): 
            
        # check the quit condition 
        if event.type == pygame.QUIT: 
            # quit the game 
            running = False
            pygame.quit() 

        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
    pressed = pygame.key.get_pressed()
    

    block_rect = pygame.Rect(blockXPosition,blockYPosition, 64, 64)
    block_surf = pygame.Surface((64, 64), pygame.SRCALPHA)
    pygame.draw.rect(block_surf, (255, 0, 0), (0, 0, 64, 64), 1)

    my_rect = pygame.Rect(playerXPosition,playerYPosition, 150, 198)
    surf = pygame.Surface((150, 198), pygame.SRCALPHA)
    pygame.draw.rect(surf, (0, 100, 255), (0, 0, 150, 198), 1)

    screen.blit(block_surf, (blockXPosition, blockYPosition))
    screen.blit(surf, (playerXPosition, playerYPosition))
    
    #https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection

    if pressed[K_w]:

        playerYPositionChange = -3
        #playerXPosition += playerXPositionChange 
        playerYPosition += playerYPositionChange 
        my_rect.y+= playerYPositionChange
        
        collision = is_collision(block_rect)
        print('previous_collision:',previous_collision,'collision:',collision)
        if (collision):
            print('playerYPosition_history:',playerYPosition_history,'playerYPosition:',playerYPosition)
            if (playerYPosition < playerYPosition_history):
                playerYPosition = playerYPosition_history#block_rect.bottom
                my_rect.y       = playerYPosition_history
    if pressed[K_s]:
        playerYPositionChange = 3
        #playerXPosition += playerXPositionChange 
        playerYPosition += playerYPositionChange 
        my_rect.y += playerYPositionChange

        collision = is_collision(block_rect)
        if (collision):
            print('previous_collision:',previous_collision,'collision:',collision)
            print('playerYPosition_history:',playerYPosition_history,'playerYPosition:',playerYPosition)
            if (playerYPosition > playerYPosition_history):
                playerYPosition = playerYPosition_history#block_rect.top-height_player
                my_rect.y       = playerYPosition_history
    if pressed[K_d]:
        playerXPositionChange = 3
        playerXPosition += playerXPositionChange 
        my_rect.x  += playerXPositionChange

        collision = is_collision(block_rect)
        if (collision):
            print('previous_collision:',previous_collision,'collision:',collision)
            print('playerXPosition_history:',playerYPosition_history,'playerXPosition:',playerYPosition)
            if (playerXPosition > playerXPosition_history):
                print('playerXPosition_history:',playerYPosition_history,'playerXPosition:',playerYPosition)
                #sys.exit()
                playerXPosition = playerXPosition_history
                my_rect.x       = playerXPosition_history
                print('Are we entering here?')
    if pressed[K_a]:
        playerXPositionChange = -3
        playerXPosition += playerXPositionChange 
        my_rect.x  += playerXPositionChange

        collision = is_collision(block_rect)
        if (collision):
            print('previous_collision:',previous_collision,'collision:',collision)
            if (playerXPosition < playerXPosition_history):
                playerXPosition = playerXPosition_history
                my_rect.x  = playerXPosition_history
        
    playerXPosition_history = playerXPosition
    playerYPosition_history = playerYPosition
    # player Function Call 
    print(playerXPosition,playerYPosition,flush=True)
    player(playerXPosition, playerYPosition) 

    # block Function Call 
    block(blockXPosition, blockYPosition) 

    # crash function call 
    #crash() 
    
    # upadte screen 
    pygame.display.update()

    clock.tick(60)