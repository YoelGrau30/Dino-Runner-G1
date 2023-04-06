
from asyncio import shield
import random

import pygame
from dino_runner.components.power_ups.power_ups import PowerUp


class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        self.when_appears = 0 


    def generate_power_ups(self, score ):
        if not self.power_ups and score == self.when_appears:
            self.when_appears += random.randint(300, 400)
            self.power_ups.append(shield())


    def update(self, game_speed, score, player):

        self.generate_power_ups(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up_start.time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.remove(power_up)
                break


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)


