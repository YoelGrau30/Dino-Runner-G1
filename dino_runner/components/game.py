import pygame
from dino_runner.components.bander_bowser import BanderBowser
from dino_runner.components.black import Black
from dino_runner.components.castle_left import CastleLeft
from dino_runner.components.castle_rigth import CastleRight
from dino_runner.components.cloud import CloudMario
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.princess import PrincessMario
from dino_runner.components.super_mario import SuperMario
from pygame import Surface

from dino_runner.utils.constants_mario import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.constants_other_mario import SUPER_MARIO


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 16
        self.x_pos_bg = 0
        self.y_pos_bg = 442
        self.cloud = CloudMario()
        self.player = SuperMario()
        self.right_castle = CastleRight()
        self.left_castle = CastleLeft()
        self.black = Black()
        self.bander_bowser = BanderBowser()
        self.princess = PrincessMario()
        self.obstacle_manager = ObstacleManager()
        self.score = 0
        self.death_count = 0
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def play(self):
        self.playing = True
        self.obstacle_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.cloud.update()
        self.player.update(user_input)
        self.princess.update()
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((36, 113, 163))
        self.cloud.draw(self.screen)
        self.draw_background()
        self.black.draw(self.screen)
        self.left_castle.draw(self.screen)
        self.bander_bowser.draw(self.screen)
        self.player.draw(self.screen)
        self.princess.draw(self.screen)
        self.obstacle_manager.draw(self.screen, self.on_death)
        self.right_castle.draw(self.screen)
        self.score.draw(self.screen)
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

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.fill((243, 156, 18))
        if self.death_count:
            pass
        else:
            font = pygame.font.Font("freesansbold.ttf", 30)
            text = font.render("PRESS START", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
            self.screen.blit(SUPER_MARIO,(half_screen_width - 45, 
                                      half_screen_height - 140))
            
        pygame.display.flip()
        self.menu_events()


    def on_death(self):
        pygame.time.delay(2000)
        self.playing = False
        self.death_count += 1


    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.play()