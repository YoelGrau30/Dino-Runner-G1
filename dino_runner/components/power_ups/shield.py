
from dino_runner.components.power_ups.power_ups import PowerUp
from dino_runner.utils.constants_mario import SHIELD_TYPE
from dino_runner.utils.constants_other_mario import SHIELD_MARIO 


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD_MARIO, SHIELD_TYPE)

        