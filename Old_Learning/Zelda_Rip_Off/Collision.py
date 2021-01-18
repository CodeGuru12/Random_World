import pygame
from INIT import *
from Player import *
from Input import *
from Camera import *
import os
from os.path import dirname, realpath, abspath

class Collision():
    """ 
    class: Collision
        Inherits: None
        Purpose: Manages user input and decides whether the user
                 has collided with any in-game objects
    """ 

    def __init__(self):
        self.index = ['leftWall', 'rightWall',
                      'downWall', 'upWall']
                           #'upLeftWall', 'upRightWall',
                           #'downLeftWall','downRightWall']
        self.mapIndex = {'leftWall': 'leftEdge', 'rightWall': 'rightEdge',
                         'downWall': 'downEdge', 'upWall': 'upEdge'}
                         
        self.wallCollision = {'leftWall': self.hitLeftWall, 
                              'rightWall': self.hitRightWall,
                              'upWall': self.hitUpWall,
                              'downWall': self.hitDownWall}  
                              
        self.mapEdgeCollision = {'leftEdge': self.leftMapEdge,
                                 'rightEdge': self.rightMapEdge,
                                 'upEdge': self.upMapEdge,
                                 'downEdge': self.downMapEdge}   
        
        self.wallHit = {'leftWall': False, 
                        'rightWall': False,
                        'upWall':  False,
                        'downWall':  False}  
                        
        self.mapEdgeHit = {'leftEdge': False, 
                           'rightEdge': False,
                           'upEdge':  False,
                           'downEdge':  False}  
    #cObj in this case is player.player_rect.x, and player.player_rect.y                        
    def hitLeftWall(self,cObj, cCamera):
        if (cObj.player_rect.x <= cCamera.minlocalX ):
            #cObj.player_rect.x = cCamera.minlocalX
            return True
        else:
            return False
            
    def hitRightWall(self,cObj, cCamera):
        if (cObj.player_rect.x >= cCamera.maxlocalX ):
            #cObj.player_rect.x = cCamera.localMapWidth
            return True
        else:
            return False
            
    def hitUpWall(self,cObj, cCamera):
        if (cObj.player_rect.y <= cCamera.minlocalY ):
            #cObj.player_rect.x = cCamera.localMapWidth
            return True
        else:
            return False  
    
    def hitDownWall(self,cObj, cCamera):
        if (cObj.player_rect.y >= cCamera.maxlocalY ):
            #cObj.player_rect.x = cCamera.localMapWidth
            return True
        else:
            return False      
    
    ######################
    def leftMapEdge(self,cObj, cCamera):
        if (cObj.player_rect.x <= cCamera.globalX):
            #cObj.player_rect.x = cCamera.minlocalX
            return True
        else:
            return False
            
    def rightMapEdge(self,cObj, cCamera):
        if (cObj.player_rect.x >= cCamera.maxWorldMapX):
            #cObj.player_rect.x = cCamera.localMapWidth
            return True
        else:
            return False
            
    def upMapEdge(self,cObj, cCamera):
        if (cObj.player_rect.y <= cCamera.globalY ):
            #cObj.player_rect.x = cCamera.localMapWidth
            return True
        else:
            return False  
    
    def downMapEdge(self,cObj, cCamera):
        if (cObj.player_rect.y >= cCamera.maxWorldMapY ):
            #cObj.player_rect.x = cCamera.localMapWidth
            return True
        else:
            return False      
            
    def detectWallCollision(self, player, camera):
        """
        - detectWallCollision(player, camera)
                arguments: Player - player class
                            Camera - camera class
        - Description: This function cycles through 
                       the wallHit dictionary calling
                       each function that checks whether you
                       are near the local map boundary. If 
                       you are near the map boundary, you then
                       check whether you are at the map edge
                       
          returned arguments: None
        """
        for index in self.index:
            fun = self.wallCollision[index]
            self.wallHit[index] = fun(player, camera)
            print(index, "= ", self.wallHit[index], '\n')
            if(self.wallHit[index]):
                fun = self.mapEdgeCollision[self.mapIndex[index]]
                self.mapEdgeHit[index] = fun(player, camera)
    
        
    def handleInput(self,keyStates):
    
screen = pygame.display.set_mode((localMapWidth, localMapHeight))                   
playerPath = os.path.join(dirname(__file__),"Sprites", "Zelda_Front_Left.png")
player = Player(WHITE, playerPath)
camera = Camera(localMapWidth, localMapHeight)
a = Collision()
fun = a.wallCollision['leftWall']
keyboardInput = Input()
keystates =keyboardInput.update()
a.detectWallCollision(player, camera)
print("Success!\n")
"""
while True:
    pygame.display.flip()
    pygame.display.update() """