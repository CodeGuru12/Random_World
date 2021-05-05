import pygame


COLOR_INACTIVE = pygame.Color((128,128,128))
COLOR_ACTIVE = pygame.Color((0,0,0))
BACKGROUND_ACTIVE = (255,255,255)
BACKGROUND_INACTIVE = ((230,230,230))


class Button:
    """usage:
    b = Button(params)  # create the button at start of program with chosen parameters

    game loop:
        b.draw(surface_to_draw_to)  # pygame.surface.Surface()
        if b.click():  # check if the button was clicked
            do stuff for when button is clicked
    """
    def __init__(self, text="", left=10, top=30, width=None, height=20):
        self.text = text
        self.left = left
        self.top = top
        self.height = height
        self.colour1 = (220, 220, 220)  # main
        self.colour2 = (100, 100, 100)  # border
        self.colour3 = (172, 220, 247)  # hover
        self.colour4 = (225, 243, 252)
        self.fontname = "cambriacambriamath"
        self.fontsize = self.height-4
        self.mouse_over = False
        self.mouse_down = False
        self.mouse = "off"
        self.clicked = False
        self.font = pygame.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pygame.font.Font.size(self.font, self.text)
        if width == None:
            self.width = self.text_width + 20
            self.width_type = "text"
        else:
            self.width = width
            self.width_type = "user"
        self.buttonUP = pygame.Surface((self.width, self.height))
        self.buttonDOWN = pygame.Surface((self.width, self.height))
        self.buttonHOVER = pygame.Surface((self.width, self.height))
        self.__update__()

    def __update__(self):
        # up
        r, g, b = self.colour1
        self.buttonUP.fill(self.colour1)
        pygame.draw.rect(self.buttonUP, (r+20, g+20, b+20), (0, 0, self.width, self.height/2), 0)
        pygame.draw.line(self.buttonUP, self.colour2, (2, 0), (self.width-3, 0), 1)
        pygame.draw.line(self.buttonUP, self.colour2, (2, self.height-1), (self.width-3, self.height-1), 1)
        pygame.draw.line(self.buttonUP, self.colour2, (0, 2), (0, self.height-3), 1)
        pygame.draw.line(self.buttonUP, self.colour2, (self.width-1, 2), (self.width-1, self.height-3), 1)
        self.buttonUP.set_at((1, 1), self.colour2)
        self.buttonUP.set_at((self.width-2, 1), self.colour2)
        self.buttonUP.set_at((1, self.height-2), self.colour2)
        self.buttonUP.set_at((self.width-2, self.height-2), self.colour2)
        self.buttonUP.blit(self.font.render(self.text, False, (0, 0, 0)), ((self.width/2)-(self.text_width/2), (self.height/2)-(self.text_height/2)))
        # hover
        self.buttonHOVER.fill(self.colour3)
        pygame.draw.rect(self.buttonHOVER, self.colour4, (0, 0, self.width, self.height/2), 0)
        pygame.draw.line(self.buttonHOVER, self.colour2, (2, 0), (self.width-3, 0), 1)
        pygame.draw.line(self.buttonHOVER, self.colour2, (2, self.height-1), (self.width-3, self.height-1), 1)
        pygame.draw.line(self.buttonHOVER, self.colour4, (2, self.height-2), (self.width-3, self.height-2), 1)
        pygame.draw.line(self.buttonHOVER, self.colour2, (0, 2), (0, self.height-3), 1)
        pygame.draw.line(self.buttonHOVER, self.colour4, (1, 2), (1, self.height-3), 2)
        pygame.draw.line(self.buttonHOVER, self.colour2, (self.width-1, 2), (self.width-1, self.height-3), 1)
        self.buttonHOVER.set_at((1, 1), self.colour2)
        self.buttonHOVER.set_at((self.width-2, 1), self.colour2)
        self.buttonHOVER.set_at((1, self.height-2), self.colour2)
        self.buttonHOVER.set_at((self.width-2, self.height-2), self.colour2)
        self.buttonHOVER.blit(self.font.render(self.text, False, (0, 0, 0)), ((self.width/2)-(self.text_width/2), (self.height/2)-(self.text_height/2)))
        # down
        r, g, b = self.colour3
        r2, g2, b2 = self.colour4
        self.buttonDOWN.fill((r-20, g-20, b-10))
        pygame.draw.rect(self.buttonDOWN, (r2-20, g2-20, b2-10), (0, 0, self.width, self.height/2), 0)
        pygame.draw.line(self.buttonDOWN, self.colour2, (2, 0), (self.width-3, 0), 1)
        pygame.draw.line(self.buttonDOWN, (r-20, g-20, b-10), (2, 1), (self.width-3, 1), 2)
        pygame.draw.line(self.buttonDOWN, self.colour2, (2, self.height-1), (self.width-3, self.height-1), 1)
        pygame.draw.line(self.buttonDOWN, self.colour2, (0, 2), (0, self.height-3), 1)
        pygame.draw.line(self.buttonDOWN, (r-20, g-20, b-10), (1, 2), (1, self.height-3), 2)
        pygame.draw.line(self.buttonDOWN, self.colour2, (self.width-1, 2), (self.width-1, self.height-3), 1)
        self.buttonDOWN.set_at((1, 1), self.colour2)
        self.buttonDOWN.set_at((self.width-2, 1), self.colour2)
        self.buttonDOWN.set_at((1, self.height-2), self.colour2)
        self.buttonDOWN.set_at((self.width-2, self.height-2), self.colour2)
        self.buttonDOWN.blit(self.font.render(self.text, False, (0, 0, 0)), ((self.width/2)-(self.text_width/2)+1, (self.height/2)-(self.text_height/2)))

    def draw(self, surface):
        self.__mouse_check__()
        if self.mouse == "hover":
            surface.blit(self.buttonHOVER, (self.left, self.top))
        elif self.mouse == "off":
            surface.blit(self.buttonUP, (self.left, self.top))
        elif self.mouse == "down":
            surface.blit(self.buttonDOWN, (self.left, self.top))

    def __mouse_check__(self):
        _1, _2, _3 = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if not _1:
            self.mouse = "off"
        if mouse_x > self.left and mouse_x < self.left + self.width and mouse_y > self.top and mouse_y < self.top + self.height and not self.mouse == "down":
            self.mouse = "hover"
        if not self.mouse_down and _1 and self.mouse == "hover":
            self.mouse = "down"
            self.clicked = True
        if self.mouse == "off":
            self.clicked = False

    def click(self):
        _1, _2, _3 = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.left and mouse_x < self.left + self.width and mouse_y > self.top and mouse_y < self.top + self.height and self.clicked and not _1:
            self.clicked = False
            return True
        else:
            return False

    def set_text(self, text, fontname="Arial", fontsize=None):
        self.text = text
        self.fontname = fontname
        if not fontsize == None:
            self.fontsize = fontsize
        self.font = pygame.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pygame.font.Font.size(self.font, self.text)
        if self.width_type == "text":
            self.width = self.text_width + 20
        self.buttonUP = pygame.Surface((self.width, self.height))
        self.buttonDOWN = pygame.Surface((self.width, self.height))
        self.buttonHOVER = pygame.Surface((self.width, self.height))
        self.__update__()

class InputBox:

    def __init__(self, screen,x, y, w, h, text=''):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.LIGHT_GREY = (180,180,180)
        self.textBackground = (255,255,255)
        self.outershadowWidth = 2
        self.outershadowHeight = 2
        self.shadowWidth = 2
        self.shadowHeight = 2
        self.xoffset = 1
        self.yoffset = 1
        self.shadowRect = pygame.Rect(x+self.xoffset ,y+self.yoffset ,w-self.shadowWidth,h-self.shadowHeight)
        self.shadowRectOuter = pygame.Rect(x-self.xoffset ,y-self.yoffset ,w+self.shadowWidth,h+self.shadowHeight)
        self.rect = pygame.Rect(x, y, w, h)
        self.rectBackground = pygame.Rect(x+1,y+1,w-1,h-1)
        self.color = COLOR_INACTIVE
        self.backgroundColor = BACKGROUND_INACTIVE
        self.text = text
        self.textCopy = ''
        self.FONT = pygame.font.SysFont("cambriacambriamath", 16)
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.font_size = 18
        self.cursor_color=(0, 0, 1)
        self.cursor_surface = pygame.Surface((int(self.font_size / 40 + 1), self.font_size-2))
        self.cursor_surface.fill(self.cursor_color)
        self.textBackgroundSurface = pygame.Surface((self.w, self.h))
        self.cursor_position    = len("")  # Inside text
        self.cursor_visible     = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms   = 500
        self.cursor_ms_counter  = 0
        self.max_string_length  = 100
        self.keydown            = False
        self.backspaceDelay     = 100
        self.timer              = 0
        self.keyTimer           = 0
        self.backspaceTimer     = 0
        self.clock = pygame.time.Clock()
        self.wipeTextOnReturn = False
        self.countWipe        = 0
    def handle_event(self,screen,events):
        self.screen = screen
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
                self.backgroundColor = BACKGROUND_ACTIVE if self.active else BACKGROUND_INACTIVE
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        self.textCopy = self.text
                        self.text = ''
                    else:
                        if ((len(self.text) < self.max_string_length) or (self.max_string_length == -1)):
                            if (event.unicode.isnumeric() or event.unicode == 'x'):
                                # If no special key is pressed, add unicode of key to text
                                self.text = self.text[:self.cursor_position] + event.unicode + self.text[self.cursor_position:]
                                self.cursor_position = len(self.text)  # Some are empty, e.g. K_UP
                    if (event.key == pygame.K_BACKSPACE):
                        self.text = self.text[:-1]
                        # Subtract one from cursor_pos, but do not go below zero:
                        self.cursor_position = max(self.cursor_position - 1, 0)
                        self.keydown         = True
                    if (event.key == pygame.K_LEFT):
                        if (self.cursor_position > 0):
                            self.cursor_position = self.cursor_position - 1
                    if (event.key == pygame.K_RIGHT):
                        # Add one to cursor_pos, but do not exceed len(text)
                        if (self.cursor_position < len(self.text)):
                            self.cursor_position = self.cursor_position + 1

            if event.type == pygame.KEYUP:
                self.keydown          = False
                self.backspaceTimer   = 0
                self.timer            = 0
                self.keyTimer         = 0

        #Handles backspace helddown, alternative to putting extra events on queue or using set_repeat
        #Putting set_repeat(1,30) in a program using this will mess up the event queue
        if (self.keydown == True):
            self.backspaceTimer += self.clock.get_time()
            self.timer += 1
            if (self.backspaceTimer >= self.backspaceDelay and (self.timer == 10)):
                self.text = self.text[:-1]
                #Subtract one from cursor_pos, but do not go below zero:
                self.cursor_position = max(self.cursor_position - 1, 0)
                self.timer = 0

        #Get key states
        key_states = pygame.key.get_pressed()
            
        if (key_states[pygame.K_END]):
            self.cursor_position = len(self.text)

        if (key_states[pygame.K_HOME]):
            self.cursor_position = 0

        # Re-render the text.
        if (self.active and self.text == ""):
            self.txt_surface = self.FONT.render(" ", True, self.color)
        else: 
            self.txt_surface = self.FONT.render(self.text, True, self.color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if (self.cursor_ms_counter >= self.cursor_switch_ms):
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.FONT.size(self.text[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if (self.cursor_position > 0):
                if (cursor_y_pos > 0):
                    cursor_y_pos -= self.cursor_surface.get_width()
            self.txt_surface.blit(self.cursor_surface, (cursor_y_pos, 2))
        
        self.update()

        self.draw(self.screen)

        self.clock.tick()

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w            = width
        self.shadowRect.w      = width-self.shadowWidth
        self.shadowRectOuter.w = width+self.shadowWidth
        self.rectBackground.w  = width-self.shadowWidth

    def draw(self, screen):
        # Blit the text
        roundedEdgeNum = 5
        pygame.draw.rect(screen, self.backgroundColor, self.rectBackground, 0,roundedEdgeNum)
        screen.blit(self.txt_surface, (self.rect.x+2, self.rect.y+2))

        pygame.draw.rect(screen, self.color, self.rect, 1,roundedEdgeNum)

def main():
    pygame.init()
    input_box1 = InputBox(screen,100, 100, 140, 32)

    done = False

    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True

        stuff = input_box1.handle_event(events)

        pygame.display.flip()



if __name__ == '__main__':
    main()
    pygame.quit()