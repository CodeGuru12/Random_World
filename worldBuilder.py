import pygame
from common_utilities import *
#import common_utilities 
import spriteManager
from spriteManager import options
from time import time
import time
import sys


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


#100 or greater is plants

map = [[0, 0, 0, 0, 2,3],
    [0, 1, 0, 3, 2, 2, 11, 14],
    [0, 0, 0, 2, 2],
    [0, 1, 0, 30, 2, 2, 13, 14],
       [0, 0, 0, 3, 2, 3, 0, 0],
       [0, 30, 0, 3, 5, 1, 12, 13],
       [0, 1, 0,  2, 2, 13, 14]
       ]
# map = [[0,1],
#         [2,30]]

class Map():
    def __init__(self,world):
        self.map = world
        self.map_view = 5
        self.wall = pygame.image.load(get_file_path('/Assets/Textures/wall.png') ).convert_alpha()  #load images
        self.tree = pygame.image.load(get_file_path('/Assets/Textures/_tree_01_192x220.png') ).convert_alpha() 
        #self.stylizedTree = pygame.image.load(get_file_path('/Assets/Textures/willowtree.png') ).convert_alpha()  #load images
        #self.stylizedTree.set_colorkey((255,255,255), pygame.RLEACCEL)
        #load_sheet(self,width,height,rows,image_count, colorkey = None)
        ss = spriteManager.spritesheet(get_file_path('/Assets/Textures/Grass-Spritesheet_Blocks.png'))
        tree_sheet = spriteManager.spritesheet(get_file_path('/Assets/Textures/tree_spritesheet_sparkle.png'),options.CONVERTALPHA)
        #plant_sheet = spriteManager.spritesheet(get_file_path('/Assets/Textures/plant_transparent.png'),options.CONVERTALPHA)
        self.enableCollideBoxes = True
        self.entityInfo = {'coordinates': [],'image': [],'subimage': [],'walkable': [], 'collisionCoord': [],'dispCollideBox': [],'hit': [],'shaded': [], 'sparkle': []}
        self.layers = 2
        self.centeredCoordinates = struct(x=0,y=0)
        self.objects = []
        for num in range(0,self.layers):
            self.objects.append({'coordinates': [],'image': [],'subimage': [],'walkable': [], 'collisionCoord': [],'dispCollideBox': [],'hit': [],'shaded': [], 'sparkle': []})
        #print('self.objects: ',self.objects)
        
        self.grass = ss.load_sheet(192,192,5,6,(0,0,0))
        self.trees = tree_sheet.load_sheet(192,194,1,4)
        #self.plants = plant_sheet.load_sheet(192,192,1,1)
        self.shadeSurface = pygame.Surface((100,121))
        self.shadeSurface.set_alpha(128)
        self.shadeSurface.fill((0,0,0))
        #self.tree = pygame.image.load(get_file_path('/Assets/Textures/stylized_tree_smaller.png') ).convert_alpha()
        self.init = True
        #self.mapping = mapping
        self.blitRect = [] #Rect surfaces to update on screen (returned by blit function)
        self.rect = []
        self.previous_update = False
        self.index = 0
        self.elapsed_time = 0
        self.currentTime = 0
        self.previousTime = 0
        self.w = 0
        self.h = 0
        self.treeOffset = struct(w=59,h=121)
        self.treeSize = struct(w=26,h=31)
        #print('tree.rect:',self.rect)
    # def update(self,coddordinates):
    #     self.map_view = self.mapping[coordinates[0]][coordinates[1]]
    #     if (DEBUG):
    #         #print('self.map_view:',self.map_view)
        
    def addCoordinates(x,y):
        return x+y

    def objectOrder(object1, object2):
        if (addCoordinates(object1.x,object1.y) > addCoordinates(object2.x,object2.y)):
            pass

    def createShadeSurface(self,width,height,opaqueness=128):
        #Create surface
        shadeSurface = pygame.Surface((width,height))
        #Set shade level
        shadeSurface.set_alpha(opaqueness)
        #Fill surface
        shadeSurface.fill((0,0,0))

        return shadeSurface

    def render(self,screen,updatemap):
        #Only update map when player screen changesdddd
        self.reset = False
        self.foreground = []
        self.count = 0
        if (True):#(self.init == True) or True):
            #    
                ##print('self.init:',self.init,flush=True)
                ##print('updatemap:',updatemap)
            tree_width = 25
            tree_height = 31
            actual_tree_width = 175
            actual_tree_height = 182
            if (self.init == True):
                for row in range(0,len(self.map)):
                    for col in range(0,len(self.map[row])):
                        cart_x = col * TILEWIDTH_HALF
                        cart_y = row * TILEHEIGHT_HALF
                        cart_x_hit = col * TILEWIDTH_HALF
                        cart_y_hit = row * TILEHEIGHT_HALF


                        iso_x, iso_y = cartesian2iso(cart_x,cart_y)
                        iso_x_hit, iso_y_hit = cartesian2iso(cart_x_hit,cart_y_hit)
                        self.centeredCoordinates.x = screen.get_rect().centerx + iso_x
                        self.centeredCoordinates.y = screen.get_rect().centery/2 + iso_y
                        
                        if (self.map[row][col] < 30):
                            self.objects[0]['coordinates'].append(struct(x=self.centeredCoordinates.x,y=self.centeredCoordinates.y))
                            self.objects[0]['image'].append(self.grass[ grass[self.map[row][col]][0] ][grass[self.map[row][col]][1]])
                            self.objects[0]['walkable'].append(True)
                            self.objects[0]['collisionCoord'].append(None)
                            self.objects[0]['hit'].append(False)
                            self.objects[0]['shaded'].append(False)
                            self.objects[0]['sparkle'].append(False)
                        elif (self.map[row][col] == 30 or self.map[row][col] == 100):
                            if (self.count == 0):
                                self.count += 1
                            self.objects[1]['coordinates'].append(struct(x=self.centeredCoordinates.x,y=self.centeredCoordinates.y) )
                            self.rect.append(pygame.Rect(self.centeredCoordinates.x+self.treeOffset.w, self.centeredCoordinates.y+self.treeOffset.h, self.treeSize.w,self.treeSize.h))
                            if (self.map[row][col] == 100):
                                pass
                                #self.objects[1]['image'].append(self.plants[0][0])
                            else:
                                self.objects[1]['image'].append(self.trees[0][0])#self.tree)
                            if (self.enableCollideBoxes == True):
                                self.objects[1]['dispCollideBox'].append(pygame.Surface((self.treeSize.w,self.treeSize.h),pygame.SRCALPHA))#(self.objects[1]['image'][-1].get_size()), pygame.SRCALPHA))

                                    
                        elif (self.map[row][col] == 31):
                            pass
                            #self.objects[1]['coordinates'].append(struct(x=self.centeredCoordinates.x,y=self.centeredCoordinates.y) )
                            #self.objects[1]['image'].append(self.stylizedTree)
                        
                            if (self.map[row][col] == 30 or self.map[row][col] == 100):
                                pass
                                #self.rect.append(pygame.Rect(self.centeredCoordinates.x+self.treeOffset.w, self.centeredCoordinates.y+self.treeOffset.h, tree_width, tree_height))
                                #tree_width, tree_height))
                                
            #sys.exit()
            self.init = False
                #sys.exit()
            #time.sleep(5)
            #for layer in range(0,self.layers):
            for index, img in enumerate(self.objects[0]['image']):
                screen.blit(img,(self.objects[0]['coordinates'][index].x, self.objects[0]['coordinates'][index].y))
            
  
        return self.objects
        #print('self.rect: ', len(self.rect),flush=True)


    def renderOver(self,screen):
        
        for index, img in enumerate(self.objects[1]['image']):

            surfToBlit = screen.blit(img,(self.objects[1]['coordinates'][index].x, self.objects[1]['coordinates'][index].y))
            #pygame.display.update(surfToBlit)  
            if (self.enableCollideBoxes == True):
                pygame.draw.rect(self.objects[1]['dispCollideBox'][index],(0, 100, 255),(0,0,self.treeSize.w,self.treeSize.h),2)
                blitRect = screen.blit(self.objects[1]['dispCollideBox'][index],self.rect[index])#(self.objects[layer]['coordinates'][index].x, self.objects[layer]['coordinates'][index].y))
                self.blitRect.append(blitRect)
            
                #pygame.display.update(blitRect)  
                #print('self.rect[index]: ',self.rect[index])
        return self.blitRect 
    def timingIndex(self,freq,numImgs):
        self.currentTime = int(time()*1000)
        self.elapsed_time += (self.currentTime - self.previousTime)
        #print('self.elapsed_time:',self.elapsed_time)
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
    