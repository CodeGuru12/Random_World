import pygame
from pygame.locals import *
import sys
from math import *
#from numpy import linspace
pygame.init()
 
DISPLAYSURF = pygame.display.set_mode((1024, 600), DOUBLEBUF)    #set the display mode, window title and FPS clock
pygame.display.set_caption('Map Rendering Demo')
FPSCLOCK = pygame.time.Clock()
 
map_data = [
[1, 1, 1, 1, 1,1, 0, 1, 0, 1],
[1, 0, 0, 0, 1,1, 0, 0, 0, 1],
[1, 0, 0, 0, 0,0, 0, 0, 0, 1],
[1, 0, 0, 0, 1,1, 0, 0, 0, 1],
[1, 0, 0, 0, 0,1, 0, 0, 0, 1],
[1, 0, 1, 0, 1,1, 0, 0, 0, 1],
[1, 0, 0, 0, 1,1, 0, 0, 0, 1],
[1, 1, 0, 0, 1,0, 0, 0, 0, 1],
[1, 0, 0, 0, 1,1, 0, 0, 0, 1],
[1, 0, 0, 0, 0,1, 0, 0, 0, 1],
[1, 0, 1, 0, 1,1, 0, 0, 0, 1],
[1, 0, 0, 0, 1,1, 0, 0, 0, 1],
[1, 1, 0, 0, 1,0, 0, 0, 0, 1]
]               #the data for the map expressed as [row[tile]].
 
wall = pygame.image.load('C:\Games\PyGame\Isometric\Assetts\Level\wall.png').convert_alpha()  #load images
grass = pygame.image.load('C:\Games\PyGame\Isometric\Assetts\Level\grass.png').convert_alpha()
 
TILEWIDTH = 64  #holds the tile width and height
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT /2
TILEWIDTH_HALF = TILEWIDTH /2
theta = 0

 
while True:


    for row_nb, row in enumerate(map_data):    #for every row of the map...
        for col_nb, tile in enumerate(row):
            if tile == 1:
                tileImage = wall
            else:
                tileImage = grass
            cart_x = row_nb * TILEWIDTH_HALF
            cart_y = col_nb * TILEHEIGHT_HALF

            r =   sqrt(cart_x ** 2 + cart_y ** 2)
            if (cart_x != 0):
                theta = degrees(atan(cart_y/cart_x))

            print(r)
            print(theta)
            iso_x = (cart_x - cart_y) - 50
            iso_y = (cart_x + cart_y)/2 -50
            centered_x = DISPLAYSURF.get_rect().centerx + iso_x
            centered_y = DISPLAYSURF.get_rect().centery/2 + iso_y
            DISPLAYSURF.blit(tileImage, (centered_x, centered_y)) #display the actual tile
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
 
    pygame.display.flip()
    FPSCLOCK.tick(30)