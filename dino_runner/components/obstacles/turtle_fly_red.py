
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import TURTLE_FLY_RED


class TurtleFlyRed(Obstacle):
    def __init__(self):
        random_img = random.randint(0,2)
        super().__init__(TURTLE_FLY_RED[0], POS_Y = (random.randint(100, 340)))
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = TURTLE_FLY_RED[self.step // 5]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 10:
            self.step = 0
