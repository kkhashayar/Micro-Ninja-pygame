import pygame
from random import choice, randrange, randint
from os import path
from sys import exit
from pygame import mixer
from math import hypot, sin, cos, radians, atan2, degrees
from map import *
from time import sleep
from pygame.locals import *
import math

pygame.init()
mixer.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(0, 500)
################# CONSTANTS
# 640x544
BLOCK_SIZE = 32
SCREEN_WIDTH = BLOCK_SIZE * 20
SCREEN_HEIGHT = BLOCK_SIZE * 17
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption("Micro Ninja V 5 By: K.N")
global FPS
FPS = 60
#--this should be disabled for pause menu
#--pygame.key.set_repeat(1,1000)
pygame.mouse.set_visible(False)
img_dir = path.join(path.dirname(__file__), "img")
snd_dir = path.join(path.dirname(__file__), 'snd')
################# ASSETS

#-- Menu
cursor_sound = mixer.Sound(path.join(snd_dir,"cursor_sound.ogg"))
mouse_hover_sound = mixer.Sound(path.join(snd_dir,"mouse_scroll.ogg"))
menu_bg = pygame.image.load(path.join(img_dir,"menu_bg.png")).convert_alpha()
pause_menu_bg = pygame.image.load(path.join(img_dir,"bg_pause_menu.png")).convert_alpha()
end_screen_bg = pygame.image.load(path.join(img_dir,"end_screen_bg.png")).convert_alpha()

#-- Player stuff
grenade_tile_sound = mixer.Sound(path.join(snd_dir,"grenade_tile.ogg"))
grenade_image = pygame.image.load(path.join(img_dir,"grenade.png")).convert_alpha()
grenade_throw_sound = mixer.Sound(path.join(snd_dir,"throw_grenade.ogg"))
grenade_pick_sound = mixer.Sound(path.join(snd_dir,"grenade_pick.ogg"))
ninja_star_image = pygame.image.load(path.join(img_dir,"ninja_star.png")).convert_alpha()
star_pickup_sound = mixer.Sound(path.join(snd_dir,"star_pickup.wav"))
all_coin_images = []
for i in range(6):
    image_name = "star_0{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"star_0{}.png".format(i))).convert_alpha()
    all_coin_images.append(image_name)

coin_pickup_sound_1 = mixer.Sound(path.join(snd_dir,"coin_pickup_1.ogg"))
key_image = pygame.image.load(path.join(img_dir,"key.png")).convert_alpha()
key_sound = mixer.Sound(path.join(snd_dir,"open_lock.ogg"))

life_image = pygame.image.load(path.join(img_dir,"life.png")).convert_alpha()
life_pickup_sound = mixer.Sound(path.join(snd_dir,"pickup_life.wav"))

#-- Player
player_walking_sound = mixer.Sound(path.join(snd_dir,"player_walk.ogg"))
player_trow_star = mixer.Sound(path.join(snd_dir,"throw_star.wav"))
player_throw_images = []
player_hurt_sound_1 = mixer.Sound(path.join(snd_dir,"player_hurt_1.ogg"))
player_hurt_sound_2 = mixer.Sound(path.join(snd_dir,"player_hurt_2.ogg"))
all_player_hurt_sounds =[player_hurt_sound_1, player_hurt_sound_2]
health_1_image = pygame.image.load(path.join(img_dir,"health_1.png")).convert_alpha()
health_2_image = pygame.image.load(path.join(img_dir,"health_2.png")).convert_alpha()
health_3_image = pygame.image.load(path.join(img_dir,"health_3.png")).convert_alpha()

for i in range(9):
    image_name = "throw_00{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"Throw__00{}.png".format(i))).convert_alpha()
    player_throw_images.append(image_name)

player_idle_images = []
for i in range(9):
    image_name = "idle_00{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"Idle__00{}.png".format(i))).convert_alpha()
    player_idle_images.append(image_name)

player_moving_images = []
for i in range(9):
    image_name = "player_move_right_00{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"Run__00{}.png".format(i))).convert_alpha()
    player_moving_images.append(image_name)

# player_dead_images = []
# for i in range(9):
#     image_name = "Dead_00{}.png".format(i)
#     image_name = pygame.image.load(path.join(img_dir,"Dead__00{}.png".format(i))).convert_alpha()
#     player_dead_images.append(image_name)

#-- Blocks
#block_image = pygame.image.load(path.join(img_dir,"block_bg_1.png")).convert_alpha()


stone_impact_00_sound = mixer.Sound(path.join(snd_dir,"stone_impact_00.ogg"))
stone_impact_01_sound = mixer.Sound(path.join(snd_dir,"stone_impact_01.ogg"))
stone_impact_02_sound = mixer.Sound(path.join(snd_dir,"stone_impact_02.ogg"))
all_stones_audio = [stone_impact_01_sound,stone_impact_00_sound,stone_impact_02_sound]

block_safe_image = pygame.image.load(path.join(img_dir,"block_safe.png")).convert_alpha()
all_bg_blocks = []
for i in range(3):
    image_name = "block_bg_{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"block_bg_{}.png".format(i))).convert_alpha()
    all_bg_blocks.append(image_name)

# island_image = pygame.image.load(path.join(img_dir,"island.png")).convert_alpha()
all_base_blocks = []
for i in range(4):
    image_name = "block_0{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"block_0{}.png".format(i))).convert_alpha()
    all_base_blocks.append(image_name)

half_block_image_00 = pygame.image.load(path.join(img_dir,"half_block_00.png")).convert_alpha()
block_image_04 = pygame.image.load(path.join(img_dir,"block_04.png")).convert_alpha()
block_image_02 = pygame.image.load(path.join(img_dir,"block_02.png")).convert_alpha()
block_elevator_image = pygame.image.load(path.join(img_dir,"block_elevator_01.png")).convert_alpha()
block_fire_place_image = pygame.image.load(path.join(img_dir,"block_fire_place.png")).convert_alpha()
block_lava_image = pygame.image.load(path.join(img_dir,"block_lava.png")).convert_alpha()

#-- Cursors
cursor_image = pygame.image.load(path.join(img_dir,"cursor.png")).convert_alpha()
cursor_image = pygame.transform.scale(cursor_image,(5,5))
cursor_image_2 = pygame.image.load(path.join(img_dir,"cursor_2.png")).convert_alpha()
cursor_image_2 = pygame.transform.scale(cursor_image,(5,5))

#-- Particles
running_particle_image = pygame.image.load(path.join(img_dir,"running_particle.png")).convert_alpha()
red_particle_image = pygame.image.load(path.join(img_dir,"red_particle.png")).convert_alpha()
light_particle_image = pygame.image.load(path.join(img_dir,"light_particle.png")).convert_alpha()
stuff_particle_image = pygame.image.load(path.join(img_dir,"stuff_particle.png")).convert_alpha()
star_to_tile_sound = mixer.Sound(path.join(snd_dir,"star_to_tile.ogg"))
gold_particle_image = pygame.image.load(path.join(img_dir,"gold_particle.png")).convert_alpha()
fire_burning_sound = mixer.Sound(path.join(snd_dir,"fire_burning.ogg"))
bird_particle_image = pygame.image.load(path.join(img_dir,"bird_particle.png")).convert_alpha()
explosive_particle_image = pygame.image.load(path.join(img_dir,"explosive_particle.png")).convert_alpha()
lava_image_1 = pygame.image.load(path.join(img_dir,"lava_particle_1.png")).convert_alpha()
lava_image_2 = pygame.image.load(path.join(img_dir,"lava_particle_2.png")).convert_alpha()

#-- Mobs
all_e1_walking = []
for i in range(8):
    image_name = "e1_walk_0{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"e1_walk_0{}.png".format(i))).convert_alpha()
    all_e1_walking.append(image_name)

all_bird_images = []
for i in range(8):
    image_name == "bird_0{}.png".format(i)
    image_name = pygame.image.load(path.join(img_dir,"bird_0{}.png".format(i))).convert_alpha()
    all_bird_images.append(image_name)

bird_sound_1 = mixer.Sound(path.join(snd_dir,"bird_1.ogg"))
bird_sound_2 = mixer.Sound(path.join(snd_dir,"bird_2.ogg"))
all_bird_sounds = [bird_sound_1, bird_sound_2]
bird_death_sound = mixer.Sound(path.join(snd_dir,"bird_death.ogg"))
egg_bomb_image = pygame.image.load(path.join(img_dir,"egg_bomb.png")).convert_alpha()

#-- E1 sounds
death_1 = mixer.Sound(path.join(snd_dir,"enemy_death_1.ogg"))
death_2 = mixer.Sound(path.join(snd_dir,"enemy_death_2.ogg"))
death_3 = mixer.Sound(path.join(snd_dir,"enemy_death_3.ogg"))
e1_all_death_sounds = [death_1,death_2,death_3]
e1_walking_sound = mixer.Sound(path.join(snd_dir,"e1_walking_sound.ogg"))

#- Screen map
block_map_image = pygame.image.load(path.join(img_dir,"block_map.png")).convert_alpha()
map_sound = mixer.Sound(path.join(snd_dir,"map_sound.wav"))

#-- Levels
level_cursor_image = pygame.image.load(path.join(img_dir,"level_cursor.png")).convert_alpha()
all_backgrounds = ["reserve"]


level_01_menu_background_image = pygame.image.load(path.join(img_dir,"level_01_menu_bg.png")).convert_alpha()
level_02_menu_background_image = pygame.image.load(path.join(img_dir,"level_02_menu_bg.png")).convert_alpha()
level_03_menu_background_image = pygame.image.load(path.join(img_dir,"level_03_menu_bg.png")).convert_alpha()
level_04_menu_background_image = pygame.image.load(path.join(img_dir,"level_04_menu_bg.png")).convert_alpha()

all_menu_backgrounds = ["reserve",level_01_menu_background_image,level_02_menu_background_image,level_03_menu_background_image,level_04_menu_background_image]

level_01_background_image = pygame.image.load(path.join(img_dir,"level_01_bg.jpg")).convert_alpha()
level_02__background_image = pygame.image.load(path.join(img_dir,"level_02_bg.png")).convert_alpha()
level_03__background_image = pygame.image.load(path.join(img_dir,"level_03_bg.png")).convert_alpha()

all_backgrounds.append(level_01_background_image)
all_backgrounds.append(level_02__background_image)
all_backgrounds.append(level_03__background_image)

dark_filter_image = pygame.image.load(path.join(img_dir,"dark_filter.png")).convert_alpha()
################# FUNCTIONS
ninja_font = pygame.font.Font("NinjaPenguin.ttf", 25)
ninja_font_menu = pygame.font.Font("NinjaPenguin.ttf", 30)
font_menu = pygame.font.SysFont(None, 30)
font_in_game = pygame.font.SysFont(None, 20)
def draw_text(text, font, color, surface, x,y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj, text_rect)

# clock.get_fps()

def create_button(name, frame,x,y, w,h, color_name, color_frame, text, cursor_x,cursor_y, click, function_name):
    name = pygame.Rect(x,y, w,h)
    frame = pygame.Rect(x,y, w+7,h+7)
    pygame.draw.rect(screen, (pygame.color.Color(color_frame)), frame)
    pygame.draw.rect(screen, (pygame.color.Color(color_name)), name)
    draw_text(text, ninja_font_menu, pygame.color.Color(color_frame), screen, x+25, y+5)
    if name.collidepoint((cursor_x,cursor_y)):
        pygame.draw.rect(screen, (pygame.color.Color(color_name)), frame)
        pygame.draw.rect(screen, (pygame.color.Color(color_frame)), name)
        draw_text(text, font_menu, pygame.color.Color(color_name), screen, x+25, y+5)
        if click:
            cursor_sound.play()
            function_name()
#-- Explosives :D
def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color,(radius,radius), radius)
    surf.set_colorkey((pygame.Color("black")))
    return surf
special_particles = []
################# CLASSES
class Rotate_object(pygame.sprite.Sprite):
    def __init__(self, x,y, width,height, image):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_orig = pygame.transform.scale(image,(self.width, self.height))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.rot = 0 #-- Frame distance change in each update
        self.last_update = pygame.time.get_ticks()
        self.speed = 160
         #-- Frame speed
        self.alpha_degree = 30
        self.alpha_timer = pygame.time.get_ticks()
        self.alpha_switch = True

    def update(self):
        self.rotate()
        self.image.set_alpha(self.alpha_degree)
        if self.alpha_degree >= randrange(20,25):
            self.alpha_degree = randrange(5,15)
        self.alpha_degree += 0.1
        self.rect.x -= 1 #randrange(1,3)
        # self.rect.y += randrange(1,2) -1
        if self.rect.right <= 0:
            self.rect.left = (SCREEN_WIDTH + randrange(10,100))
            self.rect.y = 0

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.speed:
            self.last_update = now
            self.rot = (self.rot + 10) % 360 #-- Frame distance change in each update -number change the direction
            new_image = self.image_orig
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

#-- fire particles only to make fire :D
class Fire(pygame.sprite.Sprite):
    #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
    def __init__(self, x,y, width,height, image, x_direction,y_direction, duration, move_time_distance_random):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width #-- randrange(1,10)
        self.height = height #-- randrange(1,15)
        self.image = image #--light_particle
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.x_direction = x_direction #--randrange(-5, 5)
        self.y_direction = y_direction #--randrange(-5,5)
        self.last_update = pygame.time.get_ticks()
        self.duration = duration #-- randrange(120, 240)
        self.falling_duration = pygame.time.get_ticks()
        self.movem_time_distance = move_time_distance_random #--randrange(500,1000)
        self.gravity = 0.3
        self.acc = 1.1
        self.last_time_gravity_applied = pygame.time.get_ticks()
        self.gravity_switch = False
        self.last_time_second_layer_applied = pygame.time.get_ticks()
        self.second_layer_switch = False
        self.alpha_degree = 0
        self.alpha_degree_switch = False
        self.max_size = 60
        self.general_speed = 150
        self.general_loop = pygame.time.get_ticks()
        self.name = ""

    def activate_alpha(self):
        if self.alpha_degree < 200:
            self.alpha_degree += 20
            self.image.set_alpha(tile.alpha_degree)

    def update(self):
        if self.alpha_degree == True:
            self.activate_alpha()

        now = pygame.time.get_ticks()
        if now - self.general_loop > self.general_speed:
            #-- Algorithm for particle distro
            now = pygame.time.get_ticks()
            self.rect.x += self.x_direction
            self.rect.y += self.y_direction
            if now - self.last_update > self.duration:
                self.last_update = now
                fall_now = pygame.time.get_ticks()
                self.y_direction = self.x_direction#randrange(-3,-2)
                self.x_direction = self.y_direction#randrange(0,1)
                if fall_now - self.falling_duration > self.movem_time_distance:
                    self.falling_duration = fall_now
                    self.kill()
            self.general_loop = now

        if self.gravity_switch == True:
            self.apply_falling()

    def apply_falling(self):
        now = pygame.time.get_ticks()
        if now - self.last_time_gravity_applied > 20:
            self.gravity *= self.acc
            self.rect.y += self.gravity
            self.last_time_gravity_applied = now

#-- General particles
class Particle(pygame.sprite.Sprite):
    #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
    def __init__(self, x,y, width,height, image, x_direction,y_direction, duration, move_time_distance_random):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width #-- randrange(1,10)
        self.height = height #-- randrange(1,15)
        self.image = image #--light_particle
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.x_direction = x_direction #--randrange(-5, 5)
        self.y_direction = y_direction #--randrange(-5,5)
        self.last_update = pygame.time.get_ticks()
        self.duration = duration #-- randrange(120, 240)
        self.falling_duration = pygame.time.get_ticks()
        self.movem_time_distance = move_time_distance_random #--randrange(500,1000)
        self.gravity = 0.8
        self.acc = 1.1
        self.last_time_gravity_applied = pygame.time.get_ticks()
        self.gravity_switch = False
        self.last_time_second_layer_applied = pygame.time.get_ticks()
        self.second_layer_switch = False
        self.alpha_degree = 0
        self.alpha_degree_switch = False
        self.max_size = 60
        self.general_speed = 150
        self.general_loop = pygame.time.get_ticks()
        self.name = ""

    def activate_alpha(self):
        if self.alpha_degree < 200:
            self.alpha_degree += 1
            self.image.set_alpha(tile.alpha_degree)

    def update(self):
        general_update_now = pygame.time.get_ticks()
        if general_update_now - self.general_loop > 20:
            if self.alpha_degree == True:
                self.activate_alpha()
            #-- Algorithm for particle distro
            now = pygame.time.get_ticks()
            self.rect.x += self.x_direction
            self.rect.y += self.y_direction
            if now - self.last_update > self.duration:
                self.last_update = now
                fall_now = pygame.time.get_ticks()
                self.y_direction = self.x_direction#randrange(-3,-2)
                self.x_direction = self.y_direction#randrange(0,1)
                if fall_now - self.falling_duration > self.movem_time_distance:
                    self.falling_duration = fall_now
                    self.kill()

            if self.gravity_switch == True:
                self.apply_falling()

    def apply_falling(self):
        now = pygame.time.get_ticks()
        if now - self.last_time_gravity_applied > 20:
            self.gravity *= self.acc
            self.rect.y += self.gravity
            self.last_time_gravity_applied = now

class Drop(pygame.sprite.Sprite):
    def __init__(self, x,y, w,h, image):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.name = ""
        self.puff_switch = False



class Tile(pygame.sprite.Sprite):
    def __init__(self, x,y, w,h, image):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y
        self.name = ""
        self.count = 0
        self.speed = 1
        self.change_y = 0
        self.sound_switch = "off"

    def update(self):
        if self.name == 'block_elevator':
            self.vertical_movement()

    def vertical_movement(self):
        if self.count >= randrange(300, 700):
            self.count = 0
            self.speed *= -1
        if self.count < randrange(300, 700):
            self.rect.y -= self.speed
            self.count += 1

#-- Ninja star
class Star(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 6
        self.height = 1
        self.image = stuff_particle_image
        self.image = pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.switch = True
        self.speed = 10
        self.move = [0,0]
        self.target_luck = False
        self.direction = ""
        self.name = ""

    def update(self):
        self.rect.y += 1
        self.speed -= 0.5
        if self.speed <= 3:
            self.speed = 3
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed * 2

        if self.rect.x >0 and self.rect.x < SCREEN_WIDTH:
            self.switch = False
            self.rect.x += self.speed
        if self.rect.x >= SCREEN_WIDTH or self.rect.x <= 0:
            self.kill()
            self.switch = True

class Stuff(pygame.sprite.Sprite):
    def __init__(self, x,y, w,h, image):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = ""
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
        self.general_animation_speed = pygame.time.get_ticks()
        self.last_animation = pygame.time.get_ticks()
        self.animation_duration = randrange(300,800)
        self.count = 0
        self.last_coin_update = pygame.time.get_ticks()
        self.coin_frame = -1

    def update(self):
        if self.name != "coin":
            self.up_down_move()
        if self.name == "coin":
            self.coin_animation()

    def coin_animation(self):
        if self.coin_frame == len(all_coin_images):
            self.coin_frame = -1
        now = pygame.time.get_ticks()
        if now - self.last_coin_update > 200:
            self.image = all_coin_images[self.coin_frame]
            self.image = pygame.transform.scale(self.image,(self.w, self.h))
            self.coin_frame += 1
            self.last_coin_update = now

    def up_down_move(self):
        animation_loop = pygame.time.get_ticks()
        if animation_loop - self.general_animation_speed > 100:

            now = pygame.time.get_ticks()
            self.rect.y += 1
            self.count += 1
            if now - self.last_animation > self.animation_duration:
                self.last_animation = now
                self.rect.y -= self.count
                self.count = 0
            self.general_animation_speed = animation_loop

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 24
        self.height = 40
        self.image = player_idle_images[0]
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = SCREEN_WIDTH/2,100
        self.change_x = 0
        self.change_y = 0
        self.jump_power = 13
        self.max_speed = 6
        self.speed = self.max_speed
        self.acc = 1.9
        self.score = 0
        self.level = 1
        self.life = 3
        self.items = []
        self.last_animation = pygame.time.get_ticks()
        self.last_throw_animation = pygame.time.get_ticks()
        self.idle_animation_duration = 260
        self.move_animation_duration = self.max_speed * 5
        self.dead_animation_duration = 260
        self.throw_animation_duration = 200
        self.animation_frame = -1
        self.animation_max_frame  = 9
        self.time_used = 0
        self.star_amount = 0
        self.bird_amount = 0
        self.last_direction = self.change_x
        self.stand_last_direction = ""
        self.aim = None
        self.death_count_down = 0
        self.show_map = "off"
        self.jump_switch = 0
        self.alpha_time = pygame.time.get_ticks()
        self.alpha_duration = 2
        self.inventory = []
        self.ninja_star = 0
        self.damage_take = 3

    def stuff_tracker(self):
        pass

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.change_x = -self.speed
            self.stand_last_direction = "left"

        elif key[pygame.K_d]:
            self.change_x = self.speed
            self.stand_last_direction = "right"
        else:
            self.change_x = 0

        if self.damage_take <= 0:
            self.life -= 1
            self.damage_take = 4
        if self.change_x != 0:
            self.animate_move()
        if self.change_x == 0:
            self.animate_idle()


    def animate_throw(self):
        if self.animation_frame == 8:
            self.animation_frame = -1
        now = pygame.time.get_ticks()
        if now - self.last_throw_animation > self.throw_animation_duration:
            self.animation_frame += 1
            self.image = player_throw_images[self.animation_frame]
            if self.last_direction < 0 or self.stand_last_direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image,(self.width +8, self.height))
            self.last_throw_animation = now

    def animate_idle(self):
        if self.animation_frame == 8:
            self.animation_frame = -1
        now = pygame.time.get_ticks()
        if now - self.last_animation > self.idle_animation_duration:
            self.image = player_idle_images[self.animation_frame]
            if self.stand_last_direction == "left" :#or self.aim < self.rect.x:
                self.image = pygame.transform.flip(self.image, True, False)

            self.image = pygame.transform.scale(self.image,(self.width,self.height))
            self.last_animation = now

            self.animation_frame += 1

    def animate_move(self):
        if self.animation_frame == 8:
            self.animation_frame = -1
        now = pygame.time.get_ticks()
        if now - self.last_animation > self.move_animation_duration:
            self.image = player_moving_images[self.animation_frame]
            if self.last_direction < 0 or self.stand_last_direction == "left":
                self.image = pygame.transform.flip(self.image, True,False)

            self.image = pygame.transform.scale(self.image,(self.width +10, self.height))
            self.last_animation = now
            self.animation_frame += 1

    def animate_dead(self):
        if self.animation_frame == 8:
            self.animation_frame = -1
        now = pygame.time.get_ticks()
        if now - self.last_animation > self.dead_animation_duration:
            self.animation_frame += 1
            self.image = player_dead_images[self.animation_frame]
            if self.last_direction < 0 or self.aim < self.rect.x:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image,(self.width + 8,self.height + 5))
            self.last_animation = now
            self.death_count_down += 1

    def blink(self):
        now = pygame.time.get_ticks()
        if now - self.alpha_time > self.alpha_duration:
            self.image.set_alpha(10)
            self.alpha_time = now

#-- Class enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y, w,h, image):
        super().__init__()
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y
        self.type = ""
        self.change_x = 0
        self.change_y = 0
        self.direction = "right"
        self.max_speed = 1
        self.speed = self.max_speed
        self.direction = "right"
        self.last_animation = pygame.time.get_ticks()
        self.animation_frame = -1
        self.move_animation_duration = 200
        self.bird_last_update = pygame.time.get_ticks()
        self.bird_frame = 0
        self.bird_animation_speed = 100
        self.bird_directions = ["right", "light"]
        self.bird_direction = "right"
        self.original_y = self.rect.y
        self.last_flapping_up = pygame.time.get_ticks()
        self.last_flapping_down = pygame.time.get_ticks()

    def bird_movement(self):
        if self.bird_direction == "right":
            self.rect.x += 2
        elif self.bird_direction == "left":
            self.rect.x -= 2

    def bird_animation(self):
        if self.bird_frame == len(all_bird_images):
            self.bird_frame = 1
        now = pygame.time.get_ticks()
        if now - self.bird_last_update > self.bird_animation_speed:
            self.image = all_bird_images[self.bird_frame]
            if self.bird_direction == "left":
                self.image = pygame.transform.flip(self.image,True, False)
            self.image = pygame.transform.scale(self.image,(self.width, self.height))
            self.bird_frame += 1
            self.bird_last_update = now

    def update(self):
        if self.type == "E1":
            self.E1_movement()
        if self.type == "bird":
            self.bird_movement()
            self.bird_animation()
            if self.direction == "right" and self.rect.left > SCREEN_WIDTH:
                self.rect.center = (randrange(-200,-100), randrange(100,200))
            elif self.direction == "left" and self.rect.right < 0:
                self.rect.center = (randrange( SCREEN_WIDTH+100, SCREEN_WIDTH + 200), randrange(100,200))

    def E1_movement(self):
        if self.animation_frame == 7:
            self.animation_frame = -1
        now = pygame.time.get_ticks()
        if now - self.last_animation > self.move_animation_duration:
            self.animation_frame += 1
            self.image = all_e1_walking[self.animation_frame]
            if self.speed < 0:
                self.image = pygame.transform.flip(self.image, True,False)
            self.image = pygame.transform.scale(self.image,(self.width +10, self.height))
            self.last_animation = now

################# MAIN
# Example: move_circle_coords(10, 10 ,( 100,100))
def move_circle_coords(angle, radius, coords):
    theta = radians(angle)
    return coords[0] + radius * cos(theta), coords[1] + radius * sin(theta)

def create_on_screen_map(game_level, on_screen_map_group):
    y = 10
    for row in maps[game_level]:
        x = 30
        for tile in row:
            if tile == "1": #--
                tile = Tile(x * 5, y * 5, 5, 5,block_image_04)
                on_screen_map_group.add(tile)
            if tile == "2":
                tile = Tile(x * 5, y * 5, 5, 5,block_elevator_image)
                on_screen_map_group.add(tile)
            if tile == "f":
                tile = Tile(x * 5, y * 5, 5, 5, block_fire_place_image)
                on_screen_map_group.add(tile)
            if tile == "k":
                tile = Tile(x * 5, y * 5, 5, 5, key_image)
                on_screen_map_group.add(tile)
            if tile == "w":
                tile = Tile(x * 5, y * 5, 5, 5, block_lava_image)
                on_screen_map_group.add(tile)
            if tile == "3":
                tile = Tile(x * 5, y * 5, 5, 5, block_image_02)
                on_screen_map_group.add(tile)
            x += 1
        y += 1

def create_map(game_level, all_tiles_sprite_group):
        y = 0
        for row in maps[game_level]:
            x = 0
            for tile in row:
                if tile == "1":
                    tile = Tile(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE,block_image_04)
                    tile.name = "block_base"
                    all_tiles_sprite_group.add(tile)
                if tile == "2":
                    tile = Tile(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE +15, BLOCK_SIZE-15,block_elevator_image)
                    tile.name = "block_elevator"
                    all_tiles_sprite_group.add(tile)
                if tile == "f":
                    tile = Tile(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE,block_fire_place_image)
                    tile.name = "block_fire_place"
                    all_tiles_sprite_group.add(tile)
                if tile == "w":
                    tile = Tile(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE,block_lava_image)
                    tile.name = "block_lava"
                    all_tiles_sprite_group.add(tile)
                if tile == "3":
                    tile = Tile(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE+15, BLOCK_SIZE,block_image_02)
                    tile.name = "block_loose"
                    all_tiles_sprite_group.add(tile)
                if tile == "a":
                    tile = Tile(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE,block_safe_image)
                    tile.name = "block_safe"
                    all_tiles_sprite_group.add(tile)

                x += 1
            y += 1

def spawn_stuff(game_level, all_stuff_sprite_group, player):
        y = 0
        for row in maps[game_level]:
            x = 0
            for stuff in row:
                if stuff == "s":
                    stuff = Stuff(x * BLOCK_SIZE, y * BLOCK_SIZE, 15, 15, stuff_particle_image)
                    stuff.name = "ninja_star"
                    all_stuff_sprite_group.add(stuff)
                if stuff == "c":
                    stuff = Stuff(x * BLOCK_SIZE, y * BLOCK_SIZE, 15,15, choice(all_coin_images))
                    stuff.name = "coin"
                    all_stuff_sprite_group.add(stuff)
                #-- condition to have something in inventory before spawning the key
                if stuff == "k":
                    stuff = Stuff(x * BLOCK_SIZE, y * BLOCK_SIZE, 20,20,key_image)
                    stuff.name = "key"
                    all_stuff_sprite_group.add(stuff)
                if stuff == "l":
                    stuff = Stuff(x * BLOCK_SIZE, y * BLOCK_SIZE, 10,10,life_image)
                    stuff.name = "life"
                    all_stuff_sprite_group.add(stuff)
                if stuff == "g":
                    stuff = Stuff(x * BLOCK_SIZE, y * BLOCK_SIZE, 25,25,grenade_image)
                    stuff.name = "grenade"
                    all_stuff_sprite_group.add(stuff)
                x += 1
            y += 1

def spawn_enemies(game_level, all_enemies_group, player):
        y = 0
        for row in maps[game_level]:
            x = 0
            for enemy in row:
                if enemy == "E1":
                    name = "E1"
                    enemy = Enemy(x * BLOCK_SIZE, y * BLOCK_SIZE, 45, 60,choice(all_e1_walking))
                    enemy.rect.y += 4
                    enemy.type = name
                    all_enemies_group.add(enemy)
                if enemy == "b":
                    name = "bird"
                    enemy = Enemy(x * BLOCK_SIZE, y * BLOCK_SIZE, 35,35, all_bird_images[0])
                    enemy.type = name
                    enemy.bird_direction = choice(enemy.bird_directions)
                    all_enemies_group.add(enemy)
                x += 1
            y += 1


# Controlling in game music
music_switch = "off"
def music_control():
    # collection = ["intro.wav","intro_2.mp3"]
    global music_switch
    if music_switch == "off":
        music_switch = "on"
    else:
        music_switch = "off"
    if music_switch == "on":
        #music = choice(collection)
        mixer.music.load(path.join(snd_dir,"level_2.mp3"))
        mixer.music.set_volume(0.4)
        mixer.music.play(-1)
    else:
        mixer.music.stop()

def start_screen():
    "player.kill()"
    global score_file
    score_file = open("score.txt", "r+")
    ingame_bg_x = -200
    last_animation = pygame.time.get_ticks()
    running = True
    x = -100
    cursor_image_2 = pygame.transform.scale(cursor_image,(10,10))
    while running:
        click = False
        cursor_x, cursor_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        now = pygame.time.get_ticks()
        if now - last_animation > 50:
            x+= 40
            last_animation = now
            if x >= 100:
                x = 100
        screen.fill(pygame.Color("white"))
        screen.blit(menu_bg,(0,0))
        bt_start = create_button("start", "start_frame", x,100, 100,30, "orange", "darkgreen", "Start", cursor_x,cursor_y,click,  main)
        #-- bt_music = create_button("music", "music_frame", x,140, 100,30, "orange", "darkgreen", "Music", cursor_x,cursor_y,click,  music_control)
        bt_exit = create_button("exit", "exit_frame", x,140, 100,30, "orange", "darkgreen", "Exit", cursor_x,cursor_y,click,  exit)
        screen.blit(cursor_image_2,(cursor_x, cursor_y))
        pygame.display.flip()

def level_screen(game_level):
    if game_level == 3:
        FPS = 80
    else:
        FPS = 60
    x = 180
    y = 430
    mixer.music.load(path.join(snd_dir,"ninja_theme.ogg"))
    mixer.music.play()
    n = 0
    temp_container = pygame.sprite.Group()
    if game_level == 1:
        cursor = Stuff(x,y, 20,40, level_cursor_image)
        cursor.name == "level_cursor"
        temp_container.add(cursor)
    elif game_level == 2:
        cursor = Stuff(x,y-200, 20,40, level_cursor_image)
        cursor.name == "level_cursor"
        temp_container.add(cursor)
    elif game_level == 3:
        cursor = Stuff(x + 200,y, 20,40, level_cursor_image)
        cursor.name == "level_cursor"
        temp_container.add(cursor)
    elif game_level == 4:
        cursor = Stuff(x + 200,y-200, 20,40, level_cursor_image)
        cursor.name == "level_cursor"
        temp_container.add(cursor)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mixer.music.stop()
                    running = False
        temp_container.update()

        screen.blit(all_menu_backgrounds[game_level],(0,0))

        temp_container.draw(screen)
        n += 1
        color = (n,n,n)
        if n >= 250:
            n = 0
        score_file = open("score.txt","r")
        global last_score
        last_score = score_file.readline()
        if len(last_score) >0 :
            last_score = int(last_score)

        draw_text("Max score: ", ninja_font_menu, pygame.Color("black"), screen, 20,20)
        draw_text(str(last_score), ninja_font_menu, pygame.Color("red"), screen, 110,20)

        draw_text("Press Space to Continue", ninja_font_menu, color, screen, 220,500)
        if game_level != 4:
            draw_text("A-D to move", ninja_font_menu, pygame.Color("black"), screen, 350,50)
            draw_text("Spacebar or W to jump", ninja_font_menu, pygame.Color("black"), screen, 350,75)
            draw_text("Left and mid mouseclick to throw", ninja_font_menu, pygame.Color("black"), screen, 350,100)
            draw_text("Escape to pause", ninja_font_menu, pygame.Color("black"), screen, 350,120)
            draw_text("Avoid Fire, Guards, Bird's fethers, Lavas", ninja_font, pygame.Color("red"), screen, 350,150)
            draw_text("And try not to die...,", ninja_font, pygame.Color("red"), screen, 350,175)
        pygame.display.flip()
"""
player.kill()
"""
def end_screen():
    global ingame_bg_x
    ingame_bg_x = -200
    last_animation = pygame.time.get_ticks()
    running = True
    x = -100
    cursor_image_2 = pygame.transform.scale(cursor_image,(10,10))
    while running:
        click = False
        cursor_x,cursor_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    start_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        now = pygame.time.get_ticks()
        if now - last_animation > 50:
            x+= 40
            last_animation = now
            if x >= 100:
                x = 100
        screen.fill(pygame.Color("red"))
        screen.blit(end_screen_bg,(0,0))

        bt_restart = create_button("restart", "restart_frame", x,100, 100,30, "red", "gray", "Restart", cursor_x,cursor_y,click,  start_screen)
        #bt_music = create_button("music", "music_frame", x,140, 100,30, "red", "gray", "Music", cursor_x,cursor_y,click,  music_control)
        bt_exit = create_button("exit", "exit_frame", x,140, 100,30, "red", "gray", "Exit", cursor_x,cursor_y,click,  exit)
        screen.blit(cursor_image_2,(cursor_x, cursor_y))
        pygame.display.flip()

def display_info(player):
        x = 100
        star_y = 20
        grenade_y = 20
        y_life = 20
        draw_text("Inventory", ninja_font, pygame.Color("white"), screen, 100,10)
        draw_text("Life", ninja_font, pygame.Color("red"), screen, 180,10)
        draw_text("Score", ninja_font, pygame.Color("white"), screen, 20,10)
        draw_text(str(player.score), ninja_font, pygame.Color("yellow"), screen, 60,10)
        ninja_star_image.set_colorkey(pygame.Color("black"))

        for item in player.inventory:
            if item == "ninja_star":
                star_y += 10
                screen.blit(ninja_star_image,(100,star_y))
            if item == "grenade":
                grenade_y += 10
                screen.blit(pygame.transform.scale(grenade_image,(15,15)),(120,grenade_y))
        for life in range(player.life):
            screen.blit(life_image,(180,y_life+15))
            y_life+=15

ingame_bg_x = -200
def ingame_background(game_level, screen, player):
    global ingame_bg_x
    ongame_bg_x = -200
    bg = all_backgrounds[game_level]
    if player.change_x >0:
        ingame_bg_x -=1
    elif player.change_x <0:
        ingame_bg_x +=1
    screen.blit(bg,(ingame_bg_x,0))

def main():
    dropping_names = ["coin", "ninja_star", "life"]
    dropping_stuff_timer = pygame.time.get_ticks()
    stones_timer = pygame.time.get_ticks()
    all_sprites = pygame.sprite.Group()
    for i in range(10):
        block = Rotate_object(randrange(0,SCREEN_WIDTH),randrange(0,SCREEN_HEIGHT), randrange(80,300),randrange(80,300), choice(all_bg_blocks))
        all_sprites.add(block)
    bird_circle_radius = 10
    ingame_bg_x = -200
    is_first_time = True
    game_level = 0
    key_press_count = 1

    if is_first_time:
        is_first_time = False
        player_sprite_group = pygame.sprite.Group()
        all_tiles_sprite_group = pygame.sprite.Group()
        player_stars_group = pygame.sprite.Group()
        player = Player()
        player_sprite_group.add(player)
        game_level = player.level
        all_stuff_sprite_group = pygame.sprite.Group()
        all_particles_group = pygame.sprite.Group()
        all_enemies_group = pygame.sprite.Group()
        on_screen_map_group = pygame.sprite.Group()
        all_fire_particle_group = pygame.sprite.Group()

        #-- Just for level 4
        all_dropping = pygame.sprite.Group()
        all_stones = pygame.sprite.Group()
        # all_dropped_stuff = []

        create_map(game_level, all_tiles_sprite_group)
        spawn_stuff(game_level, all_stuff_sprite_group, player)
        create_on_screen_map(game_level, on_screen_map_group)
        spawn_enemies(game_level, all_enemies_group, player)
        level_screen(game_level)

    running = True
    pause = False
    "player.last_direction"
    # scroll_y = 0
    particle_repeat_time = pygame.time.get_ticks()
    cursor_particle_repeat_time = pygame.time.get_ticks()
    cursor_angle = 0
    pause_menu_x = -100
    last_animation_pause_menu = pygame.time.get_ticks()
    end_screen_delay = pygame.time.get_ticks()
    "throw"
    on_screen_alphadegree = 100
    mixer.music.load(path.join(snd_dir,"level_{}.ogg".format(game_level)))
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)
    while running:
        cursor_x, cursor_y = pygame.mouse.get_pos()
        menu_mouse_click = False
        #-- Vertical parallax base
        # scroll_y  += (player.rect.y - scroll_y - 400)
        clock.tick(FPS)
        x,y = pygame.mouse.get_pos()
        left_click = False
        right_click = False
        middle_click = False
        if pause is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        left_click = True
                    if event.button == 2:
                        middle_click = True
                    if event.button == 3:
                        right_click  = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                    if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        player.jump_switch = 1
                        player.rect.y += 2
                        is_stand_on_tile = pygame.sprite.spritecollide(player, all_tiles_sprite_group, False)
                        player.rect.y -= 2
                        if len(is_stand_on_tile) >0:
                            player.change_y = -player.jump_power
                        if player.rect.bottom >= SCREEN_HEIGHT:
                            player.change_y = -player.jump_power
                #-- showing the map
                    if event.key == pygame.K_i:
                        #player.stuff_tracker()
                        display_info(player)

                    if event.key == pygame.K_m:
                        if player.show_map == "on":
                            player.show_map = "off"
                        elif player.show_map == "off":
                            player.show_map = "on"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        player.jump_switch = 0


            screen.fill(pygame.Color("#1f3a66"))
            #-- Update and logic
            #-- ################################################################################################## LEVEL 4
            place = randrange(player.rect.left -300, player.rect.right + 300)
            stone_speed = randrange(6,8)
            if game_level == 4:
                drop = ""
                #- all_bg_blocks
                if len(all_stones) < 3:
                    stone = Drop(place, -50, BLOCK_SIZE,BLOCK_SIZE, choice(all_bg_blocks))
                    all_stones.add(stone)

                for stone in all_stones:
                    stone.rect.y += stone_speed
                    if stone.rect.top >= SCREEN_HEIGHT:
                        stone.kill()


                for tile in all_tiles_sprite_group:
                    for stone in all_stones:
                        if stone.rect.colliderect(tile):
                            if stone.rect.bottom >= tile.rect.top:
                                stone.rect.bottom = tile.rect.top
                                stone_impact = choice(all_stones_audio)
                                stone_impact.play()
                                now_stone = pygame.time.get_ticks()
                                if now_stone - stones_timer> 10:
                                    for i in range(10):
                                        particle = Particle(stone.rect.center[0], stone.rect.y+10, randrange(4,6),randrange(4,6), choice(all_bg_blocks), randrange(-5,5),randrange(-3,3), randrange(600,800), randrange(500,700))
                                        particle.gravity_switch = True
                                        particle.name = "stuff_particle"
                                        all_particles_group.add(particle)
                                    stone.kill()
                                    stones_timer = now_stone

                for stone in all_stones:
                    if player.change_x >0 and player.rect.x >= SCREEN_WIDTH/2 + 24:
                        player.rect.x = SCREEN_WIDTH/2 + 24
                        stone.rect.x -= (player.speed/2)
                    if player.change_x <0 and player.rect.x <= SCREEN_WIDTH/2 - 48:
                        player.rect.x = SCREEN_WIDTH/2 - 48
                        stone.rect.x += (player.speed/2)

                    if player.rect.colliderect(stone):
                        if stone.rect.bottom >= player.rect.top:
                            for i in range(10):
                                particle = Particle(stone.rect.center[0], stone.rect.y+10, randrange(4,6),randrange(4,6), choice(all_bg_blocks), randrange(-5,5),randrange(-3,3), randrange(600,800), randrange(500,700))
                                particle.gravity_switch = True
                                particle.name = "stuff_particle"
                                all_particles_group.add(particle)
                            stone.kill()
                            player.damage_take -= 1
                            hurt_sound = choice(all_player_hurt_sounds)
                            hurt_sound.play()


                if len(all_enemies_group) < 3:
                    bird = Enemy(randrange(-100, SCREEN_WIDTH), randrange(-100, 100),35,35, all_bird_images[0])
                    bird.type = "bird"

                    bird.bird_direction = choice(bird.bird_directions)
                    all_enemies_group.add(bird)

                if len(all_dropping) <10:
                    name = choice(dropping_names)
                    if name == "coin":
                        drop = Drop(place, -50, 15,15, all_coin_images[0])
                        drop.name = name
                    elif name == "ninja_star":
                        available_star = [i for i in player.inventory if i == "ninja_star"]
                        if len(available_star)<2:
                            drop = Drop(place, -50, 15,15, stuff_particle_image)
                            drop.name = name
                    if player.life <2:
                        if name == "life":
                            drop = Drop(place, -50, 15,15, life_image)
                            drop.name = name

                    all_dropping.add(drop)
                    # all_dropped_stuff.append(coin)
                for drop in all_dropping:
                    if drop.rect.colliderect(player):
                        if drop.name == "coin":
                            coin_pickup_sound_1.play()
                            player.score += 1
                            for i in range(5):
                                particle = Particle(drop.rect.center[0], drop.rect.y-10, randrange(8,14),randrange(8,14), choice(all_coin_images), randrange(-5,5),randrange(-3,3), randrange(600,800), randrange(500,700))
                                particle.gravity_switch = True
                                particle.name = "stuff_particle"
                                all_particles_group.add(particle)
                            drop.kill()

                        elif drop.name == "ninja_star":
                            star_pickup_sound.play()
                            player.inventory.append("ninja_star")
                            for i in range(2):
                                particle = Particle(drop.rect.center[0], drop.rect.y-10, randrange(8,14),randrange(8,14), stuff_particle_image, randrange(-5,5),randrange(-3,3), randrange(600,800), randrange(500,700))
                                particle.gravity_switch = True
                                particle.name = "stuff_particle"
                                all_particles_group.add(particle)
                            drop.kill()

                        elif drop.name == "life":
                            life_pickup_sound.play()
                            player.life += 1
                            for i in range(5):
                                particle = Particle(drop.rect.center[0], drop.rect.y-10, randrange(8,14),randrange(8,14), life_image, randrange(-5,5),randrange(-3,3), randrange(600,800), randrange(500,700))
                                particle.gravity_switch = True
                                particle.name = "stuff_particle"
                                all_particles_group.add(particle)
                            drop.kill()

                for drop in all_dropping:
                    drop.rect.y += randrange(4,5)
                    if drop.rect.top > SCREEN_HEIGHT:
                        drop.kill()

                for drop in all_dropping:
                    for tile in all_tiles_sprite_group:
                        if drop.rect.colliderect(tile):
                            if drop.rect.bottom >= tile.rect.top:
                                drop.rect.bottom = tile.rect.top
                                if drop.name == "coin":
                                    for i in range(2):
                                        particle = Particle(drop.rect.center[0], drop.rect.y+5, randrange(1,2),randrange(1,2), gold_particle_image, randrange(-5,5),randrange(-3,3), randrange(50,100), randrange(50,100))
                                        particle.gravity_switch = True
                                        particle.name = "stuff_particle"
                                        all_particles_group.add(particle)


                    now = pygame.time.get_ticks()
                    if now - dropping_stuff_timer > 1000:
                        drop.kill()
                        dropping_stuff_timer = now

                for drop in all_dropping:
                    if player.change_x >0 and player.rect.x >= SCREEN_WIDTH/2 + 24:
                        player.rect.x = SCREEN_WIDTH/2 + 24
                        drop.rect.x -= (player.speed/2)
                    if player.change_x <0 and player.rect.x <= SCREEN_WIDTH/2 - 48:
                        player.rect.x = SCREEN_WIDTH/2 - 48
                        drop.rect.x += (player.speed/2)

            #-- Between stars and tiles
            all_tiles_sprite_group.update()
            for tile in all_tiles_sprite_group:
                for star in player_stars_group:
                    if star.rect.colliderect(tile):
                        if star.name == "grenade":
                            for i in range(10):
                                particle = Particle(star.rect.center[0], star.rect.y-10, randrange(8,14),randrange(8,14), stuff_particle_image, randrange(-5,5),randrange(-3,3), randrange(200,300), randrange(100,200))
                                particle.name = "stuff_particle"
                                all_particles_group.add(particle)
                            grenade_tile_sound.play()
                        elif star.name == "ninja_star":
                            for i in range(5):
                                particle = Particle(star.rect.center[0], star.rect.y-10, randrange(4,8),randrange(4,8), stuff_particle_image, randrange(-5,5),randrange(-3,3), randrange(200,300), randrange(100,200))
                                particle.name = "stuff_particle"
                                all_particles_group.add(particle)
                            star_to_tile_sound.play()
                        star.kill()
            #-- fire particle updates and logics
            all_fire_particle_group.update()
            #-- mechanic between player and fire particle
            for fire in all_fire_particle_group:
                if player.change_x >0 and player.rect.x >= SCREEN_WIDTH/2 + 24:
                    player.rect.x = SCREEN_WIDTH/2 + 24
                    fire.rect.x -= (player.speed/2)
                if player.change_x <0 and player.rect.x <= SCREEN_WIDTH/2 - 48:
                    player.rect.x = SCREEN_WIDTH/2 - 48
                    fire.rect.x += (player.speed/2)
                # fire.rect.y -= scroll_y

            #-- adding some mechanic interaction between tiles
            for tile in all_tiles_sprite_group:
                if tile.name == "block_elevator":
                    if tile.rect.colliderect(tile):
                #-- adding extra mechaninc between player and elevator block
                        if tile.rect.colliderect(player):
                            if player.rect.top == tile.rect.bottom:
                                player.rect.bottom = tile.rect.top
                if tile.name == "block_fire_place":
                    for fire in range(1):
                                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                        fire = Fire(randrange(tile.rect.x, tile.rect.x+30),tile.rect.top+5, randrange(6,15), randrange(8,20), light_particle_image, randrange(-3,3), randrange(-10,-5), randrange(400,600), randrange(200,300))
                        fire_glow = Fire(randrange(tile.rect.x, tile.rect.x+30),tile.rect.top, randrange(6,15), randrange(8,20), light_particle_image, randrange(-3,3), randrange(-10,-5), randrange(400,600), randrange(200,300))
                        # particle.gravity_switch = True
                        #particle.image.set_alpha(particle.alpha_degree)
                        #particle.alpha_degree_switch = True
                        all_fire_particle_group.add(fire)
                        # particle_glow.gravity_switch = True
                        all_fire_particle_group.add(fire_glow)

                if tile.name == "block_lava":
                    for water in range(1):
                        #x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                        lava_1 = Fire(randrange(tile.rect.center[0]-10, tile.rect.center[0]+10),tile.rect.bottom, randrange(4,10), randrange(6,16), lava_image_1, randrange(-3,3), randrange(0,1), randrange(1000,1500), randrange(700,1000))

                        lava_2 = Fire(randrange(tile.rect.center[0]-10, tile.rect.center[0]+10),tile.rect.bottom, randrange(4,10), randrange(6,16), lava_image_2, randrange(-3,3), randrange(0,1), randrange(1000,1500), randrange(700,1000))
                        lava_1.gravity_switch = True
                        lava_2.gravity_switch = True
                        # particle.image.set_alpha(particle.alpha_degree)
                        # particle.alpha_degree_dwitch = True
                        lava_1.name = "lava"
                        lava_2.name = "lava"
                        all_fire_particle_group.add(lava_1)
                        all_fire_particle_group.add(lava_2)

            #-- Player logics and updates
            if middle_click:
                start_x = player.rect.center[0]
                start_y = player.rect.center[1]
                available_grenade = [i for i in player.inventory if i == "grenade"]
                if len (available_grenade) > 0:
                    grenade = Star(start_x, start_y)
                    grenade.image = (pygame.transform.scale(grenade_image,(10,10)))
                    grenade.name = "grenade"
                    grenade.speed = 5
                    player.inventory.remove("grenade")
                    player.animate_throw()
                    grenade_throw_sound.play()
                    if player.change_x >= 0:
                        grenade.direction = "right"
                    if player.change_x < 0 or player.stand_last_direction == "left":
                        grenade.direction = "left"
                    player_stars_group.add(grenade)

                    for enemy in all_enemies_group:
                        if enemy.rect.colliderect(grenade):
                            for i in range(5):
                                explosive_particle = Particle(enemy.rect.center[0], enemy.rect.center[1] , randrange(5,10),randrange(5,10), red_particle_image,randrange(-1,1), randrange(-1,1), randrange(300,600), randrange(300,600))
                                explosive_particle.name = "explosive_particle"
                                explosive_particle.gravity_switch = False
                                all_particles_group.add(explosive_particle)
                                enemy.kill()

            if left_click:
                start_x = player.rect.center[0]
                start_y = player.rect.center[1]

                available_star = [i for i in player.inventory if i == "ninja_star"]
                if len(available_star) > 0:
                    player.animate_throw()
                    player_trow_star.play()
                    star = Star(start_x, start_y)
                    star.name = "ninja_star"
                    if player.change_x >= 0:
                        star.direction = "right"
                    if player.change_x < 0  or player.stand_last_direction == "left":
                        star.direction = "left"
                    print(star.direction)
                    player_stars_group.add(star)
                    for particle in range(5):
                        #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                        red_particle = Particle(player.rect.center[0], player.rect.center[1] , randrange(1,2),randrange(1,2), red_particle_image,randrange(-3,1), randrange(-1,3), randrange(100,150), randrange(50,100))
                        red_particle.name = "red_particle"
                        red_particle.gravity_switch = True
                        all_particles_group.add(red_particle)
                    player.inventory.remove("ninja_star")
                else:
                    print("Player have no Ninja_star")
            #-- player vs fire
            for fire in all_fire_particle_group:
                if player.rect.colliderect(fire):
                    player.blink()
                    if player.last_direction >0 or player.stand_last_direction == "right":
                        player.change_x = 0
                        player.rect.x -=100
                        player.rect.y -=100
                    elif player.last_direction <0 or player.stand_last_direction == "left":
                        player.change_x = 0
                        player.rect.x += 100
                        player.rect.y -=100
                    player.blink()
                    sound = choice(all_player_hurt_sounds)
                    sound.play()
                    player.damage_take -= 1
                    #player.life -= 1
                        #player.life -= 1
            #-- player throwing star
            """
            throwing is in keybinding K_SPACE
            """
            #-- Between player and enemies
            for enemy in all_enemies_group:
                if enemy.type == "E1":
                    if player.rect.colliderect(enemy):
                        if player.change_y >1 and player.rect.bottom >= enemy.rect.top:
                            player.rect.y -= 50
                            for particle in range(3):
                                #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                                particle = Particle(enemy.rect.center[0],enemy.rect.center[1], randrange(3,8), randrange(3,8), red_particle_image,randrange(-3,3), randrange(-3,3), randrange(300,500), randrange(300,700))
                                particle.name == "red_particle"
                                particle.gravity_switch = True
                                all_particles_group.add(particle)
                            enemy.kill()
                            player.score += 5
                            sound = choice(e1_all_death_sounds)
                            sound.play()
                        elif player.change_y <=1:
                            player.rect.x -= 30
                            sound = choice(all_player_hurt_sounds)
                            sound.play()
                            player.blink()
                            player.damage_take -= 1
                            #player.life -= 1

            #-- if player dies
            if player.life <= 0:
                sound = choice(all_player_hurt_sounds)
                sound.play()

                if int(player.score) > int(last_score):
                    score_file.write(str(player.score))
                else:
                    score_file.write(str(player.score))

                ingame_bg_x = -200
                player.kill()
                #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                red_particle = Particle(randrange(player.rect.x -5, player.rect.x +5), player.rect.center[1] , randrange(2,4),randrange(2,4), red_particle_image,randrange(-1,2), randrange(-1,2), randrange(100,400), randrange(200,400))
                red_particle.gravity_switch = True
                now = pygame.time.get_ticks()
                if now - end_screen_delay > 2500:
                    running = False
                    end_screen()
            #-- horizontal parallex effect
            #-- between player and enemies
            for enemy in all_enemies_group:
                if player.change_x >0 and player.rect.x >= SCREEN_WIDTH/2 + 24:
                    player.rect.x = SCREEN_WIDTH/2 + 24
                    enemy.rect.x -= (player.speed/2)
                if player.change_x <0 and player.rect.x <= SCREEN_WIDTH/2 - 48:
                    player.rect.x = SCREEN_WIDTH/2 - 48
                    enemy.rect.x += (player.speed/2)
                #-- vertical parallax, fixes the positions between player and enemies
                # enemy.rect.y -= scroll_y
            #-- between player and tiles
            for tile in all_tiles_sprite_group:
                if player.change_x >0 and player.rect.x >= SCREEN_WIDTH/2 + 24:
                    player.rect.x = SCREEN_WIDTH/2 + 24
                    tile.rect.x -= (player.speed/2)
                    # bg_x -= 0.01
                if player.change_x <0 and player.rect.x <= SCREEN_WIDTH/2 - 48:
                    player.rect.x = SCREEN_WIDTH/2 - 48
                    tile.rect.x += (player.speed/2)
                    # bg_x += 0.01
            player_sprite_group.update()
            #-- player key controller
            #player.aim = x
            player.last_direction = player.change_x
            #-- player mouse controllers

            #-- adding particle effect on player movement
            #-- checking if player is on top of any tile
            if player.change_y == 0:
                now = pygame.time.get_ticks()
                if now - particle_repeat_time > 100:
                    if player.change_x > 0:
                        for particle in range(3):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(randrange(player.rect.x + 5, player.rect.x + 20),randrange(player.rect.bottom-10, player.rect.bottom+10), randrange(3,8), randrange(3,8), running_particle_image,randrange(-3,1), randrange(-1,3), randrange(50,100), randrange(50,100))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)
                    elif player.change_x < 0:
                        for particle in range(3):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(randrange(player.rect.x + 5, player.rect.x + 20),randrange(player.rect.bottom-10, player.rect.bottom+10), randrange(3,8), randrange(3,8), running_particle_image,randrange(0,3), randrange(-3,1), randrange(50,100), randrange(50,100))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)
                    particle_repeat_time = now
                    if player.change_x != 0:
                        player_walking_sound.play()
            player.rect.x += player.change_x

            #-- Horizontal collision with tiles
            horizontal_hit = pygame.sprite.spritecollide(player, all_tiles_sprite_group, False)
            for tile in horizontal_hit:
                if player.change_x >0:
                    player.rect.right = tile.rect.left
                    if player.jump_switch == 0:
                        player.change_y = 0
                    player.change_x = 0
                if player.change_x <0:
                    player.rect.left = tile.rect.right
                    if player.jump_switch == 0:
                        player.change_y = 0
                    player.change_x = 0
            #-- Gravity and collsions
            # -- Parallax effect
            # for tile in all_tiles_sprite_group:
            #     # tile.rect.y -= scroll_y
            # for player in player_sprite_group:
                # player.rect.y -= scroll_y
            player.rect.y += player.change_y
            if player.change_y >= 10:
                player.change_y = 10
            if player.change_y == 0:
                player.change_y = 1
            else:
                player.change_y += .99
            if player.rect.bottom >= SCREEN_HEIGHT:
                player.change_y = 0
                player.rect.bottom = SCREEN_HEIGHT

            #-- getting mask for certain tiles
            for tile in all_tiles_sprite_group:
                tile.mask = pygame.mask.from_surface(tile.image)

            vertical_hit = pygame.sprite.spritecollide(player, all_tiles_sprite_group, False)
            for tile in vertical_hit:
                if player.change_y >0:
                    player.rect.bottom = tile.rect.top
                    player.change_y = 0
                if player.change_y <0:
                    if player.rect.top <= tile.rect.bottom:
                        player.change_y = 0
                        player.rect.y += 10
                if tile.name == "block_loose":
                    tile.rect.y += 1.5
            #-- Particles update
            player_stars_group.update()
            for item in player_stars_group:
                d_y = y
                d_x = x
                x_diff = d_x - start_x
                y_diff = d_y - start_y
                angle = math.atan2(y_diff, x_diff)
                move = [0,0]
                move[0] = math.cos(angle) * item.speed
                move[1] = math.sin(angle) * item.speed
                if player.last_direction > 0 or player.stand_last_direction == "right":
                    item.rect.x += move[0]
                    item.rect.y += move[1]
                elif player.last_direction < 0 or player.stand_last_direction == "left":
                    item.rect.x += move[0]
                    item.rect.y += move[1]
            #-- Enemies Logics and Updates
            #-- enemies vs player throwing stuff
            for enemy in all_enemies_group:
                for star in player_stars_group:
                    if star.rect.colliderect(enemy):
                        if enemy.type == "E1":
                            player.score += 5
                        if enemy.type == "bird":
                            bird_death_sound.play()
                            player.score += 10
                        for particle in range(5):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(enemy.rect.center[0],enemy.rect.center[1], randrange(3,8), randrange(3,8), red_particle_image,randrange(-6,6), randrange(-6,6), randrange(500,1000), randrange(500,1000))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)
                        sound = choice(e1_all_death_sounds)
                        sound.play()
                        enemy.kill()
                        star.kill()
            #-- player stuff update
            all_stuff_sprite_group.update()
            for stuff in all_stuff_sprite_group:
                if player.change_x >0 and player.rect.x >= SCREEN_WIDTH/2 + 24:
                    player.rect.x = SCREEN_WIDTH/2 + 24
                    stuff.rect.x -= (player.speed/2)
                    # bg_x -= 0.01
                if player.change_x <0 and player.rect.x <= SCREEN_WIDTH/2 - 48:
                    player.rect.x = SCREEN_WIDTH/2 - 48
                    stuff.rect.x += (player.speed/2)

                if player.rect.colliderect(stuff):
                    if stuff.name == "ninja_star":
                        for particle in range(3):
                            ninja_star_image.set_colorkey(pygame.Color("black"))
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(stuff.rect.center[0],stuff.rect.center[1], randrange(8,12), randrange(8,12), stuff_particle_image,randrange(-3,3), randrange(-3,3), randrange(300,500), randrange(500,1000))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)

                        star_pickup_sound.play()
                        player.inventory.append(stuff.name)

                    if stuff.name == "coin":
                        coin_pickup_sound_1.play()
                        player.score += 1
                        for particle in range(3):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(stuff.rect.center[0],stuff.rect.center[1], randrange(8,12), randrange(8,12), choice(all_coin_images),randrange(-3,3), randrange(-3,3), randrange(400,600), randrange(500,800))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)

                    if stuff.name == "life":
                        player.life += 1
                        life_pickup_sound.play()
                        for particle in range(3):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(stuff.rect.center[0],stuff.rect.center[1], randrange(8,15), randrange(8,15), life_image,randrange(-3,3), randrange(-3,3), randrange(400,600), randrange(500,800))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)

                    if stuff.name == "grenade":
                        grenade_pick_sound.play()
                        player.inventory.append("grenade")
                        for particle in range(3):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(stuff.rect.center[0],stuff.rect.center[1], randrange(12,18), randrange(12,18), grenade_image,randrange(-3,3), randrange(-3,3), randrange(400,600), randrange(500,800))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)

                    if stuff.name == "key":
                        for particle in range(3):
                            #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                            particle = Particle(stuff.rect.center[0],stuff.rect.center[1], randrange(8,15), randrange(8,15), key_image,randrange(-3,3), randrange(-3,3), randrange(400,600), randrange(500,800))
                            particle.gravity_switch = True
                            all_particles_group.add(particle)
                        key_sound.play()
                        player.level += 1
                        game_level = player.level
                        all_tiles_sprite_group = pygame.sprite.Group()
                        on_screen_map_group = pygame.sprite.Group()
                        all_enemies_group = pygame.sprite.Group()
                        all_stuff_sprite_group = pygame.sprite.Group()
                        player.rect.topleft = SCREEN_WIDTH/2,100
                        player.change_x = 0
                        level_screen(game_level)
                        create_map(game_level, all_tiles_sprite_group)
                        spawn_stuff(game_level, all_stuff_sprite_group, player)
                        create_on_screen_map(game_level, on_screen_map_group)
                        spawn_enemies(game_level, all_enemies_group, player)

                        mixer.music.load(path.join(snd_dir,"level_{}.ogg".format(game_level)))
                        mixer.music.set_volume(0.1)
                        mixer.music.play(-1)
                        ingame_bg_x = -200
                    stuff.kill()

            #-- enemies interaction with tiles
            #-- enemies_vs_tiles_collision = pygame.sprite.groupcollide(all_enemies_group, all_tiles_sprite_group, False,False
            all_enemies_group.update()
            for enemy in all_enemies_group:
                if enemy.type == "E1":
                    enemy.rect.x += enemy.speed

            for enemy in all_enemies_group:
                for tile in all_tiles_sprite_group:
                    if enemy.type == "E1":
                        if enemy.rect.colliderect(tile):
                            if enemy.rect.right >= tile.rect.left:
                                enemy.speed *= -1
                            elif enemy.rect.left <= tile.rect.right:
                                enemy.speed *= -1

            for enemy in all_enemies_group:
                if enemy.type == "bird":
                    enemy.rect.y -= 1
                    if enemy.rect.bottom <= 0:
                        enemy.rect.center = randrange(-200, SCREEN_WIDTH + 200), randrange(100, 300)
                        sound = choice(all_bird_sounds)
                        sound.play()
                        for i in range(10):
                            bird_particle = Particle(enemy.rect.center[0],enemy.rect.center[1], randrange(6,16)-1,randrange(6,16)-1, bird_particle_image,randrange(-1,2), randrange(-1,2), randrange(300,600), randrange(600,1000))
                            bird_particle.name = "bird_particle"
                            all_particles_group.add(bird_particle)
            #-- horizontal mechanic with tiles
            all_particles_group.update()
            for particle in all_particles_group:
                if particle.name == "bird_particle":
                    if particle.rect.colliderect(player):
                        player.blink()
                        player.damage_take -= 1
                        #player.life -= 1
                        particle.kill()
                        for i in range(4):
                            red_particle = Particle(player.rect.center[0],player.rect.center[1], randrange(3,8)-1,randrange(3,8)-1, red_particle_image,randrange(-1,2), randrange(-1,2), randrange(300,600), randrange(600,1000))
                            all_particles_group.add(red_particle)

                if particle.name == "explosive_particle":
                    for enemy in all_enemies_group:
                        if particle.rect.colliderect(enemy):
                            for i in range(4):
                                red_particle = Particle(enemy.rect.center[0],enemy.rect.center[1], randrange(3,8)-1,randrange(3,8)-1, red_particle_image,randrange(-1,2), randrange(-1,2), randrange(300,600), randrange(600,1000))
                                all_particles_group.add(red_particle)
                            enemy.kill()
                        if enemy.type == "bird":
                            sound = choice(all_bird_sounds)
                            sound.play()
                        if enemy.type == "E1":
                            sound = choice(e1_all_death_sounds)
                            sound.play()

            on_screen_map_group.update()
            all_sprites.update()
            # render
            all_sprites.draw(screen)
            #ingame_background(game_level, screen, player)
            all_tiles_sprite_group.draw(screen)
            all_fire_particle_group.draw(screen)
            all_enemies_group.draw(screen)
            #-- Only in level 4
            all_dropping.draw(screen)
            all_stones.draw(screen)


            player_sprite_group.draw(screen)
            all_stuff_sprite_group.draw(screen)
            player_stars_group.draw(screen)
            all_particles_group.draw(screen)

            #-- inventory display
            display_info(player)
            #-- adding some effects on rendering the on screen map
            on_screen_alphadegree
            for tile in on_screen_map_group:
                on_screen_alphadegree += 10
                if on_screen_alphadegree >= 250:
                    on_screen_alphadegree = 100
                tile.alpha_degree = on_screen_alphadegree
                tile.image.set_alpha(tile.alpha_degree)

            if player.show_map == "on":
                on_screen_map_group.draw(screen)
            #-- cursor and effects
            if player.change_x >0:
                cursor_angle += 8
            if player.stand_last_direction == "right":
                cursor_angle += 4

            if player.change_x <0:
                cursor_angle -= 8
            if player.stand_last_direction == "left":
                cursor_angle -= 4

            coords = move_circle_coords(cursor_angle, 10, (player.rect.center[0],player.rect.center[1] -30))
            coords_cursor = move_circle_coords(cursor_angle, 5, (cursor_x,cursor_y))
            screen.blit(health_1_image,(coords))
            screen.blit(cursor_image,(player.rect.center[0],player.rect.center[1] -30))
            # Cursor particle effect
            cursor_now = pygame.time.get_ticks()
            if cursor_now - cursor_particle_repeat_time > 200:
                for particle in range(3):
                    #(x_pos,y_pos, random_width,random_height, particle_image, x_direction,y_direction(can be random), randomrange_existence_duration, movem_time_distance_randomrange)
                    particle = Particle(player.rect.center[0],player.rect.center[1] -30, randrange(1,5), randrange(1,5), cursor_image,randrange(-3,3), randrange(-3,3), randrange(200,300), randrange(150,250))
                    all_particles_group.add(particle)
                cursor_particle_repeat_time = cursor_now

            screen.blit(cursor_image,(coords_cursor))
            screen.blit(cursor_image,(cursor_x, cursor_y))

            #-- display actual FPS
            draw_text("FPS: ", font_menu, pygame.Color("white"), screen, 250,20)
            draw_text(str(int(clock.get_fps())), font_menu, pygame.Color("white"), screen, 300,20)

            pygame.display.flip()
        #################################### PAUSE MENU
        elif pause:
            if  key_press_count >=5:
                key_press_count = 0
            cursor_x, cursor_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        key_press_count += 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu_mouse_click = True

            now = pygame.time.get_ticks()
            if now - last_animation_pause_menu > 50:
                pause_menu_x += 25
                last_animation = now
                if pause_menu_x >= 100:
                    pause_menu_x = 100

            screen.fill(pygame.Color("white"))
            screen.blit(pause_menu_bg,(0,0))

            button_resum_frame = pygame.Rect(pause_menu_x,100,107,37)
            button_resume = pygame.Rect(pause_menu_x,100, 100, 30)

            pygame.draw.rect(screen,(pygame.Color("red")), button_resum_frame)
            pygame.draw.rect(screen, (pygame.Color("orange")), button_resume)

            draw_text("Back", ninja_font_menu, pygame.Color("red"), screen, button_resume.left + 25, button_resume.center[1]-10)
            if button_resume.collidepoint((cursor_x,cursor_y)):
                pygame.draw.rect(screen,(pygame.Color("orange")), button_resum_frame)
                pygame.draw.rect(screen,(pygame.Color("red")), button_resume)
                draw_text("Back", font_menu, pygame.Color("orange"), screen, button_resume.left + 25, button_resume.center[1] - 13)
                if menu_mouse_click is True:
                    cursor_sound.play()
                    pause_menu_x = -100
                    pause = False

            if key_press_count == 2:
                pass
            #bt_music = create_button("music", "music_frame", pause_menu_x,140, 100,30, "orange", "red", "Music", cursor_x,cursor_y,menu_mouse_click,  music_control)
            bt_exit = create_button("exit", "exit_frame", pause_menu_x,180, 100,30, "orange", "red", "Exit", cursor_x,cursor_y,menu_mouse_click,  exit)
            bt_restart = create_button("restart", "restart_frame", pause_menu_x,140, 100,30, "orange", "red", "Restart", cursor_x,cursor_y,menu_mouse_click,  start_screen)

            screen.blit(cursor_image_2,(cursor_x, cursor_y))
            pygame.display.flip()

if __name__ == "__main__":
    start_screen()
