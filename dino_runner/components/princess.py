import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants_other_mario import PRINCESS


class PrincessMario(Sprite):

    X_POS = 930
    Y_POS = 157

    def __init__(self):
        self.image = PRINCESS[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step = 0

    def update(self):
        self.image = PRINCESS[self.step // 5]
        self.step += 1
        if self.step >= 10:
            self.step = 0

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))