
from dino_runner.components.power_ups.power_ups import PowerUp
from dino_runner.utils.constants_mario import  HEART_TYPE

from dino_runner.utils.constants_other_mario import HEART


class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)