# Import the pygame module

import pygame
from common_utilities import *
from time import time
import worldBuilder
import spriteManager
from spriteManager import options
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

SIZE = 0
MAP = [[BLUE, GREEN, BLUE],
       [GREEN, PURPLE, GREEN],
       [PURPLE, GREEN, BLUE]]

MAP = [[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]]

DEBUG = False
        
# Define constants for the screen width and height
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


#Constants
SCREENS = 3

SPRITE_SIZE = (64,64)
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
        self.elapsed_time += (self.currentTime - self.previousTime)
        #print('self.elapsed_time:',self.elapsed_time)
        self.previousTime = self.currentTime
        if (self.elapsed_time >= (1 / int(self.dT)*1000)): 
            #if (DEBUG):
                #print('self.elapsed_time:',self.elapsed_time)
            #Call function after elapsed time    
            self.callback(*args)
            #Reset elapsed time
            self.elapsed_time = 0

        return self.elapsed_time

class Camera():
    def __init__(self):
        self.worldX = 1000
        self.worldY = 1000
        self.cameraX = SCREEN_SIZE[0]
        self.cameraY = SCREEN_SIZE[1]
        self.screen = [2, 2]
        self.updateScreen = False
    def worldCoordinates(self,screenX, screenY):
        worldX = self.screen[0]*SCREEN_SIZE[0] + screenX
        worldY = self.screen[1]*SCREEN_SIZE[1] + screenY
        return (worldX, worldY)

    def screenCoordinates(self,worldX, worldY):
        screenX = worldX - self.screen[0]*SCREEN_SIZE[0]
        screenY = worldY - self.screen[1]*SCREEN_SIZE[1]
        return (screenX,screenY)

    def updateCamera(self,position):
        #Assume map will not be updated this loop
        self.updateScreen = False
        #Move player to other side of screen when crossing screens
        if (position.x < -SPRITE_SIZE[0] and self.screen[0] != 0):
            position.x = SCREEN_SIZE[0]
            if (self.screen[0] >= 1):
                self.screen[0] -= 1
                self.updateScreen = True

        elif (position.x > SCREEN_SIZE[0] and self.screen[0] != 2):
            position.x = 0
            if (self.screen[0] < SCREENS-1):
                self.screen[0] += 1
                self.updateScreen = True
        if (position.y < 0 and self.screen[1] != 0):
            position.y += SCREEN_SIZE[1]
            if (self.screen[1] >= 1):
                self.screen[1] -= 1
                self.updateScreen = True
        elif (position.y > SCREEN_SIZE[1] and self.screen[1] != 2):
            position.y = 0
            if (self.screen[1] < SCREENS-1):
                self.screen[1] += 1
                self.updateScreen = True
        #Prevent player from leaving edge of map
        if (position.x < 0 and self.screen[0] == 0):
            position.x = 0
        elif (position.x > SCREEN_SIZE[0]-SPRITE_SIZE[0] and self.screen[0] == 2):
            position.x = SCREEN_SIZE[0]-SPRITE_SIZE[0]

        if (position.y < 0 and self.screen[1] == 0):
            position.y = 0
            
        if (position.y > SCREEN_SIZE[1]-SPRITE_SIZE[1] and self.screen[1] == 2):
            position.y = SCREEN_SIZE[1]-SPRITE_SIZE[1]

        #if (False):
            #print('self.screen:',self.screen)
            #print('self.worldX:',self.worldX)
            #print('self.worldY:',self.worldY)

            #print('self.rect.x:',position.x)
            #print('self.rect.y:',position.y)

        return (self.screen,self.updateScreen)



class Player(Camera):
    def __init__(self):
        super(Player,self).__init__()
        self.orientation = 'Right'
        #ss = spritesheet(get_file_path('/Assets/Sprites/Walk_sprite_sheet.png'))
        ss = spriteManager.spritesheet(get_file_path('/Assets/Sprites/main_character.png'),options.CONVERTALPHA)
        # Sprite is 16x16 pixels at location 0,0 in the file...
        #load_sheet(self,width,height,rows,image_count, colorkey = None)
        self.sheet = ss.load_sheet(96,144,4,3)
        #self.images = ss.load_strip((0, 0, 64, 64),9,(255,255,255))
        self.index = 1
        #self.image = self.images[self.index]
        self.image = self.sheet[0][self.index]
        self.position = struct(x=150,y=150)
        self.history = struct(x=0,y=0)
        self.iso_position = struct(x=0,y=0)
        self.offset = struct(x=10,y=10)
        self.size_offset = struct(x=5,y=5)
        self.my_rect = pygame.Rect(self.iso_position.x+self.offset.x,  \
                                  self.iso_position.y+self.offset.y,   \
                                   96-self.size_offset.x, 144-self.size_offset.y)
        self.collisionSurf = pygame.Surface((96-self.size_offset.x, 144-self.size_offset.y), pygame.SRCALPHA)
        self.speed = 400
        ##print('self.rect:',self.rect)
    def update(self, pressed_keys,deltaT,sprite):#,self.is_collision,sprite):


        self.position.x, self.position.y = self.move(pressed_keys,deltaT,sprite)
        self.iso_position.x, self.iso_position.y = convert_to_iso(self.position.x,self.position.y)
        




    def move(self,pressed_keys,deltaT,sprite):
        global SIZE
        self.my_rect = pygame.Rect(self.position.x,self.position.y, 70, 131)
        #print(deltaT,flush=True)
        if (pressed_keys[K_UP]):
            SIZE += 1
            #print('SIZE:',SIZE,flush=True)
        elif (pressed_keys[K_DOWN]):
            SIZE -= 1
            #print('SIZE:',SIZE,flush=True)

        if self.index > len(self.sheet[0])-1:
            self.index = 0
        # Move the SPRITE_SIZE based on user keypresses
        if pressed_keys[K_w]: #up to left
            #self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
            #Allow movement only if collision not detected
                ##print('self.is_collision(sprite):',self.is_collision(sprite))
            self.position.x -= self.speed * deltaT
            self.iso_position.x, self.iso_position.y = convert_to_iso(self.position.x,self.position.y)
            self.my_rect.x = self.iso_position.x
            self.my_rect.y = self.iso_position.y
            #print('self.my_rect.x: ',self.my_rect.x)
            #print('self.my_rect.y: ',self.my_rect.y)
            #print('self.position.x: ',self.iso_position.x)
            #print('self.position.y: ',self.iso_position.y)
            if(self.is_collision(sprite)):
               self.position.x = self.history.x
            self.orientation = 'Left'
            self.image = self.sheet[1][self.index]
            self.index += 1
        
        if self.index > len(self.sheet[0])-1:
            self.index = 0

        if pressed_keys[K_s]: #down to right
            #self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
                ##print('self.is_collision(sprite):',self.is_collision(sprite))
            self.position.x += self.speed * deltaT
            #self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.iso_position.x, self.iso_position.y = convert_to_iso(self.position.x,self.position.y)
            self.my_rect.x = self.iso_position.x
            self.my_rect.y = self.iso_position.y
            if(self.is_collision(sprite)):
               self.position.x = self.history.x
            self.orientation = 'Right'
            self.image = self.sheet[1][self.index]
            self.index += 1


        if self.index > len(self.sheet[0])-1:
            self.index = 0

        if pressed_keys[K_a]:
            #self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)

                ##print('self.is_collision(sprite):',self.is_collision(sprite))
            self.position.y += self.speed * deltaT
            #self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.iso_position.x, self.iso_position.y = convert_to_iso(self.position.x,self.position.y)
            self.my_rect.x = self.iso_position.x
            self.my_rect.y = self.iso_position.y
            if(self.is_collision(sprite)):
               self.position.y = self.history.y
            self.orientation = 'Left'
            self.image = self.sheet[1][self.index]
            self.index += 1


        if self.index > len(self.sheet[0])-1:
            self.index = 0

        if pressed_keys[K_d]:
            #self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)

            ##print('self.is_collision(sprite):',self.is_collision(sprite))
            self.position.y -= self.speed * deltaT
            #self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.iso_position.x, self.iso_position.y = convert_to_iso(self.position.x,self.position.y)
            self.my_rect.x = self.iso_position.x
            self.my_rect.y = self.iso_position.y
            if(self.is_collision(sprite)):
               self.position.y = self.history.y
            self.orientation = 'Right'
            self.image = self.sheet[1][self.index]
            self.index += 1


        #Supposed to have a default rest image when not walking
        if ((not pressed_keys[K_a]) and (not pressed_keys[K_s]) 
             and (not pressed_keys[K_w]) and (not pressed_keys[K_d])):
            self.image = self.sheet[0][1]

        #Save position history for collisions
        self.history.x = self.position.x
        self.history.y = self.position.y

        return self.position.x,self.position.y

    def render(self,surface):
        if self.orientation == "Left":
            screen.blit(surface, (self.iso_position.x,self.iso_position.y))
        elif self.orientation == "Right":
            screen.blit(pygame.transform.flip(surface, True, False), (self.iso_position.x,self.iso_position.y))

    def get_rect(self):
        return pygame.Rect(self.position.x,self.position.y, 64, 64)
    
    def is_collision(self,object_rect):
        #https://gamedev.stackexchange.com/questions/116195/pygame-collide-rect
        collision = False
        #print('object_rect.rect: ',object_rect.rect)
        for r in object_rect.rect:
            if (r.colliderect(self.my_rect)):
                collision = True
            #print('collision:',collision,flush=True)
        return collision
    
# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_SIZE[0] and SCREEN_SIZE[1]
screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]),pygame.DOUBLEBUF)

frameRate = 6
# Instantiate player. Right now, this is just a rectangle.
player = Player()
#Instantiate map, takes list of lists map to be rendered
world = worldBuilder.Map(worldBuilder.map)

# Variable to keep the main loop running
running = True

frame = FrameRate(frameRate)
clock = pygame.time.Clock()
# Main loop

def main():

    screen.fill((0,0,0))
    player.update(pressed_keys,world)#,world.is_collided_with,player)
    #Returns worldScreen coordinates, whether the map should be updated
    #world.is_collided_with(player.rect)

    #worldScreen,updateMap = player.updateCamera(player.iso_position)
    player.render(player.image)
    world.update((0,0))
    world.render(screen,False)
    # Draw the player on the screen


deltaT = 0

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

    screen.fill((0,0,0))
    deltaT = frame.integrate_state(player.update,pressed_keys,deltaT/1000,world)#,world.is_collided_with,player)
    pygame.draw.rect(player.collisionSurf, (0, 0, 150), (0,0, 96-player.size_offset.x, 144-player.size_offset.y), 1)
    screen.blit(player.collisionSurf, (player.iso_position.x+player.offset.x, player.iso_position.y+player.offset.y))
    #Returns worldScreen coordinates, whether the map should be updated
    #world.is_collided_with(player.rect)

    
    #worldScreen,updateMap = player.updateCamera(player.iso_position)

    #world.update((0,0))
    world.render(screen,False)
    player.render(player.image)
    #frame.integrate_state(main)

    
    # Update the display
    pygame.display.flip()
