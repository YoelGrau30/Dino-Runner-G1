import random
import pygame
import math
from pygame.sprite import Sprite
from dino_runner.utils.constants_other_mario import CLOUD

class CloudMario(Sprite):

    X_POS = 1000
    Y_POS = 250 
    AMPLITUDE = 145 # Altura de la onda
    PERIOD = 90     # Ciclo de cada onda

    def __init__(self):
        self.image = CLOUD[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step = 0

    def update(self):
        self.rect.x -= 5
        self.step += 1
        y_offset = self.AMPLITUDE * \
                   math.sin(2 * math.pi * self.step / self.PERIOD)
        self.rect.centery = self.Y_POS + y_offset
        self.image = CLOUD[self.step // 5 % len(CLOUD)] # hace mas lenta la sucesion de la nube
        if self.rect.right < 0:
            self.rect.left = 1000

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))





