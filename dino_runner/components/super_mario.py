from pygame import Surface
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants_mario import DRIVING, DRIVING_GIGANT, DRIVING_SHIELD, JUMPING, MARIO_ANGEL, RUNNING


MARIO_JUMPING = "JUMPING"
MARIO_RUNNING = "RUNNING"
MARIO_DRIVING = "DRIVING"
MARIO_RIGHT = "RUNNING"

class SuperMario(Sprite):
    X_POS = 32
    Y_POS = 356 + 17
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.position()
        self.step = 0
        self.action = MARIO_RUNNING
        self.jump_velocity = self.JUMP_VEL
    
    def update(self, user_input):
        if self.action == MARIO_RUNNING:
            self.run()    
        elif self.action == MARIO_JUMPING:
            self.jump()
        elif self.action == MARIO_DRIVING:
            self.car()
    
        if self.action != MARIO_JUMPING:
            if user_input[pygame.K_UP] or user_input[pygame.K_w]:
                self.action = MARIO_JUMPING
            elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
                self.action = MARIO_DRIVING
            else:
                self.action = MARIO_RUNNING
    
        if self.step >= 10:
            self.step = 0

    def position(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def run(self):
        #self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.image = RUNNING[self.step // 5]
        self.rect = self.image.get_rect()
        self.position()
        self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 3.3
        self.jump_velocity -= 0.6
        #print(self.rect.y, self.jump_velocity, sep=": :")
        
        if self.rect.y >= self.Y_POS:
            self.action = MARIO_RUNNING
            self.rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VEL

    def car(self):
        self.image = DRIVING[self.step // 5]
        self.rect.y = self.Y_POS + 16
        self.step += 1
        self.action = MARIO_DRIVING

    def dead(self):
        self.image = MARIO_ANGEL

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))