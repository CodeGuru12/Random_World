# Import the pygame module

import pygame
from common_utilities import *
from time import time
import worldBuilder
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

MAP = [[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]]

DEBUG = False
        
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPEED = 15
# Setup the clock for a decent framerate
clock = pygame.time.Clock()


#Constants
SCREENS = 3

SPRITE_SIZE = (64,64)
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

worldMaxX = SCREEN_SIZE[0]*SCREENS
worldMaxY = SCREEN_SIZE[1]*SCREENS


class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit(message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if (colorkey is not None):
            if (colorkey == -1):
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

    def load_sheet(self,width,height,rows,image_count, colorkey = None):
        '''Loads an entire sprite sheet, assumes sprites are equally spaced, returns them as list of lists '''
        sprite_sheet = []
        for i in range(rows):
            sprite_sheet.append(self.load_strip((0, 0+i*height, width, height),image_count,colorkey))

        print('len(sprite_sheet)',len(sprite_sheet))
        return sprite_sheet



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

        if (DEBUG):
            print('self.screen:',self.screen)
            print('self.worldX:',self.worldX)
            print('self.worldY:',self.worldY)

            print('self.rect.x:',position.x)
            print('self.rect.y:',position.y)

        return (self.screen,self.updateScreen)



class Player(Camera):
    def __init__(self):
        super(Player,self).__init__()
        self.orientation = 'Right'
        ss = spritesheet(get_file_path('/Assets/Sprites/Walk_sprite_sheet.png'))
        # Sprite is 16x16 pixels at location 0,0 in the file...
        self.sheet = ss.load_sheet(64,64,4,9,(255,255,255))
        #self.images = ss.load_strip((0, 0, 64, 64),9,(255,255,255))
        self.index = 0
        #self.image = self.images[self.index]
        self.image = self.sheet[2][self.index]
        self.position = struct(x=0,y=0)
        self.my_rect = pygame.Rect(self.position.x,self.position.y, 64, 64)
        self.surf = pygame.Surface((64, 64), pygame.SRCALPHA)

        #print('self.rect:',self.rect)
    def update(self, pressed_keys,sprite):#,self.is_collision,sprite):
        global SPEED
        c = 0
        if (pressed_keys[K_UP]):
            c += 1
            SPEED += 1
            print('SPEED:',SPEED,flush=True)
        elif (pressed_keys[K_DOWN]):
            c -= 1
            SPEED -= 1
            print('SPEED:',SPEED,flush=True)
            if (SPEED <= 0):
                SPEED = 0
        print('self.position.x+c:',self.position.x+c,'self.position.y+c:',self.position.y+c)
        pygame.draw.rect(self.surf, (0, 100, 255), (0, 0, 48+c, 64+c), 1)
        screen.blit(self.surf, (self.position.x+c, self.position.y+c))
        print()

        moveBack = True


        if self.index > len(self.sheet[0])-1:
            self.index = 0
        # Move the SPRITE_SIZE based on user keypresses
        if pressed_keys[K_w]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
            
            #Allow movement only if collision not detected
                #print('self.is_collision(sprite):',self.is_collision(sprite))
            self.worldY -= SPEED
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.my_rect.x = self.position.x
            self.my_rect.y = self.position.y
            if(self.is_collision(sprite)):
               moveBack = False
               self.worldY += SPEED
            self.orientation = 'Right'
            self.image = self.sheet[0][self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
        
        if self.index > len(self.sheet[0])-1:
            self.index = 0

        if pressed_keys[K_s]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)
                #print('self.is_collision(sprite):',self.is_collision(sprite))
            self.worldY += SPEED
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.my_rect.x = self.position.x
            self.my_rect.y = self.position.y
            if(self.is_collision(sprite)):
               moveBack = False
               self.worldY -= SPEED
            self.orientation = 'Left'
            self.image = self.sheet[2][self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)

        if self.index > len(self.sheet[0])-1:
            self.index = 0

        if pressed_keys[K_a]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)

                #print('self.is_collision(sprite):',self.is_collision(sprite))
            self.worldX -= SPEED
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.my_rect.x = self.position.x
            self.my_rect.y = self.position.y
            if(self.is_collision(sprite)):
               moveBack = False
               self.worldX += SPEED
            self.orientation = 'Left'
            self.image = self.sheet[1][self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)

        if self.index > len(self.sheet[0])-1:
            self.index = 0

        if pressed_keys[K_d]:
            self.worldX,self.worldY = self.worldCoordinates(self.position.x,self.position.y)

                #print('self.is_collision(sprite):',self.is_collision(sprite))
            self.worldX += SPEED
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)
            self.my_rect.x = self.position.x
            self.my_rect.y = self.position.y
            if(self.is_collision(sprite)):
               moveBack = False
               self.worldX -= SPEED
            self.orientation = 'Left'
            self.image = self.sheet[3][self.index]
            self.index += 1
            self.position.x,self.position.y =  self.screenCoordinates(self.worldX,self.worldY)

        #Supposed to have a default rest image when not walking
        if ((not pressed_keys[K_a]) and (not pressed_keys[K_s]) 
             and (not pressed_keys[K_w]) and (not pressed_keys[K_d])):
            #self.image = self.images[0]
            pass

    def render(self,surface,position):
        if self.orientation == "Left":
            screen.blit(surface, (position.x,position.y))
        elif self.orientation == "Right":
            screen.blit(pygame.transform.flip(surface, True, False), (position.x,position.y))

    def get_rect(self):
        return pygame.Rect(self.position.x,self.position.y, 64, 64)
    
    def is_collision(self,object_rect):
        #https://gamedev.stackexchange.com/questions/116195/pygame-collide-rect
        collision = False
        #for r in object_rect:
        if (object_rect.rect[0].colliderect(self.my_rect)):
            collision = True
        print('collision:',collision)
        return collision

    # def is_collision(self,object_rect):
    #     #https://gamedev.stackexchange.com/questions/136195/pygame-collide-rect
    #     for rect in object_rect.rect:
    #         if (self.get_rect().colliderect(rect)):
    #             print('He\'s colliding',flush =True)
    #             return True #self.get_rect().colliderect(object_rect.rect)
    #     return False
# Initialize pygame
pygame.init()


# Create the screen object
# The size is determined by the constant SCREEN_SIZE[0] and SCREEN_SIZE[1]
screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]),pygame.DOUBLEBUF)


# Instantiate player. Right now, this is just a rectangle.
player = Player()
#Instantiate map, takes list of lists map to be rendered
world = worldBuilder.Map(worldBuilder.map_data,MAP)

# Variable to keep the main loop running
running = True

frame = FrameRate(113)
clock = pygame.time.Clock()
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

    screen.fill((0,0,0))

    frame.integrate_state(player.update,pressed_keys,world)#,world.is_collided_with,player)
    #Returns worldScreen coordinates, whether the map should be updated
    #world.is_collided_with(player.rect)

    worldScreen,updateMap = player.updateCamera(player.position)
    world.update(worldScreen)
    world.render(screen,updateMap)
    # Draw the player on the screen
    player.render(player.image,player.position)



    # Update the display
    pygame.display.flip()

    clock.tick(40)