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
        self.tree = pygame.image.load(get_file_path('/Assets/Textures/stylized_tree_smaller.png') ).convert_alpha()
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
        if (True):#(self.init == True) or True):
            #    
                #print('self.init:',self.init,flush=True)
                #print('updatemap:',updatemap)
            tree_width = 100
            tree_height = 100
            actual_tree_width = 175
            actual_tree_height = 182
            for row_nb, row in enumerate(self.map[self.map_view]):    #for every row of the map...
                for col_nb, tile in enumerate(row):
                    if (tile == 1):
                        tileImage = self.wall
                        colorkey = None
                    elif (tile == 2):
                        tileImage = self.tree
                        #colorkey = (255,255,255)
                    else:
                        tileImage = self.grass
                        colorkey = None
                    cart_x = row_nb * TILEWIDTH_HALF
                    cart_y = col_nb * TILEHEIGHT_HALF  
                    iso_x = (cart_x - cart_y) 
                    iso_y = (cart_x + cart_y)/2
                    centered_x = screen.get_rect().centerx + iso_x
                    centered_y = screen.get_rect().centery/2 + iso_y
                    if (tile == 2):
                        screen.blit(tileImage, (centered_x, centered_y))
                        surf = pygame.Surface((tree_width, tree_height), pygame.SRCALPHA)
                        pygame.draw.rect(surf,(0, 100, 255),(0,0,tree_width,tree_height),2)
                        screen.blit(surf, (centered_x+30, centered_y+80))
                    else:
                        pass 
                        #screen.blit(tileImage, (centered_x, centered_y))

                    if (self.init == True):
                        print('Going in here?')
                        if (tile == 2):
                            self.rect.append(pygame.Rect(centered_x+30, centered_y+80, tree_width, tree_height))

            self.init = False

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
    