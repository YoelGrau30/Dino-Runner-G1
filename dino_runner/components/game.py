import pygame
from dino_runner.components.bander_bowser import BanderBowser
from dino_runner.components.black import Black
from dino_runner.components.castle_left import CastleLeft
from dino_runner.components.castle_rigth import CastleRight
from dino_runner.components.cloud import CloudMario
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_ups_manager import PowerUpManager
from dino_runner.components.princess import PrincessMario
from dino_runner.components.score import Score
from dino_runner.components.super_mario import SuperMario
from pygame import Surface

from dino_runner.utils.constants_mario import BG, ICON, MARIO_ANGEL, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.constants_other_mario import EXIT, GAME_OVER, MARIO_DEAD, PLAY, RAY_BLUE, RAY_PINK, SUPER_MARIO

FONT_STYLE = "freesansbold.ttf"
BLACK_COLOR = (0,0,0)
COLOR = (33, 47, 60)

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
        self.power_up_manager = PowerUpManager()
        self.score_mario = Score()
        self.death_count = 0
        self.best_score = 0
        

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def play(self):
        self.playing = True
        self.reset()

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.obstacle_manager.reset()
        self.power_up_manager.reset()
        self.score_mario.reset()
        self.game_speed = 20


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.score_mario.update(self)
        user_input = pygame.key.get_pressed()
        self.cloud.update()
        self.player.update(user_input)
        self.princess.update()
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager(self.game_speed, self.score_mario.score, self.player)


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
        self.player.draw_power_up.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.right_castle.draw(self.screen)
        self.score_mario.draw(self.screen)
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
        half_screen_width = SCREEN_WIDTH // 2  # (52, 73, 94)
        if self.death_count:
            self.screen.fill((0, 0, 255))
            self.screen.blit(RAY_BLUE,(half_screen_width - 460, half_screen_height - 300))
            self.screen.blit(RAY_PINK,(-10, -62))
            font = pygame.font.Font(FONT_STYLE, 27)
            text = font.render(f"DEAD COUNT: {self.death_count}", True, BLACK_COLOR)
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width + 86, half_screen_height + 250)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 27)
            text = font.render(f"SCORE: {self.score_mario.score}", True, BLACK_COLOR)
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width + 86, half_screen_height + 200)
            self.screen.blit(text, text_rect)

            self.screen.blit(MARIO_DEAD,(740, half_screen_height - 240))
            self.screen.blit(EXIT,(800, 350))
            self.screen.blit(PLAY,(800, 200))
            self.screen.blit(GAME_OVER,(half_screen_width - 480, half_screen_height - 200))
            
        else:
            self.screen.fill((255, 152, 0 ))
            font = pygame.font.Font(FONT_STYLE, 27)
            text = font.render("ENTER SPACE = PLAY", True, BLACK_COLOR)
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width + 86, half_screen_height + 250)
            self.screen.blit(text, text_rect)
            self.screen.blit(SUPER_MARIO,(half_screen_width - 460, half_screen_height - 240))
            self.screen.blit(PLAY,(half_screen_width - 160 , half_screen_height + 210))
            
        pygame.display.flip()
        self.menu_events()


    def on_death(self):
        self.player.dead()
        self.draw()
        self.playing = False
        self.death_count += 1
        pygame.time.delay(2000)

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.play()


