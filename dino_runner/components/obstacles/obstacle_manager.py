import random
from turtle import Turtle
import pygame
from dino_runner.components import game
from dino_runner.components.obstacles.bill_bala import BillBala
from dino_runner.components.obstacles.bowser import Bowser
from dino_runner.components.obstacles.bum import Bum
from dino_runner.components.obstacles.chain_chomp import ChainChomp
from dino_runner.components.obstacles.dry_bowser import DryBowser
from dino_runner.components.obstacles.ghost import Ghost
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.thwomp import Thwomp
from dino_runner.components.obstacles.troppa_red import TroppaRed
from dino_runner.components.obstacles.tunnel_large import TunnelLarge
from dino_runner.components.obstacles.tunnel_small import TunnelSmall
from dino_runner.components.obstacles.turtle import TurTle
from dino_runner.components.obstacles.turtle_fly_blue import TurtleFlyBlue
from dino_runner.components.obstacles.turtle_fly_green import TurtleFlyGreen
from dino_runner.components.obstacles.turtle_fly_red import TurtleFlyRed

class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        #if len(self.obstacles) == 0:
        if not self.obstacles: 
            TYPES = [
    #            TunnelSmall(),          # 0
    #            TunnelLarge(),          # 3
          #      TurtleFlyBlue(),        # 6
          #      TurtleFlyRed(),         # 7
           #     TurtleFlyGreen(),       # 8
           #     BillBala(),             # 9
    #            Bowser(),               # 10
    #            Bum(),                  # 11
    #            DryBowser(),            # 12
           #     Ghost(),                # 13
            #    TroppaRed(),            # 14
                TurTle(),               # 15
                ChainChomp(),           # 16
              #  Thwomp(),               # 17
                ]
            self.obstacles.append(TYPES[random.randint(0, 1)])


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(2000)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)