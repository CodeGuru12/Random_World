import pygame
import os
from os.path import dirname, realpath, abspath

class Map():
    """ 
    class: TileMap()
        Inherits: None
        Purpose: Allow user to load any sized map
    """
    def __init__(self):
        self.tilemap = []
        self.DIRT = 0
        self.GRASS = 1
        self.WATER = 2
        self.COAL = 3
        #__file__ = "C:\\Users\\ASUS1\\Documents\\MyRepo\\Sandbox\\Python\\Learning\\Zelda_Rip_Off\\Textures"
        __file__ = 'C:\Games\PyGame\Old_Learning\Zelda_Rip_Off\Textures'
        filepath1 = os.path.join(dirname(__file__),"Textures", "dirt.png")
        filepath2 = os.path.join(dirname(__file__),"Textures", "grass.png")
        filepath3 = os.path.join(dirname(__file__),"Textures", "water.png")
        filepath4 = os.path.join(dirname(__file__),"Textures", "coal.png")

        
        self.textures = {self.DIRT: pygame.image.load(filepath1),
                    self.GRASS: pygame.image.load(filepath2), 
                    self.WATER: pygame.image.load(filepath3),
                    self.COAL: pygame.image.load(filepath4)}     
                    
    def loadMap(self,obj):
        """
        Function - loadMap(obj)
                 Purpose: Loads user defined map
                 Input: obj - should be a list inside a list (matrix)
                              which will be converted to the association
                              in using definitions in the init function
                    obj is a square n x n matrix
        """
        list = []
        count = 0
        k = 0
        for i in range(0,len(obj)):
            count = count + 1
            for j in range(0,len(obj[0]) ): 
                if (obj[i][j] == 0):
                    list.append(self.DIRT)
                elif (obj[i][j] == 1):
                    list.append(self.GRASS)
                elif (obj[i][j] == 2):
                    list.append(self.WATER)
                elif (obj[i][j] == 3):
                    list.append(self.COAL)
                k = k + 1
            self.tilemap.append(list)
            list = []    
        print("count = ",count, "k = ", len(self.tilemap))
        return self.tilemap
    def MapLength(obj):
        """
        Gives you the size of the map in a tuple, n x n, in the number of tiles
        The map assumes it is square
        """
        if (not tilemap):
            return (0,0)
        else:   
            return (len(obj),len(obj[0]))
  