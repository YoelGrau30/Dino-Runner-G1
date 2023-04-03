import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants_other_mario import CASTLE


class CastleMario(Sprite):

    X_POS = 888
    Y_POS = 88

    def __init__(self):
        self.image = CASTLE
        self.rect = self.image.get_rect()
        self.position()


    def position(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))