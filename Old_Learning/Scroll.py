

# Attempt at scrolling
import pygame
from pygame.locals import *
pygame.init()
# All colors used
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 100, 0)
purple = (255, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
colors = [green, blue, orange, purple, white]
# Initialize the screen you see
window_width = 600
window_height = 480
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Scrolling Attempt!")
# Draw the main map
# (Draw what you want here)
map_width = 2000
map_height = 700
main_map = pygame.Surface((map_width, map_height))
main_map = main_map.convert()
def draw():
    main_map.fill(black)
    rect1 = pygame.draw.rect(main_map, red, (250, 40, 1700, 400))
    circle1 = pygame.draw.circle(main_map, white, (1000, 300), 20)
    circle1 = pygame.draw.circle(main_map, green, (1000, 200), 20)
    circle1 = pygame.draw.circle(main_map, blue, (1000, 100), 20)
draw()
# The coords you see
map_x = 0 # Only this should change
map_y = 0
# The change for x
map_x_c = -3
screen.blit(main_map, (map_x, map_y, window_width, window_height))
pygame.display.flip()
print(map_x, map_y, map_x+window_width, map_y+window_height)
ucircle = pygame.draw.circle(screen, orange, (int((-map_x+window_width)/2)+-map_x, int((map_y+window_height)/2)), 20)
# The program
while True:
    for event in pygame.event.get():
        pass
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]: #and map_x != 0:
        map_x -= map_x_c
        print(map_x, map_y, map_x+window_width, map_y+window_height)
        #draw()
        #ucircle = pygame.draw.circle(main_map, orange, ((((-map_x+window_width)/2)+(-(map_x)/2)), (((-map_y+window_width)/2)+(-(map_y)/2))), 20)
    if key_pressed[K_RIGHT]: #and map_x != 2000:
        map_x += map_x_c
        print(map_x, map_y, map_x+window_width, map_y+window_height)
        #draw()
        #ucircle = pygame.draw.circle(main_map, orange, ((((-map_x+window_width)/2)+(-(map_x)/2)), (((-map_y+window_width)/2)+(-(map_y)/2))), 20)
    if key_pressed[K_UP]: #and map_x != 0:
        map_y -= map_x_c
        print(map_x, map_y, map_x+window_width, map_y+window_height)
        #draw()
        #ucircle = pygame.draw.circle(main_map, orange, ((((-map_x+window_width)/2)+(-(map_x)/2)), (((-map_y+window_width)/2)+(-(map_y)/2))), 20)
    if key_pressed[K_DOWN]: #and map_x != 2000:
        map_y += map_x_c
        print(map_x, map_y, map_x+window_width, map_y+window_height)
        #draw()
        #ucircle = pygame.draw.circle(main_map, orange, ((((-map_x+window_width)/2)+(-(map_x)/2)), (((-map_y+window_width)/2)+(-(map_y)/2))), 20)
    if key_pressed[K_ESCAPE]:
        quit()
    if map_x > 0:
        map_x = 0
    if map_x < -(map_width-window_width):
        map_x = -(map_width-window_width)
        
    if map_y > 0:
        map_y = 0
    if map_y < -(map_height-window_height):
        map_y = -(map_height-window_height)
    screen.blit(main_map, (map_x, map_y, window_width, window_height))
    ucircle = pygame.draw.circle(screen, orange, (int(window_width/2),int(window_height/2), 20)
    pygame.display.flip()

