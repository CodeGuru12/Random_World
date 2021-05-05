import sys
import pygame
from pygame.locals import KEYDOWN, K_q

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 600, 400

BLACK = (0, 0, 0)
GREY = (160, 160, 160)
YELLOW = (255, 255, 0)
TOMATO = (255, 0, 0)
DBLUE = (30, 144, 255)
LIME = (0, 255, 0)

_VARS = {'surf': False}


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

def main():
    pygame.init()  # Initial Setup
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawISO_Grid(origin=(260, -150))
        drawCartesian_Grid(origin=(60, 20))
        # Note: Adding points this way is tedious and used
        # here just to make things clearer...
        # ADD REGULAR POINTS :
        placeCgridTile(origin=(60, 20), color=DBLUE)
        placeCgridTile(origin=(80, 20), color=TOMATO)
        placeCgridTile(origin=(60, 40), color=LIME)
        # ADD ISOMETRIC TILES :
        placeISOTile(origin=(260, -150), color=DBLUE)
        placeISOTile(origin=(280, -150), color=TOMATO)
        placeISOTile(origin=(260, -130), color=LIME)
        pygame.display.update()


def cartToIso(point):
    isoX = point[0] - point[1]
    isoY = (point[0] + point[1])/2
    return [isoX, isoY]


def placeCgridTile(origin, color=BLACK, cellSize=18):
    # cellSize is smaller and offset by 2 to account for the grids border
    pygame.draw.rect(
        _VARS['surf'], color,
        (origin[0]+2, origin[1]+2, cellSize, cellSize)
    )


def placeISOTile(origin, color=BLACK, cellSize=18):
    tilePoints = [cartToIso(origin),
                  cartToIso([origin[0], cellSize + origin[1]]),
                  cartToIso([cellSize + origin[0], cellSize + origin[1]]),
                  cartToIso([cellSize + origin[0], origin[1]])]
    pygame.draw.polygon(_VARS['surf'], color, tilePoints, )


def drawISO_Grid(origin=[0, 0], size=8, cellSize=20):
    hw = cellSize*size
    borderPoints = [cartToIso(origin),
                    cartToIso([origin[0], hw + origin[1]]),
                    cartToIso([hw + origin[0], hw + origin[1]]),
                    cartToIso([hw + origin[0], origin[1]])]
    # Draw border
    pygame.draw.polygon(_VARS['surf'], BLACK, borderPoints, 2)
    # Draw inner grid :
    for colRow in range(1, size):
        dim = cellSize*colRow
        pygame.draw.line(_VARS['surf'], BLACK,
                         cartToIso([origin[0], origin[1] + dim]),
                         cartToIso([hw + origin[0], origin[1] + dim]), 1)
        pygame.draw.line(_VARS['surf'], BLACK,
                         cartToIso([origin[0] + dim, origin[1]]),
                         cartToIso([origin[0] + dim, hw + origin[1]]), 1)


def drawCartesian_Grid(origin=[0, 0], size=8, cellSize=20):
    # borderCoordinates:
    hw = cellSize*size
    borderPoints = [origin, [origin[0], hw + origin[1]],
                    [hw + origin[0], hw + origin[1]],
                    [hw + origin[0], origin[1]]]
    pygame.draw.polygon(_VARS['surf'], BLACK, borderPoints, 2)
    # Draw inner grid :
    for colRow in range(1, size):
        dim = cellSize*colRow
        pygame.draw.line(_VARS['surf'], BLACK, (origin[0], origin[1] + dim),
                         (hw + origin[0], origin[1] + dim), 2)
        pygame.draw.line(_VARS['surf'], BLACK, (origin[0] + dim, origin[1]),
                         (origin[0] + dim, hw + origin[1]), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()