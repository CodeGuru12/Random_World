import pygame
from common_utilities import *
import spriteManager
from spriteManager import options
from time import time

class MapBuilder():
    """ToDo MapBuilder intended to construct and return designed map"""
    def __init__(self):
        dict_key = {'type': None ,'coordinates': (0,0), 'image': None,'size': (0,0), 'Top': False, 'Foreground': False}
        self.map = []


TILEWIDTH = 143  #holds the tile width and height
TILEHEIGHT = 137
TILEHEIGHT_HALF = TILEHEIGHT /2
TILEWIDTH_HALF = TILEWIDTH /2
DEBUG = False

grass = [(0,0), (0,1), (0,2),(0,3),(0,4), (0,5), 
         (1,0), (1,1), (1,2),(1,3),(1,4), (1,5), 
         (2,0), (2,1), (2,2),(2,3),(2,4), (2,5), 
         (3,0), (3,1), (3,2),(3,3),(3,4), (3,5), 
         (4,0), (4,1), (4,2),(4,3),(4,4), (4,5)]



map = [[0, 0, 0, 0, 2,3],
    [0, 1, 0, 3, 2, 2, 13, 14],
    [0, 0, 0, 30, 2],
    [0, 1, 0, 3, 2, 2, 13, 14],
       [0, 0, 0, 3, 2, 3, 31, 0],
       [0, 3, 30, 3, 5, 0, 12, 13],
       [0, 1, 0,  2, 2, 13, 14]
       ]


class Map():
    def __init__(self,world):
        self.map = world
        self.map_view = 5
        self.wall = pygame.image.load(get_file_path('/Assets/Textures/wall.png') ).convert_alpha()  #load images
        self.stylizedTree = pygame.image.load(get_file_path('/Assets/Textures/stylized_tree_smaller.png') ).convert_alpha()  #load images
        #load_sheet(self,width,height,rows,image_count, colorkey = None)
        ss = spriteManager.spritesheet(get_file_path('/Assets/Textures/Grass-Spritesheet_Blocks.png'))
        tree_sheet = spriteManager.spritesheet(get_file_path('/Assets/Textures/trees_twinkle.png'),options.CONVERTALPHA)#,options.TRANSPARENTCOLORKEY)
        self.grass = ss.load_sheet(192,192,5,6,(0,0,0))
        self.trees = tree_sheet.load_sheet(192,192,1,4)
        #self.tree = pygame.image.load(get_file_path('/Assets/Textures/stylized_tree_smaller.png') ).convert_alpha()
        self.init = True
        #self.mapping = mapping
        self.rect = []
        self.previous_update = False
        self.index = 0
        self.elapsed_time = 0
        self.currentTime = 0
        self.previousTime = 0
        print('tree.rect:',self.rect)
    # def update(self,coddordinates):
    #     self.map_view = self.mapping[coordinates[0]][coordinates[1]]
    #     if (DEBUG):
    #         print('self.map_view:',self.map_view)
        
    def render(self,screen,updatemap):
        #Only update map when player screen changesdddd
        self.reset = False
        self.foreground = []
        if (True):#(self.init == True) or True):
            #    
                #print('self.init:',self.init,flush=True)
                #print('updatemap:',updatemap)
            tree_width = 100
            tree_height = 100
            actual_tree_width = 175
            actual_tree_height = 182
            for row in range(0,len(self.map)):
                for col in range(0, len(self.map[row])):
            #for row_nb, row in enumerate(self.map):    #for every row of the map...
            #    for col_nb, tile in enumerate(row):
                    # if (tile == 1):
                    #     tileImage = self.wall
                    #     colorkey = None
                    # elif (tile == 2):
                    #     tileImage = self.tree
                    #     #colorkey = (255,255,255)
                    # else:
                    #     tileImage = self.grass
                    #     colorkey = None
                    cart_x = col * TILEWIDTH_HALF
                    cart_y = row * TILEHEIGHT_HALF  
                    iso_x = (cart_x - cart_y) 
                    iso_y = (cart_x + cart_y)/2
                    centered_x = screen.get_rect().centerx + iso_x
                    centered_y = screen.get_rect().centery/2 + iso_y
                    self.timingIndex(4,4)
                    if (self.map[row][col] < 30):
                        tileImage = self.grass[grass[self.map[row][col]][0]][grass[self.map[row][col]][1]]
                    else:
                        tileImage = self.grass[grass[0][0]][grass[0][1]]
                        if (self.map[row][col] == 30):
                            tileForeground = self.trees[0][self.index]
                        elif (self.map[row][col] == 31):
                            tileForeground = self.stylizedTree
                        print('(centered_x,centered_x): ',(centered_x,centered_x))
                        self.foreground.append({'image': self.trees[0][0], 'coordinates': (centered_x,centered_x)})
                        
                    
                    if (self.map[row][col] < 30):
                        screen.blit(tileImage, (centered_x, centered_y))
                    else:
                        #screen.blit(item['image'], (item['coordinates'][0], item['coordinates'][1]))
                        screen.blit(tileImage, (centered_x, centered_y))
                        if (self.map[row][col] == 31):
                            screen.blit(pygame.transform.flip(tileForeground, True, False), (centered_x,centered_y-96))
                        else:
                            screen.blit(tileForeground,(centered_x, centered_y-96))
                        #screen.blit(tileForeground,(centered_x, centered_y))
                        #surf = pygame.Surface((tree_width, tree_height), pygame.SRCALPHA)
                        #pygame.draw.rect(surf,(0, 100, 255),(0,0,tree_width,tree_height),2)
                    #screen.blit(surf, (centered_x+30, centered_y+80))
                    #else:
                    #    pass 
                      #screen.blit(tileImage, (centered_x, centered_y))
                    if (self.init == True):
                        if (self.map[row][col] > 29):
                            #pass
                            self.rect.append(pygame.Rect(centered_x, centered_y-96, tree_width, tree_height))
            #Render foreground images
            for i, item in enumerate(self.foreground):
                print('item: ',item)
                screen.blit(item['image'], (item['coordinates']))


            self.init = False
    def timingIndex(self,freq,numImgs):
        self.currentTime = int(time()*1000)
        self.elapsed_time += (self.currentTime - self.previousTime)
        print('self.elapsed_time:',self.elapsed_time)
        self.previousTime = self.currentTime
        if (self.elapsed_time >= (1 / int(freq)*1000)): 
            self.index += 1
            if (self.index >= numImgs):
                self.index = 0
            self.elapsed_time = 0
         
if __name__ == '__main__':
    import pygame
    from pygame.locals import ( K_w, K_s, K_a, K_d, K_UP, K_DOWN, K_ESCAPE, KEYDOWN, QUIT, )
    running = True
    pygame.init()
    screen = pygame.display.set_mode((800, 600),pygame.DOUBLEBUF)
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        worldMap = Map(map)
        worldMap.render(screen,False)
        pygame.display.update()
    