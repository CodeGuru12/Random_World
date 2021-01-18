#Imports
import pygame
import random
import os
import errno
from pygame.locals import (
                            RLEACCEL,
                            K_UP,
                            K_DOWN,
                            K_LEFT,
                            K_RIGHT,
                            K_ESCAPE,
                            KEYDOWN,
                            QUIT,
                            )

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1000




def get_file_path(file_directory, fileName):
    '''
    get_file_path 
    Description: Get absolute file path from running directory, it will 
                 raise a FileNotFoundError exception if the file doesn't exist

    Inputs: file_directory- Folder from current directory
            fileName - name of file to get path of
    
    Outputs: Absolute path to file

    run_directory - Is the current run path, while file_directory is the file path
    below the current root directory.
    '''
    run_directory = os.path.dirname(__file__)
    file_path = os.path.join(run_directory, file_directory,fileName)

    if (not os.path.isfile(file_path)):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),file_path)

    return file_path


# Define the cloud object by extending pygame.sprite.Sprite

# Use an image for a better-looking sprite



class Cloud(pygame.sprite.Sprite):
    def __init__(self, cycle_cloud):
        super(Cloud, self).__init__()
        clouds = {'cloud1': 'Cloud1.png', 'cloud2': 'Cloud2.png', 'cloud3': 'Cloud3.png'}
        cloud_image = [cloud for key,cloud in clouds.items() if cycle_cloud in key]
        self.surf = pygame.image.load(get_file_path('Assets/Scenery',cloud_image[0])).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(get_file_path('Assets/Characters','flying_person2.png')).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
    
    def update(self,pressed_keys):
        speed = 10
        if (pressed_keys[K_UP]):
            self.rect.move_ip(0,-speed)
            move_up_sound.play()
        if (pressed_keys[K_DOWN]):
            self.rect.move_ip(0,speed)
            move_down_sound.play()
        if (pressed_keys[K_LEFT]):
            self.rect.move_ip(-speed,0)
        if (pressed_keys[K_RIGHT]):
            self.rect.move_ip(speed,0)

        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > SCREEN_WIDTH):
            self.rect.right = SCREEN_WIDTH
        if (self.rect.top <= 0):
            self.rect.top = 0
        if (self.rect.bottom >= SCREEN_HEIGHT):
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(get_file_path('Assets/Enemies','dragon_flying2.png')).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect(
            center = (random.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100),
                      random.randint(0,SCREEN_HEIGHT),
                     )
                                                
                                      )
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if (self.rect.right < 0):
            self.kill()


pygame.init()
#pygame.mixer.pre_init(44100, 16, 2, 4096)
# Setup for sounds. Defaults are good.
pygame.mixer.init()



pygame.mixer.music.load(get_file_path('Assets/sound/music','Apoxode_Electric_1.wav'))
#pygame.mixer.music.load(get_file_path('Assets/sound/sound_effects','Rising_putter.ogg'))
#pygame.mixer.music.load(get_file_path('Assets/sound/sound_effects','Collision.ogg'))
pygame.mixer.music.play(loops=-1)

# Load all sound files
move_up_sound = pygame.mixer.Sound(get_file_path('Assets/sound/sound_effects','Rising_putter.wav'))
move_down_sound = pygame.mixer.Sound(get_file_path('Assets/sound/sound_effects','Falling_putter.wav'))
collision_sound = pygame.mixer.Sound(get_file_path('Assets/sound/sound_effects','Collision.wav'))

pygame.mixer.music.play(loops=-1)

#Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


ADDCLOUD = pygame.USEREVENT + 2

pygame.time.set_timer(ADDCLOUD, 1000)


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,750)

#Instantiate player
player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#Setup clock for framerate
clock = pygame.time.Clock()

running = True
count = 0
cloud_key = ['cloud1', 'cloud2', 'cloud3']

while running:
    #Event queue loop
    for event in pygame.event.get():
        #Check for keydown
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                running = False
        elif (event.type == QUIT):
            running = False
        elif (event.type == ADDENEMY):
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud(cloud_key[count])

            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            count += 1
            if (count > 2):
                count = 0
    pressed_keys = pygame.key.get_pressed()
    
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    #Make screen black
    screen.fill((128,0,128))

    #Draw player on screen
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    if (pygame.sprite.spritecollideany(player,enemies)):
        collision_sound.play()
        player.kill()
        move_up_sound.stop()
        move_down_sound.stop()
        
        running = False

    #Update display
    pygame.display.flip()

    clock.tick(60)

pygame.mixer.music.stop()
pygame.mixer.quit()