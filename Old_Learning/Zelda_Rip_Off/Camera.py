import pygame 
from Input import *
from INIT import *

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
        self.buffer = 50
        self.maxWorldMapX = WORLDMAPWIDTH - self.buffer
        self.maxWorldMapY = WORLDMAPHEIGHT - self.buffer
        self.screen = self.setDisplay(mapWidth, mapHeight)
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