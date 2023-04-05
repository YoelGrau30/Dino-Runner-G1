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

PRINCESS_WIDTH = 70
PRINCESS_HEIGHT = 70

PRINCESS = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Princess1.png")), (PRINCESS_WIDTH, PRINCESS_HEIGHT)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Princess2.png")), (PRINCESS_WIDTH, PRINCESS_HEIGHT)),
    ]

########################################################################################################################################

CASTLE_WIDTH = 215
CASTLE_HEIGHT = 355

CASTLE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Castle.png")), (CASTLE_WIDTH, CASTLE_HEIGHT))

########################################################################################################################################

PARTS_WIDTH = 118
PARTS_LEFT = 355

CASTLE_RIGHT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/CastleRight.png")), (PARTS_WIDTH, PARTS_LEFT))
CASTLE_LEFT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/CastleLeft.png")), (PARTS_WIDTH, PARTS_LEFT))

########################################################################################################################################

BLACK_WIDTH = 90
BLACK_LEFT = 160

BLACK = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Black.png")), (BLACK_WIDTH, BLACK_LEFT))

########################################################################################################################################

BANDER_BOWSER_WIDTH = 46
BANDER_BOWSER_LEFT = 85

BANDER_BOWSER = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/BanderBowser.png")), (BANDER_BOWSER_WIDTH, BANDER_BOWSER_LEFT))

########################################################################################################################################

CONGRAT_WIDTH = 300
CONGRAT_HEIGHT = 150

CONGRATULATIONS = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Congratulations.png")), (CONGRAT_WIDTH, CONGRAT_HEIGHT))

########################################################################################################################################

DEAD_COUNT_WIDTH = 40
DEAD_COUNT_HEIGHT = 40

DEAD_COUNT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/DeadCount.png")), (DEAD_COUNT_WIDTH, DEAD_COUNT_HEIGHT))

########################################################################################################################################

DEREC_WIDTH = 150
DEREC_HEIGHT = 200

DEREC = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Derec.png")), (DEREC_WIDTH, DEREC_HEIGHT))

########################################################################################################################################

EXIT_WIDTH = 60
EXIT_HEIGHT = 60

EXIT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Exit.png")), (EXIT_WIDTH, EXIT_HEIGHT))

########################################################################################################################################

EXPLOTION_WIDTH = 120
EXPLOTION_HEIGHT = 120

EXPLOTION = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Explotion.png")), (DEREC_WIDTH, DEREC_HEIGHT))

########################################################################################################################################

OVER_WIDTH = 60
OVER_HEIGHT = 60

GAME_OVER = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/GameOver.png")), (OVER_WIDTH, OVER_HEIGHT))

########################################################################################################################################

GIGANT_WIDTH = 50
GIGANT_HEIGHT = 50

GIGANT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Gigant.png")), (GIGANT_WIDTH, GIGANT_HEIGHT))

########################################################################################################################################

HEART_WIDTH = 50
HEART_HEIGHT = 50

HEART = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Heart.png")), (HEART_WIDTH, HEART_HEIGHT))

########################################################################################################################################

IZQ_WIDTH = 150
IZQ_HEIGHT = 200

IZQ = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Izq.png")), (IZQ_WIDTH, IZQ_HEIGHT))

########################################################################################################################################

KEY_CASTLE_WIDTH = 50
KEY_CASTLE_HEIGHT = 50

KEY_CASTLE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/KeyCastle.png")), (KEY_CASTLE_WIDTH, KEY_CASTLE_HEIGHT))

########################################################################################################################################

LOGO_POINTS_WIDTH = 40
LOGO_POINTS_HEIGHT = 40

LOGO_POINTS = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/LogoPoints.png")), (LOGO_POINTS_WIDTH, LOGO_POINTS_HEIGHT))

########################################################################################################################################

MARIO_DEAD_WIDTH = 300
MARIO_DEAD_HEIGHT = 64

MARIO_DEAD = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/MarioDead.png")), (MARIO_DEAD_WIDTH, MARIO_DEAD_HEIGHT))

########################################################################################################################################

MARIO_LOVE_WIDTH = 300
MARIO_LOVE_HEIGHT = 300

MARIO_LOVE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/MarioLove.png")), (MARIO_LOVE_WIDTH, MARIO_LOVE_HEIGHT))

########################################################################################################################################

PLAY_WIDTH = 40
PLAY_HEIGHT = 40

PLAY = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Play.png")), (PLAY_WIDTH, PLAY_HEIGHT))

########################################################################################################################################

SHIELD_WIDTH = 50
SHIELD_HEIGHT = 50
SHIELD = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Shield.png")), (SHIELD_WIDTH, SHIELD_HEIGHT))

########################################################################################################################################

SUPER_MARIO_WIDTH = 50
SUPER_MARIO_HEIGHT = 50

SUPER_MARIO = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/SuperMario.png")), (SUPER_MARIO_WIDTH, SUPER_MARIO_HEIGHT))

########################################################################################################################################

SURPRISE_WIDTH = 97
SURPRISE_HEIGHT = 101

SURPRISE = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Surprise.png")), (SURPRISE_WIDTH, SURPRISE_HEIGHT))

########################################################################################################################################

YUSHI_WIDTH = 50
YUSHI_HEIGHT = 50

YUSHI = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Yushi.png")), (YUSHI_WIDTH, YUSHI_HEIGHT))

########################################################################################################################################

