
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import DRY_BOWSER


class DryBowser(Obstacle):
    def __init__(self):
        super().__init__(DRY_BOWSER[0], POS_Y = 356)
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = DRY_BOWSER[self.step // 5]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 10:
            self.step = 0