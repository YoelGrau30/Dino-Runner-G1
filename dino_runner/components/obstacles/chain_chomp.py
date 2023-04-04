
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import CHAIN_CHOMP


class ChainChomp(Obstacle):
    def __init__(self):
        super().__init__(CHAIN_CHOMP[0], POS_Y = 380)
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = CHAIN_CHOMP[self.step // 5]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 10:
            self.step = 0