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
# ESTRUCTURA DE IMAGENES PARA CUANDO CORRE
#-------------------------------------------------------------------------------------------------------

RUN_1 = os.path.join(IMG_DIR, "Mario/MarioRun1.png")
RUN_2 = os.path.join(IMG_DIR, "Mario/MarioRun2.png")
RUN_ANCHO = 87
RUN_ALTO = 98

RUN_ORIGINAL_1 = pygame.image.load(RUN_1)
RUN_REDIMENCIONADA_1 = pygame.transform.scale(RUN_ORIGINAL_1, (RUN_ANCHO, RUN_ALTO))

RUN_ORIGINAL_2 = pygame.image.load(RUN_2)
RUN_REDIMENCIONADA_2 = pygame.transform.scale(RUN_ORIGINAL_2, (RUN_ANCHO, RUN_ALTO))
#
RUN_SHIELD_1 = os.path.join(IMG_DIR, "Mario/MarioShieldRun1.png")
RUN_SHIELD_2 = os.path.join(IMG_DIR, "Mario/MarioShieldRun2.png")
RUN_SHIELD_ANCHO = 87
RUN_SHIELD_ALTO = 98

RUN_SHIELD_ORIGINAL_1 = pygame.image.load(RUN_SHIELD_1)
RUN_SHIELD_REDIMENCIONADA_1 = pygame.transform.scale(RUN_SHIELD_ORIGINAL_1, (RUN_SHIELD_ANCHO, RUN_SHIELD_ALTO))

RUN_SHIELD_ORIGINAL_2 = pygame.image.load(RUN_SHIELD_2)
RUN_SHIELD_REDIMENCIONADA_2 = pygame.transform.scale(RUN_SHIELD_ORIGINAL_2, (RUN_SHIELD_ANCHO, RUN_SHIELD_ALTO))
#
RUN_GIGANT_1 = os.path.join(IMG_DIR, "Mario/MarioGigant1.png")
RUN_GIGANT_2 = os.path.join(IMG_DIR, "Mario/MarioGigant2.png")
RUN_GIGANT_ANCHO = 180
RUN_GIGANT_ALTO = 320

RUN_GIGANT_ORIGINAL_1 = pygame.image.load(RUN_GIGANT_1)
RUN_GIGANT_REDIMENCIONADA_1 = pygame.transform.scale(RUN_GIGANT_ORIGINAL_1, (RUN_GIGANT_ANCHO, RUN_GIGANT_ALTO))

RUN_GIGANT_ORIGINAL_2 = pygame.image.load(RUN_GIGANT_2)
RUN_GIGANT_REDIMENCIONADA_2 = pygame.transform.scale(RUN_GIGANT_ORIGINAL_2, (RUN_GIGANT_ANCHO, RUN_GIGANT_ALTO))
#
RUN_YOSHI_1 = os.path.join(IMG_DIR, "Mario/YoshiRun1.png")
RUN_YOSHI_2 = os.path.join(IMG_DIR, "Mario/YoshiRun2.png")
RUN_YOSHI_ANCHO = 87
RUN_YOSHI_ALTO = 98

RUN_YOSHI_ORIGINAL_1 = pygame.image.load(RUN_YOSHI_1)
RUN_YOSHI_REDIMENCIONADA_1 = pygame.transform.scale(RUN_YOSHI_ORIGINAL_1, (RUN_YOSHI_ANCHO, RUN_YOSHI_ALTO))

RUN_YOSHI_ORIGINAL_2 = pygame.image.load(RUN_YOSHI_2)
RUN_YOSHI_REDIMENCIONADA_2 = pygame.transform.scale(RUN_YOSHI_ORIGINAL_2, (RUN_YOSHI_ANCHO, RUN_YOSHI_ALTO))

RUNNING = [RUN_REDIMENCIONADA_1, RUN_REDIMENCIONADA_2 ]

RUNNING_SHIELD = [RUN_SHIELD_REDIMENCIONADA_1, RUN_SHIELD_REDIMENCIONADA_2 ]

RUNNING_GIGANT = [RUN_GIGANT_REDIMENCIONADA_1, RUN_GIGANT_REDIMENCIONADA_2]

#RUNNING_YOSHI = [RUN_YOSHI_REDIMENCIONADA_1, RUN_YOSHI_REDIMENCIONADA_2]

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE IMAGENES PARA CUANDO SALTA
#------------------------------------------------------------------------------------------------------

JUMP = os.path.join(IMG_DIR, "Mario/MarioJump.png")
JUMP_ANCHO = 87
JUMP_ALTO = 98
JUMP_ORIGINAL = pygame.image.load(JUMP)
JUMP_REDIMENCIONADA = pygame.transform.scale(JUMP_ORIGINAL, (JUMP_ANCHO, JUMP_ALTO))

JUMP_SHIELD = os.path.join(IMG_DIR, "Mario/MarioShieldJump.png")
JUMP_SHIELD_ANCHO = 94
JUMP_SHIELD_ALTO = 102
JUMP_SHIELD_ORIGINAL = pygame.image.load(JUMP_SHIELD)
JUMP_SHIELD_REDIMENCIONADA = pygame.transform.scale(JUMP_SHIELD_ORIGINAL, (JUMP_SHIELD_ANCHO, JUMP_SHIELD_ALTO))

JUMP_GIGANT = os.path.join(IMG_DIR, "Mario/MarioGigantJump.png")
JUMP_GIGANT_ANCHO = 180
JUMP_GIGANT_ALTO = 320
JUMP_GIGANT_ORIGINAL = pygame.image.load(JUMP_GIGANT)
JUMP_GIGANT_REDIMENCIONADA = pygame.transform.scale(JUMP_GIGANT_ORIGINAL, (JUMP_GIGANT_ANCHO, JUMP_GIGANT_ALTO))

JUMP_YOSHI = os.path.join(IMG_DIR, "Mario/MarioYoshiJump.png")
JUMP_YOSHI_ANCHO = 116
JUMP_YOSHI_ALTO = 60
JUMP_YOSHI_ORIGINAL = pygame.image.load(JUMP_YOSHI)
JUMP_YOSHI_REDIMENCIONADA = pygame.transform.scale(JUMP_YOSHI_ORIGINAL, (JUMP_YOSHI_ANCHO, JUMP_YOSHI_ALTO))

JUMPING = JUMP_REDIMENCIONADA

JUMPING_SHIELD = JUMP_SHIELD_REDIMENCIONADA

JUMPING_GIGANT = JUMP_GIGANT_REDIMENCIONADA

JUMPING_YOSHI = JUMP_YOSHI_REDIMENCIONADA

#-------------------------------------------------------------------------------------------------------
# ESTRUTURA IMAGENES PARA CUANDO SE AGACHA
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

YOSHI_CAR_ANCHO = 116
YOSHI_CAR_ALTO = 60

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



