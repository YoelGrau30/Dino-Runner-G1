import pygame
from pygame.sprite import Sprite

class Score(Sprite):
    def __init__(self):
        self.score = 0


    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            self.game.game_speed += 2

    def draw(self, screen):
        font = pygame.font.Font("freesansbold.ttf", 22)
        text = font.render(f"SCORE: {self.score}, True, (0, 0, 0)")
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)