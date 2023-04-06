
from dino_runner.components.power_ups.power_ups import PowerUp
from dino_runner.utils.constants_mario import YOSHI_TYPE

from dino_runner.utils.constants_other_mario import YOSHI


class Yoshi(PowerUp):
    def __init__(self):
        super().__init__(YOSHI, YOSHI_TYPE)