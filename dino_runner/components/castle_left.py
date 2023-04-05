import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants_other_mario import CASTLE_LEFT


class CastleLeft(Sprite):

    X_POS = 911
    Y_POS = 88

    def __init__(self):
        self.image = CASTLE_LEFT
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))