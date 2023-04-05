import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants_other_mario import BANDER_BOWSER


class BanderBowser(Sprite):

    X_POS = 1015
    Y_POS = 20

    def __init__(self):
        self.image = BANDER_BOWSER
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))