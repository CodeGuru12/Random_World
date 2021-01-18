import pygame
import sys
import pygame.sprite as sprite
pygame.init()
theClock = pygame.time.Clock()

WHITE = (255, 255, 255)
background = pygame.image.load('track.png')

background_size = background.get_size()
background_rect = background.get_rect()

screen = pygame.display.set_mode(background_size)
player = pygame.image.load('Zelda_Front_Left.png').convert()
player_rect = player.get_rect()
player_rect.y = 0
player_rect.x = 0
w,h = background_size
player.set_colorkey(WHITE)
running = True
cameraX = 0
cameraY = 0
keystates={'up':False, 'down':False, 'left':False, 'right':False}

while running:
    #screen.blit(background,background_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #keys = pygame.key.get_pressed()
            if event.key == pygame.K_UP:
                print(pygame.K_UP)
                keystates['up'] = True 
            if event.key == pygame.K_DOWN:
                keystates['down'] = True  
            if event.key == pygame.K_LEFT:
                keystates['left'] = True
            if event.key == pygame.K_RIGHT:
                keystates['right'] = True 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keystates['up'] = False
            if event.key == pygame.K_DOWN:
                keystates['down'] = False 
            if event.key == pygame.K_LEFT:
                keystates['left'] = False
            if event.key == pygame.K_RIGHT:
                keystates['right'] = False
    if keystates['left']:
        player_rect.x -= 3
    elif keystates['right']:
        player_rect.x += 3
    elif keystates['up']:
        player_rect.y -= 3
    elif keystates['down']:
        player_rect.y += 3  

    if player_rect.x > w:
        cameraX += 10
    elif player_rect.x < 0:
        cameraX -= 10   
    elif player_rect.y > h:
        cameraY +=10
    elif player_rect.y < 0:
        cameraY -=10
    screen.blit(background,(cameraX,cameraY))
    screen.blit(player,(player_rect.x - cameraX,player_rect.y - cameraY))
    if cameraX > w:
        cameraX = -w
    if cameraY > h:
        cameraY = -h
    pygame.display.flip()
    pygame.display.update()
    theClock.tick()