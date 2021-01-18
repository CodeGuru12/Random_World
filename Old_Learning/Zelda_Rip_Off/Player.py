import pygame
import math

class Player(object):
    def __init__(self, color, path):
        self.SPRITEX = 40
        self.SPRITEY = 40
        #self.cCamera = Camera(localMapWidth, localMapHeight)
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey(color)
        self.player_rect = self.image.get_rect()
        self.player_rect.x = 0
        self.player_rect.y = 0
        self.speed = 3
        
    def update(self, InputState):
        keystates = InputState.update()
        if keystates['right'] and keystates['up']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x +self.player_rect.y*self.player_rect.y +  self.speed*self.speed)
            self.player_rect.y = self.player_rect.y- 1/math.sqrt(self.player_rect.y*self.player_rect.y + self.player_rect.x*self.player_rect.x+ self.speed*self.speed)
            #print(math.sqrt(self.player_rect.x*self.player_rect.x + self.player_rect.y*self.player_rect.y))
        if keystates['right'] and keystates['down']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x +self.player_rect.y*self.player_rect.y +  self.speed*self.speed)
            self.player_rect.y = self.player_rect.y- 1/math.sqrt(self.player_rect.y*self.player_rect.y + self.player_rect.x*self.player_rect.x+ self.speed*self.speed)
        if keystates['left'] and keystates['down']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x +self.player_rect.y*self.player_rect.y +  self.speed*self.speed)
            self.player_rect.y = self.player_rect.y- 1/math.sqrt(self.player_rect.y*self.player_rect.y + self.player_rect.x*self.player_rect.x+ self.speed*self.speed)
        if keystates['left'] and keystates['up']:
            self.player_rect.x = self.player_rect.x+ 1/math.sqrt(self.player_rect.x*self.player_rect.x +self.player_rect.y*self.player_rect.y +  self.speed*self.speed)
            self.player_rect.y = self.player_rect.y- 1/math.sqrt(self.player_rect.y*self.player_rect.y + self.player_rect.x*self.player_rect.x+ self.speed*self.speed)
        if keystates['right']:
            self.player_rect.x += self.speed
        if keystates['left']:
            self.player_rect.x -= self.speed
        if keystates['up']:
            self.player_rect.y -= self.speed
        if keystates['down']:
            self.player_rect.y += self.speed