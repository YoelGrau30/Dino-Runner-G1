from pygame import Surface
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING


MARIO_JUMPING = "JUMPING"
MARIO_RUNNING = "RUNNING"
MARIO_DUCKING = "DUCKING"

class SuperMario(Sprite):
    X_POS = 32
    Y_POS = 356
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step = 0
        self.action = MARIO_RUNNING
        self.jump_velocity = self.JUMP_VEL
    
    def update(self, user_input):
        if self.action == MARIO_RUNNING:
            self.run()
        elif self.action == MARIO_JUMPING:
            self.jump()
        
        if self.action != MARIO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = MARIO_JUMPING
            else:
                self.action = MARIO_RUNNING
        
        if self.step >= 10:
            self.step = 0

    def run(self):
        #self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.image = RUNNING[self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS 
        self.rect.y = self.Y_POS
        self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print(self.rect.y, self.jump_velocity, sep=": :")
        
        if self.rect.y >= self.Y_POS:
            self.action = MARIO_RUNNING
            self.rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VEL

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))