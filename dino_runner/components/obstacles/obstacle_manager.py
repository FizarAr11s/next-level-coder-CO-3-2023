import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird 
from dino_runner.utils.constants import SMALL_CACTUS , LARGE_CACTUS, BIRD, DINO_DEAD

class Obstacle_manager:
    def __init__(self):
        self.obstacles = []
        self.explosion_sound = pygame.mixer.Sound("Explosion.mp3")
        self.game_over_sound = pygame.mixer.Sound("GameOver.mp3")
        
    def update(self, game_speed, game):
        
        if len(self.obstacles) == 0:
            self.explotion = False
            type = random.randint(0, 2)
            
            match type:
                case 0:
                    self.obstacles.append(Bird(BIRD))
                    self.explotion = True
                    
                case 1:
                    self.obstacles.append(Cactus(SMALL_CACTUS))

                case 2:
                    self.obstacles.append(Cactus(LARGE_CACTUS))
                    
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)       
            if game.player.dino_rect.colliderect(obstacle.rect):
                
                if not game.player.shield:
                    game.heart_manager.reduce_heart()
                
                if not game.player.shield and game.heart_manager.heart_count < 1:
                    game.player.image = DINO_DEAD
                    self.game_over_sound.play()
                    game.playing = False
                    pygame.time.delay(300)
                    
                if self.explotion == True and game.player.hammer:
                    game.heart_manager.aument_heart()
                    self.explosion_sound.play()
                    self.obstacles.remove(obstacle)
                else:
                    self.obstacles.remove(obstacle)
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


        
            
