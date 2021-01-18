#INITIALIZATION

BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
cameraX = 0 #moved to camera class
cameraY = 0
TILESIZEX = 100
TILESIZEY = 100
MAPWIDTH = 10#6
MAPHEIGHT = 6#7

countX = 0 #moved to camera class
countY = 0
#Sprite buffer for camera
LOCALTILENUMBERX = 3
LOCALTILENUMBERY = 3
localMapWidth  = LOCALTILENUMBERX* TILESIZEX
localMapHeight = LOCALTILENUMBERY * TILESIZEY
WORLDMAPWIDTH  = MAPWIDTH*TILESIZEX 
WORLDMAPHEIGHT =  MAPHEIGHT*TILESIZEY
minlocalX = 0 #moved to camera class
minlocalY = 0

minMapX = 50 #Minimum map distance with sprite buffer
minMapY = 50
maxlocalX = LOCALTILENUMBERX*TILESIZEX - minMapX
maxlocalY = LOCALTILENUMBERY*TILESIZEY - minMapY
maxMapX = MAPWIDTH*TILESIZEX - minMapX
maxMapY = MAPHEIGHT*TILESIZEY - minMapY
step = 1 #number of steps the camera will move when player reaches screen edge
screensX = int((maxMapX - maxlocalX)/(TILESIZEX*step)) #The number of x direction screens the player can transverse before being at the edge of the map
screensY = int((maxMapY - maxlocalY)/(TILESIZEY*step)) #The number of screens the player can transverse before being at the edge of the map

# #Global Coordinates
globalX = 0
globalY = 0
# #Local coordinates
# localX = 0
# localY = 0

maxLocalX = LOCALTILENUMBERX*TILESIZEX
maxLocalY = LOCALTILENUMBERY*TILESIZEY