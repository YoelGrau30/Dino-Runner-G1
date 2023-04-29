import pygame
from dino_runner.utils.constants_mario import DRIVING, JUMPING, RUNNING
from pygame.sprite import Sprite

class Mario(Sprite):
    X_POS = 32
    Y_POS = 356
    JUMP_VEL = 10
    Y_POS_LIMIT = 130

    def __init__(self):
        self.image = RUNNING[0]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS
        self.step_index = 0
        self.mario_run = True
        self.mario_car = False
        self.mario_jump = False

    def process_event(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.mario_run = False
            self.mario_car = True
            self.mario_jump = False
        elif user_input[pygame.K_UP]:
            self.mario_run = False
            self.mario_car = False
            self.mario_jump = True


    def update(self, user_input):
        self.process_event(user_input)
        if self.mario_car:
            self.car()
        elif self.mario_jump:
            self.jump()
        else:
            self.run()

        self.step_index += 1
        if self.step_index == 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.mario_rect.x, self.mario_rect.y))

    def run(self):
        if self.step_index < 5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS

    def car(self):
        if self.step_index < 5:
            self.image = DRIVING[0]
        else:
            self.image = DRIVING[1]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS + 36
        self.mario_car = False

    def jump(self):
        self.image = JUMPING
        self.mario_rect.x = self.X_POS
        self.mario_rect.y -= self.JUMP_VEL
        if self.mario_rect.y <= self.Y_POS_LIMIT:
            self.JUMP_VEL *= -1
        if self.mario_rect.y > self.Y_POS:
            self.JUMP_VEL *= -1
            self.mario_rect.y = self.Y_POS
            self.mario_jump = False