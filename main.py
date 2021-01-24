# Import the pygame module

import pygame


# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

BLUE = (0,0,255)
PURPLE = (153,50,204)
GREEN = (0,128,0)

MAP = [[BLUE, GREEN, BLUE],
       [GREEN, PURPLE, GREEN],
       [PURPLE, GREEN, BLUE]]

DEBUG = False
        
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 8
# Setup the clock for a decent framerate
clock = pygame.time.Clock()


#Constants
SCREENS = 3

SPRITE_SIZE = (25,25)
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

worldMaxX = SCREEN_SIZE[0]*SCREENS
worldMaxY = SCREEN_SIZE[1]*SCREENS

class Camera():
    def __init__(self):
        self.worldX = 1000
        self.worldY = 1000
        self.cameraX = SCREEN_SIZE[0]
        self.cameraY = SCREEN_SIZE[1]
        self.screen = [2, 2]
    def worldCoordinates(self,screenX, screenY):
        worldX = self.screen[0]*SCREEN_SIZE[0] + screenX
        worldY = self.screen[1]*SCREEN_SIZE[1] + screenY
        return (worldX, worldY)

    def screenCoordinates(self,worldX, worldY):
        screenX = worldX - self.screen[0]*SCREEN_SIZE[0]
        screenY = worldY - self.screen[1]*SCREEN_SIZE[1]
        return (screenX,screenY)

class Player(Camera):
    def __init__(self):
        super(Player,self).__init__()
        self.player_surface = pygame.Surface(SPRITE_SIZE)
        self.player_surface.fill((255, 0, 255))
        self.rect = self.player_surface.get_rect(center = SPRITE_SIZE)
        
    def update(self, pressed_keys):
        # Move the SPRITE_SIZE based on user keypresses
        if pressed_keys[K_w]:
            self.worldX,self.worldY = self.worldCoordinates(self.rect.x,self.rect.y)
            self.worldY -= SPEED
            
            self.rect.x,self.rect.y =  self.screenCoordinates(self.worldX,self.worldY)

        if pressed_keys[K_s]:
            self.worldX,self.worldY = self.worldCoordinates(self.rect.x,self.rect.y)
            self.worldY += SPEED

            self.rect.x,self.rect.y =  self.screenCoordinates(self.worldX,self.worldY)

        if pressed_keys[K_a]:
            self.worldX,self.worldY = self.worldCoordinates(self.rect.x,self.rect.y)
            self.worldX -= SPEED

            self.rect.x,self.rect.y =  self.screenCoordinates(self.worldX,self.worldY)

        if pressed_keys[K_d]:
            self.worldX,self.worldY = self.worldCoordinates(self.rect.x,self.rect.y)
            self.worldX += SPEED
            
            self.rect.x,self.rect.y =  self.screenCoordinates(self.worldX,self.worldY)




    def updateCamera(self,pressed_keys):
        # Keep player on the screen
        #self.rect.left,self.rect.right = self.screenCoordinates(self.worldX,self.worldY)

    
        #Move player to other side of screen when crossing screens
        if (pressed_keys[K_w] or pressed_keys[K_s] or pressed_keys[K_d] or pressed_keys[K_a]):
            if (self.rect.x < -SPRITE_SIZE[0] and self.screen[0] != 0):
                self.rect.x = SCREEN_SIZE[0]
                if (self.screen[0] >= 1):
                    self.screen[0] -= 1

            elif (self.rect.x > SCREEN_SIZE[0] and self.screen[0] != 2):
                self.rect.x = 0
                if (self.screen[0] < SCREENS-1):
                    self.screen[0] += 1

            if (self.rect.y < -25 and self.screen[1] != 0):
                self.rect.y += SCREEN_SIZE[1]
                if (self.screen[1] >= 1):
                    self.screen[1] -= 1
            elif (self.rect.y > SCREEN_SIZE[1] and self.screen[1] != 2):
                self.rect.y = 0
                if (self.screen[1] < SCREENS-1):
                    self.screen[1] += 1

        #Prevent player from leaving edge of map
        if (self.rect.x < 0 and self.screen[0] == 0):
            self.rect.x = 0
        elif (self.rect.x > SCREEN_SIZE[0]-SPRITE_SIZE[0] and self.screen[0] == 2):
            self.rect.x = SCREEN_SIZE[0]-SPRITE_SIZE[0]

        if (self.rect.y < 0 and self.screen[1] == 0):
            self.rect.y = 0
            
        if (self.rect.y > SCREEN_SIZE[1]-SPRITE_SIZE[1] and self.screen[1] == 2):
            self.rect.y = SCREEN_SIZE[1]-SPRITE_SIZE[1]

        if (DEBUG):
            print('self.screen:',self.screen)
            print('self.worldX:',self.worldX)
            print('self.worldY:',self.worldY)

            print('self.rect.x:',self.rect.x)
            print('self.rect.y:',self.rect.y)

        return self.screen

    def render(self,position):
        screen.blit(self.player_surface, position)


class Map():
    def __init__(self,world):
        self.map = world
        self.map_view = PURPLE
    def update(self,coordinates):
        self.map_view = self.map[coordinates[0]][coordinates[1]]
        print('self.map_view:',self.map_view)
    def render(self,screen):
        screen.fill(self.map_view)

# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_SIZE[0] and SCREEN_SIZE[1]
screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))


# Instantiate player. Right now, this is just a rectangle.
player = Player()
#Instantiate map, takes list of lists map to be rendered
world = Map(MAP)

# Variable to keep the main loop running
running = True


# Main loop
while running:

    # for loop through the event queue

    for event in pygame.event.get():
        # Check for KEYDOWN event

        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    player.update(pressed_keys)
    worldScreen = player.updateCamera(pressed_keys)
    world.update(worldScreen)
    world.render(screen)
    # Draw the player on the screen
    player.render(player.rect)



    # Update the display
    pygame.display.flip()

    clock.tick(60)
