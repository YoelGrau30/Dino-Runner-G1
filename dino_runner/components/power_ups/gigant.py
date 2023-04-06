
from dino_runner.components.power_ups.power_ups import PowerUp
from dino_runner.utils.constants_mario import GIGANT_TYPE

from dino_runner.utils.constants_other_mario import GIGANT


class Gigant(PowerUp):
    def __init__(self):
        super().__init__(GIGANT, GIGANT_TYPE)