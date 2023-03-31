import pygame
from dino_runner.utils.constants import RUNNING
from pygame.sprite import Sprite

class Mario(Sprite):
    X_POS = 10
    Y_POS = 62

    def __init__(self):
        self.image = RUNNING[0]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS
        self.step = 0

    def update(self):
        self.run()

        self.step += 1
        if self.step == 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.mario_rect.x, self.mario_rect.y))

    def run(self):
        if self.step < 5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS

    def car(self):
        pass

    def jump(self):
        pass