import pygame

from dino_runner.components.bg_clouds.clouds import Cloud
from dino_runner.utils.constants import CLOUD

class Cloud_manager:
    def __init__(self):
        self.objects = []
    def update(self, game_speed, game):
        
        if len(self.objects) == 0:
            type = 0
            
            match type:
                case 0:
                    self.objects.append(Cloud(CLOUD))
        
        for object in self.objects:
            object.update(game_speed, self.objects)
            
    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)

