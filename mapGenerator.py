import pygame
from common_utilities import  *
import spriteManager

RED = (255,0, 0)
BLUE = (0,0,255)
GREEN = (0,128,0)
YELLOW = (255,255,0)

class Isometric():
    def __init__(self):
        vMouse = struct(x=0,y=0)
        # Number of tiles in world
        self.vWorldSize = (14, 10)

        # Size of single tile graphic
        self.vTileSize = struct(x=192, y=192)

        # Where to place tile (0,0) on screen (in tile size steps)
        self.vOrigin = (5, 1)

        # Sprite that holds all imagery
        self.sprIsom = None
		# Load sprites used in demonstration
		self.sprIsom = spriteManager.spritesheet(get_file_path('/Assets/Textures/isometric_demo.png'))
        #Create surface and display
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA)
        self.screen = pygame.display.set_mode((1000, 700,pygame.DOUBLEBUF)
		# Create empty world
		self.pWorld = []

	def ToScreen(int x, int y):
        '''convert "world" coordinate into screen space '''
        return ((vOrigin.x * vTileSize.x) + (x - y) * (vTileSize.x / 2),(vOrigin.y * vTileSize.y) + (x + y) * (vTileSize.y / 2))

	def OnUserUpdate(mouseClick) 
	{
		#Clear(olc::WHITE);

		# Get Mouse in world
        vMouse.x, vMouse.y = pygame.mouse.get_pos()
		
		# Work out active cell
		vCell = (vMouse.x / vTileSize.x, vMouse.y / vTileSize.y)

		# Work out mouse offset into cell
		vOffset = (vMouse.x % vTileSize.x, vMouse.y % vTileSize.y)

		# Sample into cell offset colour
		col = self.sprIsom.sheet.get_at(3 * vTileSize.x + vOffset.x, vOffset.y);

		# Work out selected cell by transforming screen cell
		vSelected = [(vCell.y - self.vOrigin.y) + (vCell.x - self.vOrigin.x),(vCell.y - self.vOrigin.y) - (vCell.x - self.vOrigin.x)]

		# "Bodge" selected cell by sampling corners
		if (col == RED)    vSelected[0] += -1
		if (col == BLUE)   vSelected[1] += -1
		if (col == GREEN)  vSelected[1] += 1
		if (col == YELLOW) vSelected[0] += 1

		# Handle mouse click to toggle if a tile is visible or not
		if (mouseClicked == True):
			# Guard array boundary
			if (vSelected.x >= 0 and vSelected.x < vWorldSize.x and vSelected.y >= 0 and vSelected.y < vWorldSize.y):
                pWorld[vSelected.y * vWorldSize.x + vSelected.x] = (pWorld[vSelected.y * vWorldSize.x + vSelected.x] + 1) % 6
				#++pWorld[vSelected.y * vWorldSize.x + vSelected.x] %= 6;
						

		
		# Draw World - has binary transparancy so enable masking
		#SetPixelMode(olc::Pixel::MASK);

		# (0,0) is at top, defined by vOrigin, so draw from top to bottom
		# to ensure tiles closest to camera are drawn last
        for y in range(0,len(vWorldSize.y):
			for x in range(0,len(vWorldSize.x):
				# Convert cell coordinate to world space
				vWorld = self.ToScreen(x, y);
				
				if (pWorld[y*vWorldSize.x + x] == 0):
					# Invisble Tile
					screen.blit(self.sprIsom, (vWorld.x, vWorld.y, self.sprIsom, 1 * vTileSize.x, 0, vTileSize.x, vTileSize.y);
					break
				elif((pWorld[y*vWorldSize.x + x] == 1):
					# Visible Tile
					DrawPartialSprite(vWorld.x, vWorld.y, self.sprIsom, 2 * vTileSize.x, 0, vTileSize.x, vTileSize.y);
					break
				elif((pWorld[y*vWorldSize.x + x] ==  2):
					# Tree
					DrawPartialSprite(vWorld.x, vWorld.y - vTileSize.y, self.sprIsom, 0 * vTileSize.x, 1 * vTileSize.y, vTileSize.x, vTileSize.y * 2);
					break
				elif((pWorld[y*vWorldSize.x + x] ==  3):
					# Spooky Tree
					DrawPartialSprite(vWorld.x, vWorld.y - vTileSize.y, self.sprIsom, 1 * vTileSize.x, 1 * vTileSize.y, vTileSize.x, vTileSize.y * 2);
					break
				elif((pWorld[y*vWorldSize.x + x] == 4):
					# Beach
					DrawPartialSprite(vWorld.x, vWorld.y - vTileSize.y, self.sprIsom, 2 * vTileSize.x, 1 * vTileSize.y, vTileSize.x, vTileSize.y * 2);
				elif((pWorld[y*vWorldSize.x + x] == 5):
					# Water
					DrawPartialSprite(vWorld.x, vWorld.y - vTileSize.y, self.sprIsom, 3 * vTileSize.x, 1 * vTileSize.y, vTileSize.x, vTileSize.y * 2);
					break


		# Draw Selected Cell - Has varying alpha components
		SetPixelMode(olc::Pixel::ALPHA);

		# Convert selected cell coordinate to world space
		vSelectedWorld = self.ToScreen(vSelected.x, vSelected.y);

		# Draw "highlight" tile
		DrawPartialSprite(vSelectedWorld.x, vSelectedWorld.y, sprIsom, 0 * vTileSize.x, 0, vTileSize.x, vTileSize.y);

		# Go back to normal drawing with no expected transparency
		SetPixelMode(olc::Pixel::NORMAL);

		# Draw Hovered Cell Boundary
		#DrawRect(vCell.x * vTileSize.x, vCell.y * vTileSize.y, vTileSize.x, vTileSize.y, olc::RED);
				
		# Draw Debug Info
		DrawString(4, 4, "Mouse   : " + std::to_string(vMouse.x) + ", " + std::to_string(vMouse.y), olc::BLACK);
		DrawString(4, 14, "Cell    : " + std::to_string(vCell.x) + ", " + std::to_string(vCell.y), olc::BLACK);
		DrawString(4, 24, "Selected: " + std::to_string(vSelected.x) + ", " + std::to_string(vSelected.y), olc::BLACK);
		return true;
	}
};


def main()
    running = True

    while running: # your main loop
        # get all events
        ev = pygame.event.get()

        # proceed events
        for event in ev:
            # handle MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClick = True
            else:
                mouseClick = False

	IsometricDemo demo;
	if (demo.Construct(512, 480, 2, 2))
		demo.Start();
	return 0;

if __init__ == '__main__':
    main()