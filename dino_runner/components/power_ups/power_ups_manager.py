
from asyncio import shield
import random
from dino_runner.components.power_ups.power_ups import PowerUp


class PowerUpManager:
    def __init__(self):
        self.power_ups: list[PowerUp] = []
        self.when_appears = 0 


    def generate_power_ups(self, score ):
        if not self.power_ups and score == self.when_appears:
            self.when_appears += random.randint(300, 400)
            self.power_ups.append(shield())


    def update(self, game_speed, score):
        self.generate_power_ups(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)


