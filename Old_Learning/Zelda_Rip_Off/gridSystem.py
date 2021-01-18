"""
Author - Thomas Just
Improvements - Seperate constants into a constants file, it's getting kind of large
             - Need a way to store the map in a different file, and pre-load it
             - Need to improve controls, there's a little bit of funny business sometimes
               depending on what order buttons are pushed, the character will stop for a second
             - Optimize so only the character is redrawn on the tiles he's currently on, not redraw
               the entire screen, too  consuming
             - start cleaning up code and seperating into classes, including camera, and input code
                    classes to create: player,time input, camera, and screen. Later on, can add collision
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

   
localMapWidth  = LOCALTILENUMBERX* TILESIZEX
localMapHeight = LOCALTILENUMBERY * TILESIZEY
SPRITEX = 40
SPRITEY = 40
WORLDMAPWIDTH  = MAPWIDTH*TILESIZEX 
WORLDMAPHEIGHT =  MAPHEIGHT*TILESIZEY
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
#__file__ = "C:\\Users\\ASUS1\\Documents\\MyRepo\\Sandbox\\Python\\Learning\\Zelda_Rip_Off\\Sprites"
playerPath = os.path.join(dirname(__file__),"Sprites", "Zelda_Front_Left.png")
player = Player(WHITE, playerPath)
count = 0
DEBUG = False
while running:
    globalX = cameraX + player.player_rect.x
    globalY = cameraY + player.player_rect.y
    #print("globalY = ", globalY, "cameraY = ", cameraY, "maxMapY = ", maxMapY, "player.player_rect.y = ", player.player_rect.y, "countY = ", countY, "\n")
    keystates = keyboardInput.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        down = event.type == pygame.KEYDOWN
        print(down) 
    player.update(keystates)   
        #print("cameraX = ", cameraX)
    #Solved map drawing issue
    #Use camera units to determine which local camera matrix
    #to use to draw the scene, alternatingly increasing map in x direction 
    #requires adding cameraYunits, and increases in y direction
    #requires adding cameraXunits
    print("This\n")
    if not down:
        if (count <=60 ):
            count = count + 1;
            for column in range(0,LOCALTILENUMBERX):
                for row in range(0,LOCALTILENUMBERY):
                    screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
            screen.blit(player.image, (player.player_rect.x, player.player_rect.y)) 
                #print("player.player_rect.x = ", player.player_rect.x, "player.player_rect.y = ", player.player_rect.y)
    elif (down):
        count = 0
        #print("Yes yes yes yes\n")
        doNotDrawMe = 0
        #Is the player trying to go left
        if keystates['left']:
            #Are they near the edge of camera?
            if (DEBUG):
                print("Entered Left\n")
            if(player.player_rect.x <= minlocalX and globalX > minMapX and countX > 0):
                #Go ahead and move the camera left
                if (DEBUG):
                    print("Entered edge of camera\n")
                cameraX -= TILESIZEX
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (maxlocalX, player.player_rect.y))
                player.player_rect.x = maxlocalX
                if(screensX > 0):
                    countX -= 1
            #if they are not near the edge of the camera
            elif(player.player_rect.x > minlocalX):
                if (DEBUG):
                    print("Entered go left, not near left edge\n")
                #player_rect.x -= 1
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            elif(globalX <= minMapX): 
                if (DEBUG):
                    print("Don't move player left, reached map edge\n")
                player.player_rect.x = minlocalX
            else:
                print("You have reached error state: LEFT")

        elif keystates['up']:
            #Are they near the edge of camera?
            if (DEBUG):
                print("Entered up key if\n")
            if(player.player_rect.y <= minlocalY and globalY > minMapY and countY > 0):
                #Go ahead and move the camera up
                if (DEBUG):
                    print("Entered up edge local screen, move screen up\n")
                cameraY -= 1*TILESIZEY
                #cameraY -= 1*TILESIZEY
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, maxlocalY))
                player.player_rect.y = maxlocalY
                if(countY > 0):
                    countY -= 1
            #if they are not near the edge of the camera
            elif(player.player_rect.y > minlocalY):
                if (DEBUG):
                    print("Entered key up, not near edge\n")
                #player_rect.x += 1
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            elif(globalY <= minMapY): 
                if (DEBUG):
                    print("Entered y edge of map, stay put\n")
                player.player_rect.y = minlocalY 
            else:
                print("You have reached error state: UP")
        elif keystates['down']:
            if (DEBUG):
                print("Entered down key state\n")
            #Are they near the edge of camera? 
            if(player.player_rect.y >= maxlocalY and globalY < maxMapY and countY < screensY):
                #Go ahead and move the camera down
                if (DEBUG):
                    print("Entered move camera down\n")
                cameraY += 1*TILESIZEY
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))

                player.player_rect.y = minlocalY
                if(countY < screensY):
                    countY +=1
            #if they are not near the edge of the camera
            elif(player.player_rect.y < maxlocalY):
                #player_rect.y -= 1
                if (DEBUG):
                    print("Entered down, not near camera edge, go ahead and move\n")
                for column in range(0,LOCALTILENUMBERX):
                    for row in range(0,LOCALTILENUMBERY):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                
                #print("motion", motion)
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            elif(globalY >= maxMapY): 
                if (DEBUG):
                    print("Entered down, edge of map, don't move")
                    print("player.player_rect.x = ", player.player_rect.x, "player.player_rect.y = ", player.player_rect.y)
                #print("Glonal max!")
                player.player_rect.y = maxlocalY
            else:
                print("globalY = ", globalY, "cameraY = ", cameraY, "maxMapY = ", maxMapY, "player.player_rect.y = ", player.player_rect.y, "countY = ", countY, "\n")
                print("You have reached error state: DOWN")
        elif keystates['right']:
                    #Are they near the edge of camera?
            if (DEBUG):
                print("Entered right key state\n")
            #print("globalX = ", globalX, "maxlocalX = ", maxlocalX, "player_rect.x = ", player_rect.x)
            if(player.player_rect.x >= maxlocalX and globalX < maxMapX and countX < screensX):
                if (DEBUG):
                    print("Entering, edge of camera right, move camera right\n")
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
                if (countX < screensX):
                    countX += 1
            #if they are not near the edge of the camera
            elif(player.player_rect.x < maxlocalX):
                #player_rect.x -= 1
                #print("Here")
                if (DEBUG):
                    print("Entering, not edge of right camera, do normal stuff\n")
                for column in range(0,LOCALTILENUMBERY):
                    for row in range(0,LOCALTILENUMBERX):
                        screen.blit(map.textures[tilemap[int(cameraY/TILESIZEY)+column][int(cameraX/TILESIZEX)+row]],(row*TILESIZEX, column*TILESIZEY))
                screen.blit(player.image, (player.player_rect.x, player.player_rect.y))
            elif(globalX >= maxMapX): 
                player.player_rect.x = maxlocalX    
            else:
                print("You have reached error state: RIGHT")
    #print("player_rect.x = ", player_rect.x, "player_rect.y = ", player_rect.y)
    pygame.display.flip()
    pygame.display.update()
    theClock.tick(5)        
            