import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants_other_mario import BLACK


class Black(Sprite):

    X_POS = 980
    Y_POS = 284

    def __init__(self):
        self.image = BLACK
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))