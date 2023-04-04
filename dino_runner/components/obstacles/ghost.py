
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import GHOST


class Ghost(Obstacle):
    def __init__(self):
        random_img = random.randint(0,2)
        super().__init__(GHOST[random_img], POS_Y = random.randint(100, 300))
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = GHOST[self.step // 5]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 10:
            self.step = 0