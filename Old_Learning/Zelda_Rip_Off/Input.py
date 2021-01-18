import pygame

class Input(object):
    """
    Class - Input()
               Summary: Responsible for grouping key inputs 
                        and updating the game loop with pressed keys 
               Limitations: Currently only checks keynoard up,down, right, and left
               
               Future Improvements: Add other keyboard key listening logic, and allow player
                                    to map the keys to their own liking, but have a default 
                                    key mapping
    """
    def __init__(self):
        self.keystates={'up':False, 'down':False, 'left':False, 'right':False}
    def update(self):
        currently_pressed = pygame.key.get_pressed()
        #print(currently_pressed)
        if currently_pressed[pygame.K_UP]:
            self.keystates['up'] = True
        else:
            self.keystates['up'] = False
        if currently_pressed[pygame.K_DOWN]:
            self.keystates['down'] = True
        else:
            self.keystates['down'] = False
        if currently_pressed[pygame.K_LEFT]:
            self.keystates['left'] = True
        else:   
            self.keystates['left'] = False
        if currently_pressed[pygame.K_RIGHT]:
            self.keystates['right'] = True
           # print("Got here")
        else:
            self.keystates['right'] = False
        
        return self.keystates