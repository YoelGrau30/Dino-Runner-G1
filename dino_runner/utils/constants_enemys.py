import pygame
import os
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA OBSTACULO TUNEL LARGO
#-------------------------------------------------------------------------------------------------------
LARGE_TUNNEL_WIDTH_1 = 48
LARGE_TUNNEL_HEIGHT_1 = 95

LARGE_TUNNEL_WIDTH_2 = 99
LARGE_TUNNEL_HEIGHT_2 = 95

LARGE_TUNNEL_WIDTH_3 = 102
LARGE_TUNNEL_HEIGHT_3 = 95


LARGE_TUNNEL = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel1.png")), (LARGE_TUNNEL_WIDTH_1, LARGE_TUNNEL_HEIGHT_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel2.png")), (LARGE_TUNNEL_WIDTH_2, LARGE_TUNNEL_HEIGHT_2)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel3.png")), (LARGE_TUNNEL_WIDTH_3, LARGE_TUNNEL_HEIGHT_3)),
]
#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA OBSTACULO TUNEL PEQUEÑO
#-------------------------------------------------------------------------------------------------------
SMALL_TUNNEL_WIDTH_1 = 40
SMALL_TUNNEL_HEIGHT_1 = 71

SMALL_TUNNEL_WIDTH_2 = 68
SMALL_TUNNEL_HEIGHT_2 = 71

SMALL_TUNNEL_WIDTH_3 = 105
SMALL_TUNNEL_HEIGHT_3 = 71

SMALL_TUNNEL = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel1.png")), (SMALL_TUNNEL_WIDTH_1, SMALL_TUNNEL_HEIGHT_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel2.png")), (SMALL_TUNNEL_WIDTH_2, SMALL_TUNNEL_HEIGHT_2)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel3.png")), (SMALL_TUNNEL_WIDTH_3, SMALL_TUNNEL_HEIGHT_3)),
]

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE ENEMIGOS
#-------------------------------------------------------------------------------------------------------
BILL_BALA_WIDTH = 60
BILL_BALA_HEIGHT = 70
BILL_BALA = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/BillBala1.png")), (BILL_BALA_WIDTH, BILL_BALA_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/BillBala2.png")), (BILL_BALA_WIDTH, BILL_BALA_HEIGHT)),
]

########################################################################################################################################

BOWSER_WIDTH = 107
BOWSER_HEIGHT = 116
BOWSER = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bowser1.png")), (BOWSER_WIDTH, BOWSER_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bowser2.png")), (BOWSER_WIDTH, BOWSER_HEIGHT)),
]

########################################################################################################################################

BUM_WIDTH = 60
BUM_HEIGHT = 70
BUM = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bum1.png")), (BUM_WIDTH, BUM_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bum2.png")), (BUM_WIDTH, BUM_HEIGHT)),
]

########################################################################################################################################

CHAIN_CHOMP_WIDTH = 96
CHAIN_CHOMP_HEIGHT = 62
CHAIN_CHOMP = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/ChainChomp1.png")), (CHAIN_CHOMP_WIDTH, CHAIN_CHOMP_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/ChainChomp2.png")), (CHAIN_CHOMP_WIDTH, CHAIN_CHOMP_HEIGHT)),
]

########################################################################################################################################

DRY_BOWSER_WIDTH = 98
DRY_BOWSER_HEIGHT = 116
DRY_BOWSER = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/DryBowser1.png")), (DRY_BOWSER_WIDTH, DRY_BOWSER_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/DryBowser2.png")), (DRY_BOWSER_WIDTH, DRY_BOWSER_HEIGHT)),
]

########################################################################################################################################

GHOST_WIDTH = 60
GHOST_HEIGHT = 70
GHOST = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Ghost1.png")), (GHOST_WIDTH, GHOST_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Ghost2.png")), (GHOST_WIDTH, GHOST_HEIGHT)),
]

########################################################################################################################################

THWOMP_WIDTH = 70
THWOMP_HEIGHT = 70
THWOMP = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Thwomp.png")), (THWOMP_WIDTH, THWOMP_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Thwomp2.png")), (THWOMP_WIDTH, THWOMP_HEIGHT)),
]

########################################################################################################################################

TROPPA_RED_WIDTH = 60
TROPPA_RED_HEIGHT = 70
TROPPA_RED = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TroppaRed1.png")), (TROPPA_RED_WIDTH, TROPPA_RED_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TroppaRed2.png")), (TROPPA_RED_WIDTH, TROPPA_RED_HEIGHT)),
]

########################################################################################################################################

TURTLE_WIDTH = 50
TURTLE_HEIGHT = 50

TURTLE = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleBlue.png")), (TURTLE_WIDTH, TURTLE_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleRed.png")), (TURTLE_WIDTH, TURTLE_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleGreen.png")), (TURTLE_WIDTH, TURTLE_HEIGHT)),
]

########################################################################################################################################

TURTLE_FLY_BLUE_WIDTH_1 = 60
TURTLE_FLY_BLUE_HEIGHT_1 = 70

TURTLE_FLY_BLUE_WIDTH_2 = 60
TURTLE_FLY_BLUE_HEIGHT_2 = 70

TURTLE_FLY_BLUE = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyBlue1.png")), (TURTLE_FLY_BLUE_WIDTH_1, TURTLE_FLY_BLUE_HEIGHT_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyBlue2.png")), (TURTLE_FLY_BLUE_WIDTH_2, TURTLE_FLY_BLUE_HEIGHT_2)),
]

########################################################################################################################################

TURTLE_FLY_RED_WIDTH_1 = 60
TURTLE_FLY_RED_HEIGHT_1 = 70

TURTLE_FLY_RED_WIDTH_2 = 60
TURTLE_FLY_RED_HEIGHT_2 = 70


TURTLE_FLY_RED = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyRed1.png")), (TURTLE_FLY_RED_WIDTH_1, TURTLE_FLY_RED_HEIGHT_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyRed2.png")), (TURTLE_FLY_RED_WIDTH_2, TURTLE_FLY_RED_HEIGHT_2)),
]

########################################################################################################################################

TURTLE_FLY_GREEN_WIDTH_1 = 60
TURTLE_FLY_GREEN_HEIGHT_1 = 70

TURTLE_FLY_GREEN_WIDTH_2 = 60
TURTLE_FLY_GREEN_HEIGHT_2 = 70

TURTLE_FLY_GREEN = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyGreen1.png")), (TURTLE_FLY_GREEN_WIDTH_1, TURTLE_FLY_GREEN_HEIGHT_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyGreen2.png")), (TURTLE_FLY_GREEN_WIDTH_2, TURTLE_FLY_GREEN_HEIGHT_2)),
]

########################################################################################################################################






