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
        print('self.init:',self.init,'updatemap:',updatemap,flush=True)
        if ((self.init == True) or True):
            #    
                #print('self.init:',self.init,flush=True)
                #print('updatemap:',updatemap)

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
                    centered_x = screen.get_rect().centerx + iso_x-50
                    centered_y = screen.get_rect().centery/2 + iso_y-50
                    if (tile == 2):
                        screen.blit(self.grass, (centered_x, centered_y))
                        screen.blit(tileImage, (centered_x, centered_y)) #display the actual tile
                    else:
                        screen.blit(tileImage, (centered_x, centered_y))
                    


                    if (tile == 2 and (self.init)):
                        #Draw rectangle

                        self.rect.append(pygame.Rect(centered_x, centered_y, 64, 64))
                    elif (updatemap and (self.reset)):
                        self.rect = []
                        surf = pygame.Surface((64, 64), pygame.SRCALPHA)
                        pygame.draw.rect(surf,(0, 100, 255),(centered_x,centered_y,64,64),21)
                        screen.blit(surf, (centered_x, centered_x))
                        self.rect.append(pygame.Rect(centered_x, centered_y, 64, 64))

                    if (tile == 2):
                        print('we are coming in here?',flush=True)
                        surf = pygame.Surface((64, 64), pygame.SRCALPHA)
                        pygame.draw.rect(surf,(0, 100, 255),(centered_x,centered_y,64,64),3)
                        screen.blit(surf, (centered_x, centered_x))
                        #print('self.rect:',self.rect)
                        #screen.set_colorkey(colorkey, pygame.RLEACCEL)
            self.init = False
            self.previous_update = updatemap
    #def is_collided_with(self, sprite):
    #    return self.rect.colliderect(sprite.rect)

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
    