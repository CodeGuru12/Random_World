"""
Author - Thomas Just
Improvements - Seperate constants into a constants file, it's getting kind of large
             - Need a way to store the map in a different file, and pre-load it
             - Need to improve controls, there's a little bit of funny business sometimes
               depending on what order buttons are pushed, the character will stop for a second
             - Optimize so only the character is redrawn on the tiles he's currently on, not redraw
               the entire screen, too time consuming
             - start cleaning up code and seperating into classes, including camera, and input code
                    classes to create: player, input, camera, and screen. Later on, can add collision
            Top priority
            - Fix code near left and up boundary, current != 0 isn't allowing sprite to move up or left
            - There is some odd behavior near the edges of the screen, including bouncing of sprite
              and when sprite is going in two directions at once, the screen occasionally shifts to another screen
"""
import pygame, sys
import os
from os.path import dirname, realpath, abspath
from pygame.locals import *
from Maps.TileMap import *
from Maps.Map import *
from INIT import *
from Input import *
from Player import *
theClock = pygame.time.Clock()

def fromLocalToGlobal(localCoordX, localCoordY):
    globalCoordX = cameraX + localCoordX
    globalCoordY = cameraY + localCoordY
    return globalCoordX,globalCoordY

def fromGlobalToLocal(globalCoordX, globalCoordY):
    localCoordX = globalCoordX - cameraX
    localCoordY = globalCoordY - cameraY
    return localCoordX,localCoordY
    


localMapWidth  = LOCALTILENUMBERX* TILESIZEX
localMapHeight = LOCALTILENUMBERY * TILESIZEY
maxlocalX = localMapWidth
maxlocalY = localMapHeight
SPRITEX = 40
SPRITEY = 40
WORLDMAPWIDTH  = MAPWIDTH*TILESIZEX 
WORLDMAPHEIGHT =  MAPHEIGHT*TILESIZEY
maxMapX = WORLDMAPWIDTH
maxMapY = WORLDMAPHEIGHT
running = True
keystates={'up':False, 'down':False, 'left':False, 'right':False}
#screen = pygame.display.set_mode((200,200))
screen = pygame.display.set_mode((localMapWidth, localMapHeight))

index = 0
map = Map()
tilemap = map.loadMap(tiles)
motion = 0
pygame.init()
down = False
doNotDrawMe = 0
KeyStatesFalse = 0
keyboardInput = Input()
keystates =keyboardInput.update()
__file__ = 'C:\Games\PyGame\Old_Learning\Zelda_Rip_Off\Sprites'
playerPath = os.path.join(dirname(__file__),"Sprites", "Zelda_Front_Left.png")
player = Player(WHITE, playerPath)
minMapX = 0
cameraX = 0
cameraY = 0
minMapY = 0
while running:
    globalX = cameraX + player.player_rect.x
    globalY = cameraY + player.player_rect.y
    localX, localY = fromGlobalToLocal(globalX, globalY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        down = event.type == pygame.KEYDOWN
        keystates = keyboardInput.update()
    player.update(keyboardInput)
        #print("cameraX = ", cameraX)
    #Solved map drawing issue
    #Use camera units to determine which local camera matrix
    #to use to draw the scene, alternatingly increasing map in x direction 
    #requires adding cameraYunits, and increases in y directionf
    #requires adding cameraXunits
    if not down:
        for column in range(0,LOCALTILENUMBERX):
            for row in range(0,LOCALTILENUMBERY):
                screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
        screen.blit(player.image, (player.player_rect.x, player.player_rect.y)) 
    elif (down):
        #print("Yes yes yes yes\n")
        doNotDrawMe = 0
        #Is the player trying to go left
        if keystates['left']:
            #Are they near the edge of camera?
            if(player.player_rect.x <= localX and globalX > minMapX):
                #Go ahead and move the camera left
                cameraX -= TILESIZEX
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                player.player_rect.x = maxlocalX
                screen.blit(player.image, (maxlocalX, player.player_rect.y))
                if(screensX != 0):
                    countX -= 1
            #if they are not near the edge of the camera
            elif(player.player_rect.x > minlocalX):
                #player_rect.x -= 1
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            #At left edge of screen map
            else:
                player.player_rect.x = minlocalX
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))

        if keystates['up']:
            #Are they near the edge of camera?
            if(player.player_rect.y <= minlocalY and globalY > minMapY):
                #Go ahead and move the camera up
                cameraY -= 1*TILESIZEY
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                player.player_rect.y = maxlocalY
                screen.blit(player.image, (player.player_rect.x, maxlocalY))
                if(screensY != 0):
                    countY -= 1
            #if they are not near the edge of the camera
            elif(player.player_rect.y > minlocalX):
                #player_rect.x += 1
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            else:
                player.player_rect.y = minlocalY 
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
        if keystates['down']:
            #Are they near the edge of camera? 
            if(player.player_rect.y >= maxlocalY and globalY < maxMapY):
                #Go ahead and move the camera up
                cameraY += 1*TILESIZEY
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))

                player.player_rect.y = minlocalY
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
                if(countY != screensY):
                    countY +=1
            #if they are not near the edge of the camera
            elif(player.player_rect.y < maxlocalY):
                #player_rect.y -= 1
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            else:
                player.player_rect.y = maxlocalY
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
                print("You have reached error state: DOWN")
        if keystates['right']:
                    #Are they near the edge of camera?
            #print("globalX = ", globalX, "maxlocalX = ", maxlocalX, "player_rect.x = ", player_rect.x)
            if(player.player_rect.x >= maxlocalX and globalX < maxMapX):
                #print(screensX)
                #print("-----------------Entered-----------")
                #print("globalX = ", globalX, "maxlocalX = ", maxlocalX, "player_rect.x = ", player_rect.x)
                #Go ahead and move the camera right
                cameraX += 1*TILESIZEX
                for column in range(0,LOCALTILENUMBERY):
                    for row in range(0,LOCALTILENUMBERX):
                       # print(int(cameraY/TILESIZEY)+column)
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (minlocalX, player.player_rect.y))
                player.player_rect.x = minlocalX
                if (countX != screensX):
                    countX += 1
            #if they are not near the edge of the camera
            elif(player.player_rect.x < maxlocalX):
                #player_rect.x -= 1
                #print("Here")
                for column in range(0,LOCALTILENUMBERY):
                    for row in range(0,LOCALTILENUMBERX):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            else:
                player.player_rect.x = maxlocalX   
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y)) 
    #print("player_rect.x = ", player_rect.x, "player_rect.y = ", player_rect.y)
    pygame.display.flip()
    pygame.display.update()
    theClock.tick(60)        
            