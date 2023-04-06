
from dino_runner.components.power_ups.power_ups import PowerUp
from dino_runner.utils.constants import SHIELD
from dino_runner.utils.constants_mario import SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)