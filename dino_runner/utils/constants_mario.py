import pygame
import os

# Global Constants
TITLE = "Super Mario"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

BG = pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Base.png'))

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "LogoMario.png"))

DEFAULT_TYPE = "default"

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

run1 = os.path.join(IMG_DIR, "Mario/MarioRun1.png")
run2 = os.path.join(IMG_DIR, "Mario/MarioRun2.png")
ancho = 87
alto = 98

run_original1 = pygame.image.load(run1)
run_redimensionada1 = pygame.transform.scale(run_original1, (ancho, alto))

run_original2 = pygame.image.load(run2)
run_redimensionada2 = pygame.transform.scale(run_original2, (ancho, alto))

RUNNING = [run_redimensionada1, run_redimensionada2]

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

jump1 = os.path.join(IMG_DIR, "Mario/MarioJump.png")
ancho = 87
alto = 98
jump_original1 = pygame.image.load(jump1)
imagen_jump = pygame.transform.scale(jump_original1, (ancho, alto))

JUMPING = imagen_jump

#-------------------------------------------------------------------------------------------------------
# ESTRUTURA PARA CUANDO MARIO SE AGACHA
#-------------------------------------------------------------------------------------------------------
CAR_1 = os.path.join(IMG_DIR, "Mario/MarioCar1.png")
CAR_2 = os.path.join(IMG_DIR, "Mario/MarioCar2.png")

CAR_SHIELD_1 = os.path.join(IMG_DIR, "Mario/MarioShieldCar1.png")
CAR_SHIELD_2 = os.path.join(IMG_DIR, "Mario/MarioShieldCar2.png")

CAR_GIGANT_1 = os.path.join(IMG_DIR, "Mario/MarioCar1.png")
CAR_GIGANT_2 = os.path.join(IMG_DIR, "Mario/MarioCar2.png")

YOSHI_CAR_1 = os.path.join(IMG_DIR, "Mario/MarioYoshiCar1.png")
YOSHI_CAR_2 = os.path.join(IMG_DIR, "Mario/MarioYoshiCar2.png")

CAR_ANCHO = 116
CAR_ALTO = 60

CAR_SHIELD_ANCHO = 146
CAR_SHIELD_ALTO = 75

CAR_GIGANT_ANCHO = 180
CAR_GIGANT_ALTO = 320

YOSHI_CAR_ANCHO = 120
YOSHI_CAR_ALTO = 70

CAR_ORIGINAL_1 = pygame.image.load(CAR_1)
CAR_ORIGINAL_2 = pygame.image.load(CAR_2)

CAR_SHIELD_ORIGINAL_1 = pygame.image.load(CAR_SHIELD_1)
CAR_SHIELD_ORIGINAL_2 = pygame.image.load(CAR_SHIELD_2)

CAR_GIGANT_ORIGINAL_1 = pygame.image.load(CAR_GIGANT_1)
CAR_GIGANT_ORIGINAL_2 = pygame.image.load(CAR_GIGANT_2)

CAR_YOSHI_ORIGINAL_1 = pygame.image.load(YOSHI_CAR_1)
CAR_YOSHI_ORIGINAL_2 = pygame.image.load(YOSHI_CAR_2)

CAR_REDIMENCIONADA_1 = pygame.transform.scale(CAR_ORIGINAL_1, (CAR_ANCHO, CAR_ALTO))
CAR_REDIMENCIONADA_2 = pygame.transform.scale(CAR_ORIGINAL_2, (CAR_ANCHO, CAR_ALTO))

CAR_SHIELD_REDIMENCIONADA_1 = pygame.transform.scale(CAR_SHIELD_ORIGINAL_1, (CAR_SHIELD_ANCHO, CAR_SHIELD_ALTO))
CAR_SHIELD_REDIMENCIONADA_2 = pygame.transform.scale(CAR_SHIELD_ORIGINAL_2, (CAR_SHIELD_ANCHO, CAR_SHIELD_ALTO))

CAR_GIGANT_REDIMENCIONADA_1 = pygame.transform.scale(CAR_GIGANT_ORIGINAL_1, (CAR_GIGANT_ANCHO, CAR_GIGANT_ALTO))
CAR_GIGANT_REDIMENCIONADA_2 = pygame.transform.scale(CAR_GIGANT_ORIGINAL_2, (CAR_GIGANT_ANCHO, CAR_GIGANT_ALTO))

CAR_YOSHI_REDIMENCIONADA_1 = pygame.transform.scale(CAR_YOSHI_ORIGINAL_1, (YOSHI_CAR_ANCHO, YOSHI_CAR_ALTO))
CAR_YOSHI_REDIMENCIONADA_2 = pygame.transform.scale(CAR_YOSHI_ORIGINAL_2, (YOSHI_CAR_ANCHO, YOSHI_CAR_ALTO))

DRIVING = [CAR_REDIMENCIONADA_1, CAR_REDIMENCIONADA_2]

DRIVING_SHIELD = [CAR_SHIELD_REDIMENCIONADA_1, CAR_SHIELD_REDIMENCIONADA_2]

DRIVING_GIGANT = [CAR_GIGANT_REDIMENCIONADA_1, CAR_GIGANT_REDIMENCIONADA_2]

DRIVING_YOSHI = [CAR_YOSHI_REDIMENCIONADA_1, CAR_YOSHI_REDIMENCIONADA_2]

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
CLOUD = [
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud3.png')),
]
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
DINOSAUR = pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Dinosaur.png"))
FOSIL = pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Fosil.png"))
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
AN1 = 48
AN2 = 99
AN3 = 102

AL1 = 95
AL2 = 95
AL3 = 95

LARGE_TUNNEL = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel1.png")), (AN1, AL1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel2.png")), (AN2, AL2)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel3.png")), (AN3, AL3))
]
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
AN_1 = 40
AN_2 = 68
AN_3 = 105

AL_1 = 71
AL_2 = 71
AL_3 = 71

SMALL_TUNNEL = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel1.png")), (AN_1, AL_1)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel2.png")), (AN_2, AL_2)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Tunnel/SmallTunnel3.png")), (AN_3, AL_3)),
]
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
