import random
from pygame import Surface
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.utils.constants_mario import DRIVING, DRIVING_GIGANT, DRIVING_SHIELD, DRIVING_YOSHI, JUMPING_GIGANT, JUMPING_SHIELD,  JUMPING_YOSHI, JUMPING, JUMPING_YOSHI, MARIO_ANGEL, RUNNING, RUNNING_GIGANT, RUNNING_SHIELD, RUNNING_YOSHI, RUNNING, RUNNING_YOSHI, SHIELD_TYPE, YOSHI_TYPE
from dino_runner.utils.message import draw_message


MARIO_IMG_JUMPING = "IMG_JUMPING"
MARIO_IMG_RUNNING = "IMG_RUNNING"
MARIO_IMG_DRIVING = "IMG_DRIVING"
IMG_RUNNING = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, YOSHI_TYPE: RUNNING_YOSHI }
IMG_DRIVING = {DEFAULT_TYPE: DRIVING, SHIELD_TYPE: DRIVING_SHIELD, YOSHI_TYPE: DRIVING_YOSHI }
IMG_JUMPING = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, YOSHI_TYPE: JUMPING_YOSHI }

TYPES_DEFAULT = [IMG_DRIVING, IMG_RUNNING, IMG_JUMPING]
IMG_SURPRISE = random.choice(TYPES_DEFAULT)



class SuperMario(Sprite):
    X_POS = 32
    Y_POS = 356 + 17
    JUMP_VEL = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        #self.image = JUMPING[]
        self.image = IMG_RUNNING[self.type][0]
        self.rect = self.image.get_rect()
        self.position()
        self.step = 0
        self.action = MARIO_IMG_RUNNING
        self.jump_velocity = self.JUMP_VEL
        self.power_up_time_up = 0


    def update(self, user_input):
        if self.action == MARIO_IMG_RUNNING:
            self.run()    
        elif self.action == MARIO_IMG_JUMPING:
            self.jump()
        elif self.action == MARIO_IMG_DRIVING:
            self.car()
    
        if self.action != MARIO_IMG_JUMPING:
            if user_input[pygame.K_UP] or user_input[pygame.K_w]:
                self.action = MARIO_IMG_JUMPING
            elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
                self.action = MARIO_IMG_DRIVING
            else:
                self.action = MARIO_IMG_RUNNING
    
        if self.step >= 10:
            self.step = 0

    def position(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def run(self):
        #self.image = IMG_RUNNING[0] if self.step < 5 else IMG_RUNNING[1]
        self.image = IMG_RUNNING[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.position()
        self.step += 1

    def jump(self):
        self.image = IMG_JUMPING[self.type]
        self.rect.y -= self.jump_velocity * 3.3
        self.jump_velocity -= 0.6
        #print(self.rect.y, self.jump_velocity, sep=": :")
        
        if self.rect.y >= self.Y_POS:
            self.action = MARIO_IMG_RUNNING
            self.rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VEL

    def car(self):
        self.image = IMG_DRIVING[self.type][self.step // 5]
        self.rect.y = self.Y_POS + 16
        self.step += 1
        self.action = MARIO_IMG_DRIVING

    def dead(self):
        self.image = MARIO_ANGEL

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + power_up.duration * 1000

    def draw_power_up(self, screen):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.type != DEFAULT_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message(f"{self.type.capitalize()} enabled for {time_to_show} seconds",
                             screen,
                             font_size=18,
                             pos_y_center= 80
                )
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0