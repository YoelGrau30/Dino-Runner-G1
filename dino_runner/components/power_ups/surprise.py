
from dino_runner.components.power_ups.power_ups import PowerUp
from dino_runner.utils.constants_mario import SURPRISE_TYPE
from dino_runner.utils.constants_other_mario import SURPRISE 


class Surprise(PowerUp):
    def __init__(self):
        super().__init__(SURPRISE, SURPRISE_TYPE)