import pygame

from dino_runner.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    FONT_ARIAL,
    GAME_OVER
    )
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstacle_manager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.player_hearts.heart_manager import Heart_manager
from dino_runner.components.bg_clouds.cloud_manager import Cloud_manager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.cloud_speed = self.game_speed - 15
        self.user_input_scape = pygame.key.get_pressed()
        self.player = Dinosaur()
        self.obstacle_manager = Obstacle_manager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = Heart_manager()
        self.cloud_manager = Cloud_manager()
        
    def increase_score(self):
        self.points += 1
        if self.points % 100 == 0:
            if self.game_speed < 50:
                self.game_speed += 1
            
        self.player.check_invincibility()
        
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting_for_key = False
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.cloud_manager.update(self.cloud_speed, self)
        self.player.update(user_input)        
        self.obstacle_manager.update(self.game_speed, self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

        self.increase_score()
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #codigo RGB
        self.draw_background()
        self.cloud_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        if not self.playing:
            self.show_game_over()
            
        self.draw_score()        
        self.heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 30)
        surface = font.render(str(self.points), True, (0, 0, 0))
        rect = surface.get_rect()
        rect.x = 1000
        rect.y = 10
        self.screen.blit(surface, rect)
        
    def show_game_over(self):
        image = GAME_OVER
        rect = image.get_rect()
        rect.x = 380
        rect.y = 200
        self.screen.blit(image, rect)
        