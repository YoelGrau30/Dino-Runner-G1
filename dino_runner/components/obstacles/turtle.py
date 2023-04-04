
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants_enemys import TURTLE


class Turtle(Obstacle):
    def __init__(self):
        random_img = random.randint(0,2)
        super().__init__(TURTLE[random_img], POS_Y = 356)