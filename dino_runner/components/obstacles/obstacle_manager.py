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

    def update(self, game_speed, player, on_death):
        #if len(self.obstacles) == 0:
        if not self.obstacles: 
            TYPES = [
                TunnelSmall(),          # 0
                TunnelSmall(),          # 1
                TunnelLarge(),          # 2
                TunnelLarge(),          # 3
                TurtleFlyBlue(),        # 4
                TurtleFlyBlue(),        # 5
                TurtleFlyRed(),         # 6
                TurtleFlyGreen(),       # 7
                BillBala(),             # 8
                Thwomp(),               # 9
                Bowser(),               # 10
                Bum(),                  # 11
                Bum(),                  # 12
                DryBowser(),            # 13
                Ghost(),                # 14
                TroppaRed(),            # 15
                TurTle(),               # 16
                ChainChomp(),           # 17
                Thwomp(),               # 18
                ]
            self.obstacles.append(random.choice(TYPES))


        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect):
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []