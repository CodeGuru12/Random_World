
import pygame
from pygame.constants import K_SPACE
from common_utilities import *
#import common_utilities 
import spriteManager
from spriteManager import options
import math
from time import time
#import sys

class Item():
    blitRect = None #Class member to return blit rects for render, workaround for time step integration function
    def __init__(self,image, isSheet, amount,size,rows=1,columns=1):
        self.index = 0
        width, height = size
        self.isSheet = isSheet
        self.rows = rows
        self.columns = columns
        self.elapsed_time = 0
        self.currentTime = 0
        self.previousTime = 0
        #Load single image, or sheet of images
        if (isSheet == False):
            self.image = pygame.image.load(get_file_path(image) ).convert_alpha()
        else:
            imageSheet = spriteManager.spritesheet(get_file_path(image),options.CONVERTALPHA)
            self.image = imageSheet.load_sheet(width,height,rows,columns)
        self.amount = amount #How many of the item we start with

    def rotateImage(self):
        pass

    def drop(self,event):
        give = False
        if (event.key == pygame.K_SPACE and self.amount > 0):
            self.amount -= 1
            give = True
        else:
            give = False

        return give
        

    def rect_distance(self,rect1, rect2):
        x1, y1 = rect1.topleft
        x1b, y1b = rect1.bottomright
        x2, y2 = rect2.topleft
        x2b, y2b = rect2.bottomright
        left = x2b < x1
        right = x1b < x2
        top = y2b < y1
        bottom = y1b < y2
        if bottom and left:
            print('bottom left')
            return math.hypot(x2b-x1, y2-y1b)
        elif left and top:
            print('top left')
            return math.hypot(x2b-x1, y2b-y1)
        elif top and right:
            print('top right')
            return math.hypot(x2-x1b, y2b-y1)
        elif right and bottom:
            print('bottom right')
            return math.hypot(x2-x1b, y2-y1b)
        elif left:
            print('left')
            return x1 - x2b
        elif right:
            print('right')
            return x2 - x1b
        elif top:
            print('top')
            return y1 - y2b
        elif bottom:
            print('bottom')
            return y2 - y1b
        else:  # rectangles intersect
            print('intersection')
            return 0

    def render(self,screen,position,row=1,column=1):
        x,y = position
        if (self.isSheet == False):
            self.blitRect = screen.blit(self.image, (x,y))
        else:
            #print('len(self.image): ',len(self.image))
            self.timingIndex(self.columns,self.columns)
            self.blitRect = screen.blit(self.image[row-1][self.index], (x,y))

    def timingIndex(self,freq,numImgs):
        '''Allows render to animate sheets by incrementing an index based on number of images in sheet'''
        self.currentTime = int(time()*1000)
        self.elapsed_time += (self.currentTime - self.previousTime)
        #print('self.elapsed_time:',self.elapsed_time)
        self.previousTime = self.currentTime
        if (self.elapsed_time >= (1 / int(freq)*1000)): 
            self.index += 1
            if (self.index >= numImgs):
                self.index = 0
            self.elapsed_time = 0