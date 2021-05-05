import sys
import os
import numpy
import pygame
from pygame.locals import KEYDOWN, K_q
from common_utilities import *

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 600, 400

BLACK = (128, 128, 128)
GREY = (160, 160, 160)
YELLOW = (255, 255, 0)
TOMATO = (255, 0, 0)
DBLUE = (30, 144, 255)
LIME = (0, 255, 0)



 

class Map():
    def __init__(self):
        self.fileName = ''
        self.extension = '.txt'
    def loadFromFile(self,filename):
        with open(filename, 'r') as fileHandle:
            map_data = [[int(c) for c in row] for row in fileHandle.read().split('\n')]
        return map_data
        
    def writeToFile(self, filename,xres, yres):
        map_data = numpy.zeros((yres, xres), dtype=int)
        with open(filename, 'w') as f:
            for y, row in enumerate(map_data):
                if y != 0:
                    f.write('\n')
                for x, tile in enumerate(row):
                    f.write('%s' % tile)

    def checkFile(self):
        '''Checks file existence, if it exists appends a number to it '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fileName = dir_path + '/Map' + self.extension
        #Check for file existence, keep adding number to file until one does not exist
        #We don't want to overwrite existing map files
        i = 0
        while (os.path.isfile(fileName)):
            if (os.path.isfile(fileName)):
                fileName = fileName[:-len(self.extension)] + str(i) + self.extension
                i += 1

        return fileName

    def cartToIso(self,point):
        isoX = point[0] - point[1]
        isoY = (point[0] + point[1])/2
        return [isoX, isoY]   

    def placeCgridTile(self,screen,origin, color=BLACK, cellSize=18):
        # cellSize is smaller and offset by 2 to account for the grids border
        pygame.draw.rect(screen, color,(origin[0]+2, origin[1]+2, cellSize, cellSize) )

    def placeISOTile(self,screen,origin, color=BLACK, cellSize=18):
        tilePoints = [self.cartToIso(origin),
                    self.cartToIso([origin[0], cellSize + origin[1]]),
                    self.cartToIso([cellSize + origin[0], cellSize + origin[1]]),
                    self.cartToIso([cellSize + origin[0], origin[1]])]
        pygame.draw.polygon(screen, color, tilePoints, )

    def drawCartesian_Grid(self,screen,origin=[0, 0], size=8, cellSize=20):
        # borderCoordinates:
        hw = cellSize*size
        borderPoints = [origin, [origin[0], hw + origin[1]],
                        [hw + origin[0], hw + origin[1]],
                        [hw + origin[0], origin[1]]]
        pygame.draw.polygon(screen, BLACK, borderPoints, 2)
        # Draw inner grid :
        for colRow in range(1, size):
            dim = cellSize*colRow
            pygame.draw.line(screen, BLACK, (origin[0], origin[1] + dim),
                            (hw + origin[0], origin[1] + dim), 2)
            pygame.draw.line(screen, BLACK, (origin[0] + dim, origin[1]),
                            (origin[0] + dim, hw + origin[1]), 2)


    def draw(self,screen,origin=[0, 0], size=8, cellSize=20):
        hw = cellSize*size
        borderPoints = [self.cartToIso(origin),
                        self.cartToIso([origin[0], hw + origin[1]]),
                        self.cartToIso([hw + origin[0], hw + origin[1]]),
                        self.cartToIso([hw + origin[0], origin[1]])]

        # Draw border
        pygame.draw.polygon(screen, BLACK, borderPoints, 2)
        # Draw inner grid :
        for colRow in range(1, size):
            dim = cellSize*colRow
            pygame.draw.line(screen, BLACK,
                            self.cartToIso([origin[0], origin[1] + dim]),
                            self.cartToIso([hw + origin[0], origin[1] + dim]), 1)
            pygame.draw.line(screen, BLACK,
                            self.cartToIso([origin[0] + dim, origin[1]]),
                            self.cartToIso([origin[0] + dim, hw + origin[1]]), 1)


def main():
    pygame.init()  # Initial Setup
    screen = pygame.display.set_mode(SCREENSIZE)

    map = Map()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_q:
                pygame.quit()
                sys.exit()
        
        screen.fill(GREY)
        map.draw(screen,(260, -150))
        map.drawCartesian_Grid(screen,(60, 20))
        # Note: Adding points this way is tedious and used
        # here just to make things clearer...
        # ADD REGULAR POINTS :
        map.placeCgridTile(screen,(60, 20), DBLUE)
        map.placeCgridTile(screen,(80, 20), TOMATO)
        map.placeCgridTile(screen,(60, 40), LIME)
        # ADD ISOMETRIC TILES :
        map.placeISOTile(screen,(260, -150), DBLUE)
        map.placeISOTile(screen,(280, -150), TOMATO)
        map.placeISOTile(screen,(260, -130), LIME)
        pygame.display.update()


if __name__ == '__main__':
    main()