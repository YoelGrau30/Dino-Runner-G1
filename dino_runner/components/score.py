import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants_other_mario import LOGO_POINTS

FONT_SCORE = "freesansbold.ttf"
COLOR = (189, 189, 189)

class Score(Sprite):
    def __init__(self):
        self.score = 0


    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        font = pygame.font.Font(FONT_SCORE, 22)
        text = font.render(f"SCORE: {self.score}", True, COLOR)
        text_rect = text.get_rect()
        text_rect.center = (512, 40)
        screen.blit(text, text_rect)
        screen.blit(LOGO_POINTS,(395, 15))

    def reset(self):
        self.score = 0