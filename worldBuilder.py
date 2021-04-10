import pygame
from common_utilities import *

map_data = [
[
    [1, 1, 1, 1, 1,1, 0, 1, 0, 1,2,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 0,0,0],
    [1, 0, 0, 0, 0,0, 0, 2, 0, 0,0,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1,0,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 0,0,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 0,0,0],
    [1, 0, 0, 0, 2,0, 0, 0, 0, 1,0,0],
    [1, 0, 2, 0, 0,0, 0, 0, 0, 1,0,0],
    [1, 0, 0, 0, 0,0, 0, 2, 0, 0,0,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 0,1,2],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1,2,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 2,0,0],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1,0,0]
],
[
    [1, 1, 1, 1, 1,1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1]
],
[
    [1, 1, 1, 1, 1,1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1,0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1,0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1,0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1]
],
[
    [1, 1, 0, 1, 1,0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1]
],
[
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
],
[
    [1, 1, 1, 1, 1,1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1],
    [1, 2, 0, 0, 0,1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1,1, 0, 2, 2, 1],
    [1, 0, 0, 0, 1,1, 0, 0, 2, 1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1]
],
[
    [1, 1, 1, 1, 1,1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 1,1, 0, 0, 2, 1,0,1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1,0,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,2,1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1,2,1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1,2,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,0,1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1,0,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,0,1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1,2,1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1,0,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,2,1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1,0,1]
],
[
    [1, 1, 1, 1, 1,1, 0, 1, 0, 1,1,0,0,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,1,0,0,1],
    [1, 0, 0, 0, 0,0, 0, 0, 0, 1,1,0,0,1],
    [1, 0, 0, 0, 1,1, 2, 0, 0, 1,1,0,0,1],
    [1, 0, 2, 0, 0,1, 0, 0, 0, 1,1,0,0,1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1,1,0,0,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,1,0,2,1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1,1,0,2,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,1,0,0,1],
    [1, 0, 0, 0, 0,1, 0, 0, 0, 1,1,0,1,1],
    [1, 0, 1, 0, 1,1, 0, 0, 0, 1,1,0,2,1],
    [1, 0, 0, 0, 1,1, 0, 0, 0, 1,1,0,1,1],
    [1, 1, 0, 0, 1,0, 0, 0, 0, 1,1,0,1,1]
],
[
    [2]
]
]               #the data for the map expressed as [row[tile]].

TILEWIDTH = 64  #holds the tile width and height
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT /2
TILEWIDTH_HALF = TILEWIDTH /2
DEBUG = False

class Map():
    def __init__(self,world,mapping):
        self.map = world
        self.map_view = 5
        self.wall = pygame.image.load(get_file_path('/Assets/Textures/wall.png') ).convert_alpha()  #load images
        self.grass = pygame.image.load(get_file_path('/Assets/Textures/grass.png') ).convert_alpha()
        self.tree = pygame.image.load(get_file_path('/Assets/Textures/tree.png') ).convert_alpha()
        self.init = True
        self.mapping = mapping
        self.rect = []
        self.previous_update = False
        print('tree.rect:',self.rect)
    def update(self,coordinates):
        self.map_view = self.mapping[coordinates[0]][coordinates[1]]
        if (DEBUG):
            print('self.map_view:',self.map_view)
        
    def render(self,screen,updatemap):
        #Only update map when player screen changes
        self.reset = False
        global temp_x
        global temp_y

        self.rect = pygame.Rect(250, 250, 64, 64)

        tileImage = self.tree
        #screen.blit(self.grass, (centered_x, centered_y))
        screen.blit(tileImage, (250, 250)) #display the actual tile

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(250, 250, 64, 64),  2) 
        pygame.display.flip() 
        #tree_rect = pygame.Surface((64, 64), pygame.SRCALPHA)
        #pygame.draw.rect(tree_rect,(0, 255, 0),(0,0,64,64),3)
        #print('centered_x: ',centered_x,'centered_y: ',centered_y)
        #screen.blit(tree_rect, (250, 250))


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

        worldMap = Map(map_data)
        worldMap.render(screen,False)
        pygame.display.update()
    