import pygame
import math
import os, sys
from os.path import dirname, realpath, abspath
from INIT import *
from Maps.TileMap import *
from Maps.Map import *
from Input import *
map = Map()
tilemap = map.loadMap(tiles)
WHITE = (255, 255, 255)

class Player(object):
    def __init__(self, color, path):
        pygame.init()
        self.SPRITEX = 40
        self.SPRITEY = 40
        self.cCamera = Camera(localMapWidth, localMapHeight)
        self.keyBoardInput = Input()
        self.keystates = self.keyBoardInput.update()
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey(color)
        self.player_rect = self.image.get_rect()
        self.screen = self.cCamera.setDisplay(localMapWidth, localMapHeight)
        self.player_rect.x = 0
        self.player_rect.y = 0
        self.speed = 3
        
    def updatePosition(self, positionX, positionY):
        self.player_rect.x = positionX
        self.player_rect.y = positionY

        
    def update(self, InputState):
        keystates = InputState.update()
        if keystates['right'] and keystates['up']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
            self.player_rect.y = self.player_rect.y+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
            #print(math.sqrt(self.player_rect.x*self.player_rect.x + self.player_rect.y*self.player_rect.y))
        elif keystates['right'] and keystates['down']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
            self.player_rect.y = self.player_rect.y+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
        elif keystates['left'] and keystates['down']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
            self.player_rect.y = self.player_rect.y+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
        elif keystates['left'] and keystates['up']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
            self.player_rect.y = self.player_rect.y+ 1/math.sqrt(self.player_rect.x*self.player_rect.x + self.speed*self.speed)
        if keystates['right']:
            self.player_rect.x += self.speed
        if keystates['left']:
            self.player_rect.x -= self.speed
        if keystates['up']:
            self.player_rect.y -= self.speed
        if keystates['down']:
            self.player_rect.y += self.speed
            
    
class Camera():
    """ 
    class: Camera
        Inherits: 
        Purpose: Manages the user displayed screen
                 Taking user inputs and maping them
                 to the screen, where the camera shows
    """
    def __init__(self, mapWidth, mapHeight): 
        self.localMapWidth  = mapWidth
        self.localMapHeight = mapHeight
        self.worldMapWidth = WORLDMAPWIDTH
        self.worldMapHeight = WORLDMAPHEIGHT
        self.maxWorldMapX = WORLDMAPWIDTH - self.buffer
        self.maxWorldMapY = WORLDMAPHEIGHT - self.buffer
        self.screen = self.setDisplay(mapWidth, mapHeight)
        self.buffer = 50
        self.cameraX = 0
        self.cameraY = 0
        self.countX = 0
        self.countY = 0
        
        self.minlocalX = 50
        self.minlocalY = 50  
        self.maxlocalX = mapWidth - self.buffer
        self.maxlocalY = mapHeight - self.buffer
        #Global Coordinates
        self.globalX = 50
        self.globalY = 50
        #self.globalX = self.cameraX + self.player_rect.x
        #self.globalY = self.cameraY + self.player_rect.y
        #Local coordinates
        self.localX = 50
        self.localY = 50
        self.moveCamera = {'up':False, 'down':False, 'left':False, 'right':False}
        self.maxCameraScreen = {'screensOver':screensY, 'screensDown':screensY}
        
        
    def setDisplay(self, mapWidth, mapHeight):
        return pygame.display.set_mode((mapWidth, mapHeight))
    
    def updateGlobalCoordinates(playerX, playerY):
        self.globalX = self.cameraX + playerX
        self.globalY = self.cameraY + playerY
    
    def NearCameraEdge(player, keyStates):
        #Are we near the top left side of screen
        if keyStates['up'] and keyStates['left']:
            if (player.player_rect.x <= minlocalX and player.player_rect.y <= minlocalY):
                if (self.nearMapEdge()):
                    player.updatePosition(minlocalX,minlocalY)
                else: 
                    #step is the number of steps the camera will move
                    cameraX -= step*TILESIZEX
                    cameraY += step*TILESIZEY
                   # self.moveCamera = {'leftUp':False,'leftDown':False,'rightUp':False,'rightDown':False, 
                   #                 'up':False, 'down':False, 'left':False, 'right':False}
        f
        #Are we near the left side of screen
        if keyStates['up'] and keyStates['left']:
            if (player.player_rect.x <= minlocalX and player.player_rect.y > minlocalY):
                if (self.nearMapEdge()):
                    player.player_rect.x = minlocalX
                    #player.player_rect.y = minlocalY   
                else:
                    cameraX -= step*TILESIZEX
        #Are we near the bottom left of screen
        elif (playerX <= minlocalX and playerY > maxlocalY):
            return True        
        #Are we near the top of the screen
        elif (playerX > minlocalX and playerY <= minlocalY):
            return True
        #Are we near the top right of the screen
        elif (playerX >= maxlocalX and playerY <= minlocalY):
            return True
        #Are we near the bottom right of the screen
        elif (playerX >= maxlocalX and playerY >= maxlocalY):
            return True
        #Are we near the bottom of the screen
        elif (playerX > minlocalX and playerY >= maxlocalY):
            return True   
        #Are we near the right of the screen
        elif (playerX >= maxlocalX and playerY > minlocalY):
            return True  
        else: 
            return False
            
    def nearMapEdge():
        #Are we near the top left side of screen
        if (self.globalX <= minMapX and self.globalY <= minMapY):
            return True 
        #Are we near the left side of screen
        elif (self.globalX <= minMapX and self.globalY > minMapY):
            return True
        #Are we near the bottom left of screen
        elif (self.globalX <= minMapX and self.globalY > maxMapY):
            return True        
        #Are we near the top of the screen
        elif (self.globalX > minMapX and self.globalY <= minMapY):
            return True
        #Are we near the top right of the screen
        elif (self.globalX >= maxMapX and self.globalY <= minMapY):
            return True
        #Are we near the bottom right of the screen
        elif (self.globalX >= maxMapX and self.globalY >= maxMapY):
            return True
        #Are we near the bottom of the screen
        elif (self.globalX > minMapX and self.globalY >= maxMapY):
            return True   
        #Are we near the right of the screen
        elif (self.globalX >= maxMapX and self.globalY > minMapY):
            return True  
        else:
            return False   
            
    def MoveCamera(move):
        #moveCamera[move]
        pass 
    def Update(self, screen, image, positionX, positionY):
        for column in range(0,LOCALTILENUMBERX):
            for row in range(0,LOCALTILENUMBERY):
                screen.blit(map.textures[tilemap[int(self.cameraY/TILESIZEY)+column][int(self.cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
        screen.blit(image, (positionX,positionY))
        
    def Display(self):
        pygame.display.flip()
        pygame.display.update()  
        
playerPath = os.path.join(dirname(__file__),"Sprites", "Zelda_Front_Left.png")
player = Player(WHITE, playerPath)

player.cCamera.Update(player.screen,player.image, player.player_rect.x, player.player_rect.y)
player.cCamera.Display()

print("Success\n")

