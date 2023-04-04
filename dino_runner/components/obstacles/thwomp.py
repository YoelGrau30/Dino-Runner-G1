
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import THWOMP


class Thwomp(Obstacle):
    def __init__(self):
        random_img = random.randint(0,1)
        super().__init__(THWOMP[random_img], POS_Y = (random.randint(100, 300)))