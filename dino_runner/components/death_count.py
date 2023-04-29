import pygame
from pygame.sprite import Sprite

FONT_SCORE = "freesansbold.ttf"
COLOR = (52, 73, 94)

class DeathCount(Sprite):
    def __init__(self):
        self.score = 0


    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

        if self.score == self.game.play:
            self.score == 0

    def draw(self, screen):
        font = pygame.font.Font(FONT_SCORE, 22)
        text = font.render(f"Deads: {self.death_count}", True, COLOR)
        text_rect = text.get_rect()
        text_rect.center = (300, 30)
        screen.blit(text, text_rect)