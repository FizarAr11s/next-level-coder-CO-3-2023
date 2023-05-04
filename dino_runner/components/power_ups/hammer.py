from dino_runner.components.power_ups.power_up import Powerup
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(Powerup):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)