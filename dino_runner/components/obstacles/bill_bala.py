
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import BILL_BALA


class BillBala(Obstacle):
    def __init__(self):
        super().__init__(BILL_BALA[0], POS_Y = (random.randint(100, 340)))
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = BILL_BALA[self.step // 5]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 10:
            self.step = 0