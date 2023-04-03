import pygame
import os
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA OBSTACULO TUNEL LARGO
#-------------------------------------------------------------------------------------------------------
LARGE_TUNNEL_ANCHO_1 = 48
LARGE_TUNNEL_ALTO_1 = 95

LARGE_TUNNEL_ANCHO_2 = 99
LARGE_TUNNEL_ALTO_2 = 95

LARGE_TUNNEL_ANCHO_3 = 102
LARGE_TUNNEL_ALTO_3 = 95


LARGE_TUNNEL = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel1.png")), (LARGE_TUNNEL_ANCHO_1, LARGE_TUNNEL_ALTO_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel2.png")), (LARGE_TUNNEL_ANCHO_2, LARGE_TUNNEL_ALTO_2)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel3.png")), (LARGE_TUNNEL_ANCHO_3, LARGE_TUNNEL_ALTO_3)),
]
#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA OBSTACULO TUNEL PEQUEÑO
#-------------------------------------------------------------------------------------------------------
SMALL_TUNNEL_ANCHO_1 = 40
SMALL_TUNNEL_ALTO_1 = 71

SMALL_TUNNEL_ANCHO_2 = 68
SMALL_TUNNEL_ALTO_2 = 71

SMALL_TUNNEL_ANCHO_3 = 105
SMALL_TUNNEL_ALTO_3 = 71

SMALL_TUNNEL = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel1.png")), (SMALL_TUNNEL_ANCHO_1, SMALL_TUNNEL_ALTO_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel2.png")), (SMALL_TUNNEL_ANCHO_2, SMALL_TUNNEL_ALTO_2)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel3.png")), (SMALL_TUNNEL_ANCHO_3, SMALL_TUNNEL_ALTO_3)),
]


#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#################################################################################################################################################
["Enemys/BillBala1.png", "Enemys/BillBala2.png"],
["Enemys/Bowser1.png", "Enemys/Bowser2.png"],
["Enemys/Bum1.png", "Enemys/Bum2.png"],
["Enemys/ChainChomp1.png", "Enemys/ChainChomp2.png"],
["Enemys/DryBowser1.png", "Enemys/DryBowser2.png"],
["Enemys/Ghost1.png", "Enemys/Ghost2.png"],
["Enemys/Thwomp1.png", ],
["Enemys/TroppaRed1.png", "Enemys/TroppaRed2.png"],
["Enemys/TurtleBlue.png", "Enemys/TurtleRed.png", "Enemys/TurtleGreen.png"],
["Enemys/TurtleFlyBlue1.png", "Enemys/TurtleFlyBlue2.png",],
["Enemys/TurtleFlyRed1.png", "Enemys/TurtleFlyRed2.png",],
["Enemys/TurtleGreen1.png", "Enemys/TurtleGreen2.png"],


#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE ENEMIGOS
#-------------------------------------------------------------------------------------------------------
BILL_BALA_ANCHO = 60
BILL_BALA_ALTO = 70
BILL_BALA = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/BillBala1.png")), (BILL_BALA_ANCHO, BILL_BALA_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/BillBala2.png")), (BILL_BALA_ANCHO, BILL_BALA_ALTO)),
]

BOWSER_ANCHO = 60
BOWSER_ALTO = 70
BOWSER = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bowser1.png")), (BOWSER_ANCHO, BOWSER_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bowser2.png")), (BOWSER_ANCHO, BOWSER_ALTO)),
]

BUM_ANCHO = 60
BUM_ALTO = 70
BUM = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bum1.png")), (BUM_ANCHO, BUM_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Bum2.png")), (BUM_ANCHO, BUM_ALTO)),
]

CHAIN_CHOMP_ANCHO = 60
CHAIN_CHOMP_ALTO = 70
CHAIN_CHOMP = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/ChainChomp1.png")), (CHAIN_CHOMP_ANCHO, CHAIN_CHOMP_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/ChainChomp2.png")), (CHAIN_CHOMP_ANCHO, CHAIN_CHOMP_ALTO)),
]

DRY_BOWSER_ANCHO = 60
DRY_BOWSER_ALTO = 70
DRY_BOWSER = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/DryBowser1.png")), (DRY_BOWSER_ANCHO, DRY_BOWSER_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/DryBowser2.png")), (DRY_BOWSER_ANCHO, DRY_BOWSER_ALTO)),
]

GHOST_ANCHO = 60
GHOST_ALTO = 70
GHOST = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Ghost1.png")), (GHOST_ANCHO, GHOST_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Ghost2.png")), (GHOST_ANCHO, GHOST_ALTO)),
]

THWOMP_ANCHO = 60
THWOMP_ALTO = 70
THWOMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/Thwomp1.png")), (THWOMP_ANCHO, THWOMP_ALTO)),


TROPPA_RED_ANCHO = 60
TROPPA_RED_ALTO = 70
TROPPA_RED = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TroppaRed1.png")), (TROPPA_RED_ANCHO, TROPPA_RED_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TroppaRed2.png")), (TROPPA_RED_ANCHO, TROPPA_RED_ALTO)),
]
###########################################

TURTLE_ANCHO = 60
TURTLE_ALTO = 70

TURTLE = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleBlue.png")), (TURTLE_ANCHO, TURTLE_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleRed.png")), (TURTLE_ANCHO, TURTLE_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleGreen.png")), (TURTLE_ANCHO, TURTLE_ALTO)),
]
#
TURTLE_FLY_BLUE_ANCHO_1 = 60
TURTLE_FLY_BLUE_ALTO_1 = 70

TURTLE_FLY_BLUE_ANCHO_2 = 60
TURTLE_FLY_BLUE_ALTO_2 = 70

TURTLE_FLY_BLUE = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyBlue1.png")), (TURTLE_FLY_BLUE_ANCHO_1, TURTLE_FLY_BLUE_ALTO_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyBlue2.png")), (TURTLE_FLY_BLUE_ANCHO_2, TURTLE_FLY_BLUE_ALTO_2)),
]

#

TURTLE_FLY_RED_ANCHO_1 = 60
TURTLE_FLY_RED_ALTO_1 = 70

TURTLE_FLY_RED_ANCHO_2 = 60
TURTLE_FLY_RED_ALTO_2 = 70


TURTLE_FLY_RED = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyRed1.png")), (TURTLE_FLY_RED_ANCHO_1, TURTLE_FLY_RED_ALTO_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyRed2.png")), (TURTLE_FLY_RED_ANCHO_2, TURTLE_FLY_RED_ALTO_2)),
]
#

TURTLE_FLY_GREEN_ANCHO_1 = 60
TURTLE_FLY_GREEN_ALTO_1 = 70

TURTLE_FLY_GREEN_ANCHO_2 = 60
TURTLE_FLY_GREEN_ALTO_2 = 70

TURTLE_FLY_GREEN = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyGreen1.png")), (TURTLE_FLY_GREEN_ANCHO_1, TURTLE_FLY_GREEN_ALTO_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemys/TurtleFlyGreen2.png")), (TURTLE_FLY_GREEN_ANCHO_2, TURTLE_FLY_GREEN_ALTO_2)),
]






