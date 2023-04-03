import pygame
import os
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE NUBES
#-------------------------------------------------------------------------------------------------------

CLOUD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud3.png')),
]

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE IMAGENES ADICIONALES
#-------------------------------------------------------------------------------------------------------

DINOSAUR = pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Dinosaur.png"))

########################################################################################################################################

FOSIL = pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Fosil.png"))

########################################################################################################################################

CASTLE_ANCHO = 215
CASTLE_ALTO = 355

CASTLE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Castle.png")), (CASTLE_ANCHO, CASTLE_ALTO))

########################################################################################################################################

CONGRAT_ANCHO = 300
CONGRAT_ALTO = 150

CONGRATULATIONS = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Congratulations.png")), (CONGRAT_ANCHO, CONGRAT_ALTO))

########################################################################################################################################

DEAD_COUNT_ANCHO = 40
DEAD_COUNT_ALTO = 40

DEAD_COUNT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/DeadCount.png")), (DEAD_COUNT_ANCHO, DEAD_COUNT_ALTO))

########################################################################################################################################

DEREC_ANCHO = 150
DEREC_ALTO = 200

DEREC = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Derec.png")), (DEREC_ANCHO, DEREC_ALTO))

########################################################################################################################################

EXIT_ANCHO = 60
EXIT_ALTO = 60

EXIT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Exit.png")), (EXIT_ANCHO, EXIT_ALTO))

########################################################################################################################################

EXPLOTION_ANCHO = 120
EXPLOTION_ALTO = 120

EXPLOTION = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Explotion.png")), (DEREC_ANCHO, DEREC_ALTO))

########################################################################################################################################

OVER_ANCHO = 60
OVER_ALTO = 60

GAME_OVER = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/GameOver.png")), (OVER_ANCHO, OVER_ALTO))

########################################################################################################################################

GIGANT_ANCHO = 50
GIGANT_ALTO = 50

GIGANT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Gigant.png")), (GIGANT_ANCHO, GIGANT_ALTO))

########################################################################################################################################

HEART_ANCHO = 50
HEART_ALTO = 50

HEART = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Heart.png")), (HEART_ANCHO, HEART_ALTO))

########################################################################################################################################

IZQ_ANCHO = 150
IZQ_ALTO = 200

IZQ = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Izq.png")), (IZQ_ANCHO, IZQ_ALTO))

########################################################################################################################################

KEY_CASTLE_ANCHO = 50
KEY_CASTLE_ALTO = 50

KEY_CASTLE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/KeyCastle.png")), (KEY_CASTLE_ANCHO, KEY_CASTLE_ALTO))

########################################################################################################################################

LOGO_POINTS_ANCHO = 40
LOGO_POINTS_ALTO = 40

LOGO_POINTS = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/LogoPoints.png")), (LOGO_POINTS_ANCHO, LOGO_POINTS_ALTO))

########################################################################################################################################

MARIO_DEAD_ANCHO = 300
MARIO_DEAD_ALTO = 64

MARIO_DEAD = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/MarioDead.png")), (MARIO_DEAD_ANCHO, MARIO_DEAD_ALTO))

########################################################################################################################################

MARIO_LOVE_ANCHO = 300
MARIO_LOVE_ALTO = 300

MARIO_LOVE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/MarioLove.png")), (MARIO_LOVE_ANCHO, MARIO_LOVE_ALTO))

########################################################################################################################################

PLAY_ANCHO = 40
PLAY_ALTO = 40

PLAY = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Play.png")), (PLAY_ANCHO, PLAY_ALTO))

########################################################################################################################################

SHIELD_ANCHO = 50
SHIELD_ALTO = 50
SHIELD = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Shield.png")), (SHIELD_ANCHO, SHIELD_ALTO))

########################################################################################################################################

SUPER_MARIO_ANCHO = 50
SUPER_MARIO_ALTO = 50

SUPER_MARIO = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/SuperMario.png")), (SUPER_MARIO_ANCHO, SUPER_MARIO_ALTO))

########################################################################################################################################

SURPRISE_ANCHO = 50
SURPRISE_ALTO = 50

SURPRISE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Surprise.png")), (SURPRISE_ANCHO, SURPRISE_ALTO))

########################################################################################################################################

YUSHI_ANCHO = 50
YUSHI_ALTO = 50

YUSHI = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Yushi.png")), (YUSHI_ANCHO, YUSHI_ALTO))

########################################################################################################################################

