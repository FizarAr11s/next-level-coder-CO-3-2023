import random
from dino_runner.components.bg_clouds.object import Object

class Cloud(Object):
    def __init__(self, image):
        self.type = random.randint(0,3)
        super().__init__(image, self.type)
        self.rect.y = 100