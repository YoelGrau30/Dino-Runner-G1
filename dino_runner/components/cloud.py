import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants_other_mario import CLOUD

class CloudMario(Sprite):

    X_POS = 1000
    Y_POS = random.randint(120, 400)

    def __init__(self):
        self.image = CLOUD[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step = 0

    def update(self):

        self.rect.x -= 5 
        self.image = CLOUD[self.step // 5]
        self.step += 1
        if self.step >= 10:
            self.step = 0
        if self.rect.right < 0:
            self.rect.left = 1000 
            self.rect.centery = random.randint(100, 300) 

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))





