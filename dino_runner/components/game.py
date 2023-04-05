import pygame
from dino_runner.components.castle import CastleMario
from dino_runner.components.cloud import CloudMario
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.princess import PrincessMario
#from dino_runner.components.mario import Mario
from dino_runner.components.super_mario import SuperMario
from pygame import Surface

from dino_runner.utils.constants_mario import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 16
        self.x_pos_bg = 0
        self.y_pos_bg = 442
        #self.player = Mario()
        self.cloud = CloudMario()
        self.player = SuperMario()
        self.castle = CastleMario()
        self.princess = PrincessMario()
        self.obstacle_manager = ObstacleManager()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.cloud.update()
        self.player.update(user_input)
        self.princess.update()
        self.obstacle_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((36, 113, 163))
        self.cloud.draw(self.screen)
        self.draw_background()
        self.player.draw(self.screen)
        self.castle.draw(self.screen)
        self.princess.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
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
