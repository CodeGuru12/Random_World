# Import the pygame module

import pygame
from common_utilities import *
from time import time
# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

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

SPEED = 15
# Setup the clock for a decent framerate
clock = pygame.time.Clock()


#Constants
SCREENS = 3

SPRITE_SIZE = (150,198)
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

worldMaxX = SCREEN_SIZE[0]*SCREENS
worldMaxY = SCREEN_SIZE[1]*SCREENS



class FrameRate():
    def __init__(self,dT):
        self.previousTime = 0
        self.currentTime  = 0
        self.elapsed_time = 0
        self.dT           = dT

    def integrate_state(self,callback,*args):
        '''
        
        '''
        self.callback = callback
        self.currentTime = int(time()*1000)

        self.elapsed_time += self.currentTime - self.previousTime
        if (DEBUG):
            print('self.elapsed_time:',self.elapsed_time)
        self.previousTime = self.currentTime
        if (self.elapsed_time >= int(self.dT)): 
            if (DEBUG):
                print('self.elapsed_time:',self.elapsed_time)
            #Call function after elapsed time    
            self.callback(*args)
            #Reset elapsed time
            self.elapsed_time = 0

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

    def updateCamera(self,position):
        #Move player to other side of screen when crossing screens
        if (position.x < -SPRITE_SIZE[0] and self.screen[0] != 0):
            position.x = SCREEN_SIZE[0]
            if (self.screen[0] >= 1):
                self.screen[0] -= 1

        elif (position.x > SCREEN_SIZE[0] and self.screen[0] != 2):
            position.x = 0
            if (self.screen[0] < SCREENS-1):
                self.screen[0] += 1

        if (position.y < -25 and self.screen[1] != 0):
            position.y += SCREEN_SIZE[1]
            if (self.screen[1] >= 1):
                self.screen[1] -= 1
        elif (position.y > SCREEN_SIZE[1] and self.screen[1] != 2):
            position.y = 0
            if (self.screen[1] < SCREENS-1):
                self.screen[1] += 1

        #Prevent player from leaving edge of map
        if (position.x < 0 and self.screen[0] == 0):
            position.x = 0
        elif (position.x > SCREEN_SIZE[0]-SPRITE_SIZE[0] and self.screen[0] == 2):
            position.x = SCREEN_SIZE[0]-SPRITE_SIZE[0]

        if (position.y < 0 and self.screen[1] == 0):
            position.y = 0
            
        if (position.y > SCREEN_SIZE[1]-SPRITE_SIZE[1] and self.screen[1] == 2):
            position.y = SCREEN_SIZE[1]-SPRITE_SIZE[1]

        if (DEBUG):
            print('self.screen:',self.screen)
            print('self.worldX:',self.worldX)
            print('self.worldY:',self.worldY)

            print('self.rect.x:',position.x)
            print('self.rect.y:',position.y)

        return self.screen

class Player(Camera):
    def __init__(self):
        super(Player,self).__init__()
        self.orientation = 'Right'
        self.images = []
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk1.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk2.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk3.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk4.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk5.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk6.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk7.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk8.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk9.png'))
        self.images.append(pygame.image.load('C:/Games/Random_World/Assets/Sprites/pumpking_walk/walk10.png'))
 
        self.index = 0
 
        self.image = self.images[self.index]

        self.position = struct(x=0,y=0)
    def update(self, pressed_keys):
        global SPEED
        if (pressed_keys[K_UP]):
            SPEED += 1
            print('SPEED:',SPEED,flush=True)
        elif (pressed_keys[K_DOWN]):
            SPEED -= 1
            print('SPEED:',SPEED,flush=True)
            if (SPEED <= 0):
                SPEED = 0
                
        if self.index > len(self.images)-1:
            self.index = 0
        # Move the SPRITE_SIZE based on user keypresses
        if pressed_keys[K_w]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
            self.worldY -= SPEED
            self.orientation = 'Right'
            self.image = self.images[self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
        
        if self.index > len(self.images)-1:
            self.index = 0

        if pressed_keys[K_s]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
            self.worldY += SPEED
            self.orientation = 'Left'
            self.image = self.images[self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)

        if self.index > len(self.images)-1:
            self.index = 0

        if pressed_keys[K_a]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
            self.worldX -= SPEED
            self.orientation = 'Left'
            self.image = self.images[self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)

        if self.index > len(self.images)-1:
            self.index = 0

        if pressed_keys[K_d]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
            self.worldX += SPEED
            self.orientation = 'Right'
            self.image = self.images[self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
        
        if ((not pressed_keys[K_a]) and (not pressed_keys[K_s]) 
             and (not pressed_keys[K_w]) and (not pressed_keys[K_d])):
            self.image = self.images[0]

    def render(self,surface,position):
        if self.orientation == "Right":
            screen.blit(surface, (position.x,position.y))
        elif self.orientation == "Left":
            screen.blit(pygame.transform.flip(surface, True, False), (position.x,position.y))

class Map():
    def __init__(self,world):
        self.map = world
        self.map_view = PURPLE
    def update(self,coordinates):
        self.map_view = self.map[coordinates[0]][coordinates[1]]
        if (DEBUG):
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

frame = FrameRate(100)

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



    frame.integrate_state(player.update,pressed_keys)
    worldScreen = player.updateCamera(player.position)
    world.update(worldScreen)
    world.render(screen)
    # Draw the player on the screen
    player.render(player.image,player.position)



    # Update the display
    pygame.display.update()

    #clock.tick(5)
