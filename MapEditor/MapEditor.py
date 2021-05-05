import common_utilities
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
#import faulthandler
#faulthandler.enable()
#Remove hello world print, all imports that have any pygame imports go here
import os, sys
with open(os.devnull, 'w') as f:
    # disable stdout
    oldstdout = sys.stdout
    sys.stdout = f

    import pygame
    import pygame.font
    import widgets

    import MapVisuals

    # enable stdout
    sys.stdout = oldstdout



BACKGROUND = (30,30,30)
GREY       = (128, 128, 128)
WHITE      = (255,255,255)


TOMATO = (255, 0, 0)
DBLUE = (30, 144, 255)
LIME = (0, 255, 0)

class Graphics():
    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = str(100)+ "," + str(100)
        pygame.init()
        self.Map = MapVisuals.Map()
        self.screen_resolution = common_utilities.getScreenResolution()
        self.nonFullScreenSize=(int(self.screen_resolution[0]/1.25),int(self.screen_resolution[1]/1.25))
        self.fullscreen = True
        self.setScreenResolution()


        self.icon_surface = pygame.image.load(common_utilities.get_file_path("MapEditor/Assets/Icon_rubikscub.png")).convert_alpha()

        self.mapXRes = 0
        self.mapYRes = 0
        pygame.display.set_caption("Level Editor")
        pygame.display.set_icon(self.icon_surface)
        self.textBox = widgets.InputBox(self.screen,100, 720, 140, 25)
        self.buttonLoad  = widgets.Button("Load Map",100, 750, 100, 20)
        self.buttonCreate  = widgets.Button("New Map",210, 750, 100, 20)
        self.backGround = pygame.Rect(10, 10, self.screen_resolution[0]-20,self.screen_resolution[1]-20)
        font = pygame.font.SysFont('cambriacambriamath',18)
        self.textBoxText = font.render("Map Size (X x Y)",True, WHITE)
        self.textBoxRect = self.textBoxText.get_rect()
        self.boxOutline  = pygame.Rect(90,695,230,85)
        self.root = Tk()
        self.root.withdraw() # we don't want a full GUI, so keep the root window from appearing
        self.root.iconbitmap(common_utilities.get_file_path("MapEditor/Assets/icon_rubikscub_1Lo_icon.ico")) #Replace tkinter icon

        self.keyStateCounter = 0
        self.mapResolution = None
        self.mapSize = common_utilities.struct(x=0,y=0)
        self.mapData = None


    def __click__(self):
        '''Handles mouse click actions, internal call, not intended to be called outside of a function '''
        if (self.buttonLoad.click()):
            self.Map.fileName = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            #Protect for askbox cancel
            if (self.Map.fileName != ''):
                self.mapData = self.Map.loadFromFile(self.Map.fileName)

        if (self.buttonCreate.click()):
            if (self.mapResolution != None):
                if (isinstance(self.mapResolution,str)):
                    self.mapResolution = self.mapResolution.split('x')
                    self.mapSize.x = int(self.mapResolution[0])
                    self.mapSize.y = int(self.mapResolution[1])

                    if (len(self.mapResolution) < 2):
                        print('Not enough arguments!',flush=True)
                    else:
                        fileName = self.Map.checkFile()
                        self.Map.writeToFile(fileName,self.mapSize.x,self.mapSize.y)


    def setScreenResolution(self):

        self.fullscreen = not self.fullscreen

        if (self.fullscreen):
            self.screen = pygame.display.set_mode(self.screen_resolution, pygame.FULLSCREEN,0)
        else:
            pygame.display.quit() 
            pygame.display.init()
            os.environ['SDL_VIDEO_WINDOW_POS'] = str(100)+ "," + str(100)

            self.screen = pygame.display.set_mode(self.nonFullScreenSize,pygame.RESIZABLE,0)

        pygame.display.update()
        
    def __hitkey__(self,events):
        '''Handle key events '''
        #key_states = pygame.key.get_pressed()
        for event in events:
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_F3):
                    self.setScreenResolution()



    def draw(self,events):
        self.__click__()
        self.__hitkey__(events)
        self.screen.blit(self.textBoxText,(100,695))
        pygame.draw.rect(self.screen, GREY, self.backGround, 1, 4)
        pygame.draw.rect(self.screen, GREY, self.boxOutline, 1, 4)

        origin = (700, -100)
        origin2 = (100,150)

        originC3 = (100, 150)
        originC4 = (120,150)
        originC5 = (100,170)

        originI3 = (700, -100)
        originI4 = (720, -100)
        originI5 = (700, -80)

        self.Map.draw(self.screen,origin)
        self.Map.drawCartesian_Grid(self.screen,origin2)
        # Note: Adding points this way is tedious and used
        # here just to make things clearer...
        # ADD REGULAR POINTS :
        self.Map.placeCgridTile(self.screen,originC3, DBLUE)
        self.Map.placeCgridTile(self.screen,originC4, TOMATO)
        self.Map.placeCgridTile(self.screen,originC5, LIME)
        # ADD ISOMETRIC TILES :
        self.Map.placeISOTile(self.screen,originI3, DBLUE)
        self.Map.placeISOTile(self.screen,originI4, TOMATO)
        self.Map.placeISOTile(self.screen,originI5, LIME)


running = True
graphics = Graphics()

while running:

    # for loop through the event queue
    events = pygame.event.get()
    for event in events:
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == pygame.QUIT:
            running = False
    graphics.screen.fill(BACKGROUND)
    graphics.draw(events)
    graphics.buttonLoad.draw(graphics.screen)
    graphics.buttonCreate.draw(graphics.screen)
    #Don't return anything from handle_event, ends function completely
    graphics.textBox.handle_event(graphics.screen,events)
    #Instead, we keep a copy of 
    if (graphics.textBox.textCopy != '' and graphics.mapResolution == None):
        graphics.mapResolution = graphics.textBox.textCopy

    #print('graphics.mapResolution: ',graphics.mapResolution)
    # Update the display
    pygame.display.flip()