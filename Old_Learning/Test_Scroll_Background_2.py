import pygame
import sys
import pygame.sprite as sprite
pygame.init()
theClock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255, 255, 255)
background = pygame.image.load('track.png')
background2 = pygame.image.load('track.png')
background_size = background.get_size()
background_rect = background.get_rect()
background_rect2 = background2.get_rect()

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
key_order = []
index = 0
while running:
    #screen.blit(background,background_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        down = event.type == pygame.KEYDOWN
            #keys = pygame.key.get_pressed()
        if (down):
            key_order.append(event.key)
    if(down):
        #print(down)
        if ( len(key_order) != 0 ):
            for queue in key_order:
                if queue == pygame.K_UP:
                    #player_rect.y -= -cameraY
                    cameraY +=3
                    keystates['up'] = True
                    key_order.remove(queue)
                if queue == pygame.K_DOWN:
                    keystates['down'] = True
                    #player_rect.y += -cameraY
                    cameraY -= 3
                    key_order.remove(queue)
                if queue == pygame.K_LEFT:
                    #player_rect.x -= -cameraX
                    cameraX += 3
                    keystates['left'] = True
                    key_order.remove(queue)
                if queue == pygame.K_RIGHT:
                    #player_rect.x += -cameraY
                    cameraY -= 3
                    keystates['right'] = True
                    key_order.remove(queue)
        if keystates['up']:
            player_rect.y -= 3
            cameraY +=3
        if keystates['down']:
            player_rect.y += 3
            cameraY -= 3
        if keystates['left']:
            player_rect.x -= 3
            cameraX += 3
        if keystates['right']:
            player_rect.x += 3
            cameraX -= 3
    else:   
        keystates['up']    = False
        keystates['down']  = False 
        keystates['left']  = False
        keystates['right'] = False

    # if player_rect.x > w-50 and keystates['right'] and player_rect.x <2.25*w:
        # cameraX += 10
    # elif player_rect.x < 0 and keystates['left']:
        # cameraX -= 10   
    # elif player_rect.y > h and keystates['down']:
        # cameraY +=10
    # elif player_rect.y < 0 and keystates['up']:
        # cameraY -=10
    # if player_rect.x < w-50:
        # screen.blit(background,(0 - cameraX,0 - cameraY))
    # elif player_rect.x > w-50 and player_rect.x:
        # screen.blit(background2,(w-50 - cameraX, 0 - cameraY))
        # print(1)
    #background.fill(BLACK)
    screen.blit(background, (cameraX,cameraY))
    screen.blit(player,(player_rect.x,player_rect.y))
    # if cameraX > w:
        # cameraX = -w
    # if cameraY > h:
        # cameraY = -h
    pygame.display.flip()
    pygame.display.update()
    theClock.tick(60)