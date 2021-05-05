import pygame
import pygame.font
import sys
import os
import math
import random
import numpy
from pygame.locals import *
import os.path
#sys.path.append(
#    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import common_utilities
from pygame.rect import Rect
import textBox

#preettings
size = 2
pygame.init()
icon_surface = pygame.image.load(common_utilities.get_file_path("MapEditor/Icon_rubikscub.png")).convert_alpha()
pygame.display.set_icon(icon_surface)
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Level Editor")
#pygame.mouse.set_visible(False)
#pygame.key.set_repeat(1, 30)
clock = pygame.time.Clock()
tilee01 = pygame.image.load("tilee1.png").convert_alpha()
tilee01 = pygame.transform.scale(tilee01, (20, 20))
tilee02 = pygame.image.load("tilee2.png").convert_alpha()
tilee02 = pygame.transform.scale(tilee02, (20, 20))
tilee03 = pygame.image.load("tilee3.png").convert_alpha()
tilee03 = pygame.transform.scale(tilee03, (20, 20))
tilee04 = pygame.image.load("tilee4.png").convert_alpha()
tilee04 = pygame.transform.scale(tilee04, (20, 20))
tilee05 = pygame.image.load("tilee5.png").convert_alpha()
tilee05 = pygame.transform.scale(tilee05, (20, 20))
tilee06 = pygame.image.load("tilee6.png").convert_alpha()
tilee06 = pygame.transform.scale(tilee06, (20, 20))
tilee07 = pygame.image.load("tilee7.png").convert_alpha()
tilee07 = pygame.transform.scale(tilee07, (20, 20))
tilee08 = pygame.image.load("tilee8.png").convert_alpha()
tilee08 = pygame.transform.scale(tilee08, (20, 20))
tilee09 = pygame.image.load("tilee9.png").convert_alpha()
tilee09 = pygame.transform.scale(tilee09, (20, 20))
#cursor = pygame.image.load("cursor.png").convert_alpha()
#cursor = pygame.transform.scale(cursor, (10, 10))

tilee1 = pygame.image.load("tilee1.png").convert_alpha()
tilee1 = pygame.transform.scale(tilee1, (int(20 * size), int(20 * size)))
tilee2 = pygame.image.load("tilee2.png").convert_alpha()
tilee2 = pygame.transform.scale(tilee2, (int(20 * size), int(20 * size)))
tilee3 = pygame.image.load("tilee3.png").convert_alpha()
tilee3 = pygame.transform.scale(tilee3, (int(20 * size), int(20 * size)))
tilee4 = pygame.image.load("tilee4.png").convert_alpha()
tilee4 = pygame.transform.scale(tilee4, (int(20 * size), int(20 * size)))
tilee5 = pygame.image.load("tilee5.png").convert_alpha()
tilee5 = pygame.transform.scale(tilee5, (int(20 * size), int(20 * size)))
tilee6 = pygame.image.load("tilee6.png").convert_alpha()
tilee6 = pygame.transform.scale(tilee6, (int(20 * size), int(20 * size)))
tilee7 = pygame.image.load("tilee7.png").convert_alpha()
tilee7 = pygame.transform.scale(tilee7, (int(20 * size), int(20 * size)))
tilee8 = pygame.image.load("tilee8.png").convert_alpha()
tilee8 = pygame.transform.scale(tilee8, (int(20 * size), int(20 * size)))
tilee9 = pygame.image.load("tilee9.png").convert_alpha()
tilee9 = pygame.transform.scale(tilee9, (int(20 * size), int(20 * size)))
#cursor = pygame.image.load("cursor.png").convert_alpha()
#cursor = pygame.transform.scale(cursor, (10, 10))


def mapfunction():
    global xl
    global yl
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 0:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(int((x * 20 + xshift) * size), int((y * 20 + yshift) * size), int(20 * size), int(20 * size)), 1)
            if tile == 1:
                screen.blit(tilee1, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 2:
                screen.blit(tilee2, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 3:
                screen.blit(tilee3, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 4:
                screen.blit(tilee4, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 5:
                screen.blit(tilee5, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 6:
                screen.blit(tilee6, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 7:
                screen.blit(tilee7, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 8:
                screen.blit(tilee8, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            if tile == 9:
                screen.blit(tilee9, (int((x * 20 + xshift) * size), int((y * 20 + yshift) * size)))
            xl = x
            yl = y

def tilemenu():
    global tilee
    pygame.draw.rect(screen, (190, 190, 190), pygame.Rect(10, 710, 1380, 60), 0)
    txt = font.render(str(tilee), 1, (10, 10, 10))
    txt0 = font.render('0', 1, (10, 10, 10))
    txt1 = font.render('1', 1, (10, 10, 10))
    txt2 = font.render('2', 1, (10, 10, 10))
    txt3 = font.render('3', 1, (10, 10, 10))
    txt4 = font.render('4', 1, (10, 10, 10))
    txt5 = font.render('5', 1, (10, 10, 10))
    txt6 = font.render('6', 1, (10, 10, 10))
    txt7 = font.render('7', 1, (10, 10, 10))
    txt8 = font.render('8', 1, (10, 10, 10))
    txt9 = font.render('9', 1, (10, 10, 10))
    txt10 = font.render('w, a, s, d = move', 1, (10, 10, 10))
    txt11 = font.render('scroll = zoom', 1, (10, 10, 10))
    txt12 = font.render('p = save', 1, (10, 10, 10))
    screen.blit(txt, (660, 720))
    screen.blit(txt0, (20, 720))
    screen.blit(txt1, (80, 720))
    screen.blit(txt2, (140, 720))
    screen.blit(txt3, (200, 720))
    screen.blit(txt4, (260, 720))
    screen.blit(txt5, (320, 720))
    screen.blit(txt6, (380, 720))
    screen.blit(txt7, (440, 720))
    screen.blit(txt8, (500, 720))
    screen.blit(txt9, (560, 720))
    screen.blit(txt10, (750, 720))
    screen.blit(txt11, (1020, 720))
    screen.blit(txt12, (1250, 720))
    pygame.draw.rect(screen, (244, 244, 244), pygame.Rect(40, 730, 20, 20), 0)
    screen.blit(tilee01, (100, 730, 20, 20))
    screen.blit(tilee02, (160, 730, 20, 20))
    screen.blit(tilee03, (220, 730, 20, 20))
    screen.blit(tilee04, (280, 730, 20, 20))
    screen.blit(tilee05, (340, 730, 20, 20))
    screen.blit(tilee06, (400, 730, 20, 20))
    screen.blit(tilee07, (460, 730, 20, 20))
    screen.blit(tilee08, (520, 730, 20, 20))
    screen.blit(tilee09, (580, 730, 20, 20))
    if tilee == 0:
        pygame.draw.rect(screen, (244, 244, 244), pygame.Rect(680, 730, 20, 20), 0)
    if tilee == 1:
        screen.blit(tilee01, (680, 730, 20, 20))
    if tilee == 2:
        screen.blit(tilee02, (680, 730, 20, 20))
    if tilee == 3:
        screen.blit(tilee03, (680, 730, 20, 20))
    if tilee == 4:
        screen.blit(tilee04, (680, 730, 20, 20))
    if tilee == 5:
        screen.blit(tilee05, (680, 730, 20, 20))
    if tilee == 6:
        screen.blit(tilee06, (680, 730, 20, 20))
    if tilee == 7:
        screen.blit(tilee07, (680, 730, 20, 20))
    if tilee == 8:
        screen.blit(tilee08, (680, 730, 20, 20))
    if tilee == 9:
        screen.blit(tilee09, (680, 730, 20, 20))
        

def mousefunction():
    global tilee
    global xl
    global yl
    if int(mx - (xshift * size)) > 0 and int(my - (yshift * size)) > 0:
        mx2 = int((mx - (xshift * size)) // (20 * size))
        my2 = int((my - (yshift * size)) // (20 * size))
        if mx2 <= xl  and my2 <= yl:
            map_data[my2][mx2] = tilee

def text(text1, text2, text3, text4, text5):
        text01 = font.render(str(text1), 1, (10, 10, 10))
        text02 = font.render(str(text2), 1, (10, 10, 10))
        text03 = font.render(str(text3), 1, (10, 10, 10))
        text04 = font2.render(str(text4), 1, (10, 10, 10))
        text05 = font2.render(str(text5), 1, (10, 10, 10))
        screen.blit(text01, (20, 20))
        screen.blit(text02, (20, 70))
        screen.blit(text03, (20, 120))
        screen.blit(text04, (20, 250))
        screen.blit(text05, (20, 350))

def round_down(n, decimals = 0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
                    


tilee = 1
font = pygame.font.SysFont('berlin sans fb', 28, True)
font2 = pygame.font.SysFont('berlin sans fb', 40, True)
xshift = 0
yshift = 0
xl = 1
yl = 1
mousestatus = False
xres = 0
yres = 0
res = 'x'


Xinput_box = textBox.InputBox(screen,200, 250, 140, 32)
Yinput_box = textBox.InputBox(screen,100, 250, 140, 32)


start = True
while start:
    screen.fill((244, 244, 244))
    mx, my = pygame.mouse.get_pos()
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                start = False
                sys.exit()
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            start = False
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            if False:#event.type == pygame.MOUSEBUTTONDOWN:
                if mx > 215 and mx < 550 and my > 555 and my < 590:
                    start = False
                    main = True
                    map_data = numpy.zeros((yres, xres), dtype=int)
                    with open('map.txt', 'w') as f:
                        for y, row in enumerate(map_data):
                            if y != 0:
                                f.write('\n')
                            for x, tile in enumerate(row):
                                f.write('%s' % tile)
                if mx > 915 and mx < 1185 and my > 555 and my < 590:
                    start = False
                    main = True
                    m = open("map.txt")
                    map_data = [[int(c) for c in row] for row in m.read().split('\n')]
        
    xres = Xinput_box.handle_event(events)
    yres = Yinput_box.handle_event(events)
                
    #if xres < 0:
    #    xres = 0
    #if yres < 0:
    #    yres = 0
    #if xres > 150:y
    #    xres = 150
    #if yres > 150:
    #    yres = 150

        
    text("You can use your own tiles by changing the tile.png in this folder by your own images. You have to",
         "name the tiles 'tileex.png'; tilee with 2 e's and x has to be  a number between 1 and 9.",
         "select a resolution (press 'x' or 'y' and a number):",
         "  x =  " + str(xres),
         "  y =  " + str(yres))
    text1 = font2.render("create new map", 1, (10, 10, 10))
    text2 = font2.render("load map.txt", 1, (10, 10, 10))
    screen.blit(text1, (220, 550))
    screen.blit(text2, (915, 550))
    #screen.blit(cursor, (mx - 5, my - 5))
    pygame.display.flip()

main = True
while main:
    screen.fill((244, 244, 244))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
                # Check for QUIT event. If QUIT, then set running to false.
        if event.type == QUIT:
            main = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                main = False
                sys.exit()
            if event.key == ord('0'):
                tilee = 0
            if event.key == ord('1'):
                tilee = 1
            if event.key == ord('2'):
                tilee = 2
            if event.key == ord('3'):
                tilee = 3
            if event.key == ord('4'):
                tilee = 4
            if event.key == ord('5'):
                tilee = 5
            if event.key == ord('6'):
                tilee = 6
            if event.key == ord('7'):
                tilee = 7
            if event.key == ord('8'):
                tilee = 8
            if event.key == ord('9'):
                tilee = 9
            if event.key == ord('a'):
                xshift += 20
            if event.key == ord('d'):
                xshift -= 20
            if event.key == ord('w'):
                yshift += 20
            if event.key == ord('s'):
                yshift -= 20
            if event.key == ord('p'):
                with open('map.txt', 'w') as f:
                    for y, row in enumerate(map_data):
                        if y != 0:
                            f.write('\n')
                        for x, tile in enumerate(row):
                            f.write('%s' % tile)

                        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousestatus = True
            if event.button == 4 and size < 4:
                size += 0.1
                size = round(size, 2)
                tilee1 = pygame.image.load("tilee1.png").convert_alpha()
                tilee1 = pygame.transform.scale(tilee1, (int(20 * size), int(20 * size)))
                tilee2 = pygame.image.load("tilee2.png").convert_alpha()
                tilee2 = pygame.transform.scale(tilee2, (int(20 * size), int(20 * size)))
                tilee3 = pygame.image.load("tilee3.png").convert_alpha()
                tilee3 = pygame.transform.scale(tilee3, (int(20 * size), int(20 * size)))
                tilee4 = pygame.image.load("tilee4.png").convert_alpha()
                tilee4 = pygame.transform.scale(tilee4, (int(20 * size), int(20 * size)))
                tilee5 = pygame.image.load("tilee5.png").convert_alpha()
                tilee5 = pygame.transform.scale(tilee5, (int(20 * size), int(20 * size)))
                tilee6 = pygame.image.load("tilee6.png").convert_alpha()
                tilee6 = pygame.transform.scale(tilee6, (int(20 * size), int(20 * size)))
                tilee7 = pygame.image.load("tilee7.png").convert_alpha()
                tilee7 = pygame.transform.scale(tilee7, (int(20 * size), int(20 * size)))
                tilee8 = pygame.image.load("tilee8.png").convert_alpha()
                tilee8 = pygame.transform.scale(tilee8, (int(20 * size), int(20 * size)))
                tilee9 = pygame.image.load("tilee9.png").convert_alpha()
                tilee9 = pygame.transform.scale(tilee9, (int(20 * size), int(20 * size)))
            if event.button == 5 and size > 0.5:
                size -= 0.1
                size = round(size, 2)
                tilee1 = pygame.image.load("tilee1.png").convert_alpha()
                tilee1 = pygame.transform.scale(tilee1, (int(20 * size), int(20 * size)))
                tilee2 = pygame.image.load("tilee2.png").convert_alpha()
                tilee2 = pygame.transform.scale(tilee2, (int(20 * size), int(20 * size)))
                tilee3 = pygame.image.load("tilee3.png").convert_alpha()
                tilee3 = pygame.transform.scale(tilee3, (int(20 * size), int(20 * size)))
                tilee4 = pygame.image.load("tilee4.png").convert_alpha()
                tilee4 = pygame.transform.scale(tilee4, (int(20 * size), int(20 * size)))
                tilee5 = pygame.image.load("tilee5.png").convert_alpha()
                tilee5 = pygame.transform.scale(tilee5, (int(20 * size), int(20 * size)))
                tilee6 = pygame.image.load("tilee6.png").convert_alpha()
                tilee6 = pygame.transform.scale(tilee6, (int(20 * size), int(20 * size)))
                tilee7 = pygame.image.load("tilee7.png").convert_alpha()
                tilee7 = pygame.transform.scale(tilee7, (int(20 * size), int(20 * size)))
                tilee8 = pygame.image.load("tilee8.png").convert_alpha()
                tilee8 = pygame.transform.scale(tilee8, (int(20 * size), int(20 * size)))
                tilee9 = pygame.image.load("tilee9.png").convert_alpha()
                tilee9 = pygame.transform.scale(tilee9, (int(20 * size), int(20 * size)))

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mousestatus = False

        if mousestatus == True:
            mousefunction()
 
    mapfunction()
    tilemenu()
    #screen.blit(cursor, (mx - 5, my - 5))
    pygame.display.flip()
