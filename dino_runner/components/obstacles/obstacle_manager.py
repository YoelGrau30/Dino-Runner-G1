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
from dino_runner.components.obstacles.troppa_red import TroppaRed
from dino_runner.components.obstacles.tunnel_large import TunnelLarge
from dino_runner.components.obstacles.tunnel_small import TunnelSmall
from dino_runner.components.obstacles.turtle_fly_blue import TurtleFlyBlue
from dino_runner.components.obstacles.turtle_fly_green import TurtleFlyGreen
from dino_runner.components.obstacles.turtle_fly_red import TurtleFlyRed
from dino_runner.utils.constants_enemys import BILL_BALA, BOWSER, BUM, CHAIN_CHOMP, DRY_BOWSER, GHOST, LARGE_TUNNEL, SMALL_TUNNEL, TROPPA_RED, TURTLE, TURTLE_FLY_BLUE, TURTLE_FLY_GREEN, TURTLE_FLY_RED

class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        #if len(self.obstacles) == 0:
        if not self.obstacles: 
            TYPES = [
                TunnelSmall(SMALL_TUNNEL[0]),
                TunnelSmall(SMALL_TUNNEL[1]),
                TunnelSmall(SMALL_TUNNEL[2]),
                TunnelLarge(LARGE_TUNNEL[0]), 
                TunnelLarge(LARGE_TUNNEL[1]),
                TunnelLarge(LARGE_TUNNEL[2]),
                TurtleFlyBlue(TURTLE_FLY_BLUE[0]),
                TurtleFlyRed(TURTLE_FLY_RED[0]),
                TurtleFlyGreen(TURTLE_FLY_GREEN[0]),
                BillBala(BILL_BALA[0]),
                Bowser(BOWSER[0]),
                Bum(BUM[0]),
                DryBowser(DRY_BOWSER[0]),
                Ghost(GHOST[0]),
                TroppaRed(TROPPA_RED[0]),
                Turtle(TURTLE[0]),
                Turtle(TURTLE[1]),
                Turtle(TURTLE[3]),
                ChainChomp(CHAIN_CHOMP[0])
                ]
            self.obstacles.append(TYPES[random.randint(0, 6)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(2000)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)