import pygame
from dino_runner.utils.constants import RUNNING
from pygame.sprite import Sprite

class Mario(Sprite):
    X_POS = 10
    Y_POS = 30

    def __init__(self):
        self.image = RUNNING[0]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.mario_rect.x, self.mario_rect.y))

    def run(self):
        pass

    def car(self):
        pass

    def jump(self):
        pass