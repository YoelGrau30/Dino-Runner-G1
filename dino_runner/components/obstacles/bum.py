
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import BUM


class Bum(Obstacle):
    def __init__(self):
        random_img = random.randint(0,2)
        super().__init__(BUM[0], POS_Y = 359)
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = BUM[self.step // 5]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 10:
            self.step = 0