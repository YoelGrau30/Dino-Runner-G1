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
SHIELD_TYPE = "shield"
GIGANT_TYPE = "gigant"
YOSHI_TYPE = "yoshi"
SURPRISE_TYPE = "surprise"

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE IMAGENES PARA CUANDO CORRE
#-------------------------------------------------------------------------------------------------------

RUN_1 = os.path.join(IMG_DIR, "Mario/MarioRun1.png")
RUN_2 = os.path.join(IMG_DIR, "Mario/MarioRun2.png")
RUN_WIDTH = 67
RUN_HEIGHT = 78

RUN_ORIGINAL_1 = pygame.image.load(RUN_1)
RUN_REDIMENCIONADA_1 = pygame.transform.scale(RUN_ORIGINAL_1, (RUN_WIDTH, RUN_HEIGHT))

RUN_ORIGINAL_2 = pygame.image.load(RUN_2)
RUN_REDIMENCIONADA_2 = pygame.transform.scale(RUN_ORIGINAL_2, (RUN_WIDTH, RUN_HEIGHT))
#
RUN_SHIELD_1 = os.path.join(IMG_DIR, "Mario/MarioShieldRun1.png")
RUN_SHIELD_2 = os.path.join(IMG_DIR, "Mario/MarioShieldRun2.png")
RUN_SHIELD_WIDTH = 87
RUN_SHIELD_HEIGHT = 98

RUN_SHIELD_ORIGINAL_1 = pygame.image.load(RUN_SHIELD_1)
RUN_SHIELD_REDIMENCIONADA_1 = pygame.transform.scale(RUN_SHIELD_ORIGINAL_1, (RUN_SHIELD_WIDTH, RUN_SHIELD_HEIGHT))

RUN_SHIELD_ORIGINAL_2 = pygame.image.load(RUN_SHIELD_2)
RUN_SHIELD_REDIMENCIONADA_2 = pygame.transform.scale(RUN_SHIELD_ORIGINAL_2, (RUN_SHIELD_WIDTH, RUN_SHIELD_HEIGHT))
#
RUN_GIGANT_1 = os.path.join(IMG_DIR, "Mario/MarioGigant1.png")
RUN_GIGANT_2 = os.path.join(IMG_DIR, "Mario/MarioGigant2.png")
RUN_GIGANT_WIDTH = 180
RUN_GIGANT_HEIGHT = 320

RUN_GIGANT_ORIGINAL_1 = pygame.image.load(RUN_GIGANT_1)
RUN_GIGANT_REDIMENCIONADA_1 = pygame.transform.scale(RUN_GIGANT_ORIGINAL_1, (RUN_GIGANT_WIDTH, RUN_GIGANT_HEIGHT))

RUN_GIGANT_ORIGINAL_2 = pygame.image.load(RUN_GIGANT_2)
RUN_GIGANT_REDIMENCIONADA_2 = pygame.transform.scale(RUN_GIGANT_ORIGINAL_2, (RUN_GIGANT_WIDTH, RUN_GIGANT_HEIGHT))
#
RUN_YOSHI_1 = os.path.join(IMG_DIR, "Mario/YoshiRun1.png")
RUN_YOSHI_2 = os.path.join(IMG_DIR, "Mario/YoshiRun2.png")
RUN_YOSHI_WIDTH = 87
RUN_YOSHI_HEIGHT = 98

RUN_YOSHI_ORIGINAL_1 = pygame.image.load(RUN_YOSHI_1)
RUN_YOSHI_REDIMENCIONADA_1 = pygame.transform.scale(RUN_YOSHI_ORIGINAL_1, (RUN_YOSHI_WIDTH, RUN_YOSHI_HEIGHT))

RUN_YOSHI_ORIGINAL_2 = pygame.image.load(RUN_YOSHI_2)
RUN_YOSHI_REDIMENCIONADA_2 = pygame.transform.scale(RUN_YOSHI_ORIGINAL_2, (RUN_YOSHI_WIDTH, RUN_YOSHI_HEIGHT))

RUNNING = [RUN_REDIMENCIONADA_1, RUN_REDIMENCIONADA_2 ]

RUNNING_SHIELD = [RUN_SHIELD_REDIMENCIONADA_1, RUN_SHIELD_REDIMENCIONADA_2 ]

RUNNING_GIGANT = [RUN_GIGANT_REDIMENCIONADA_1, RUN_GIGANT_REDIMENCIONADA_2]

RUNNING_YOSHI = [RUN_YOSHI_REDIMENCIONADA_1, RUN_YOSHI_REDIMENCIONADA_2]

#-------------------------------------------------------------------------------------------------------
# ESTRUCTURA DE IMAGENES PARA CUANDO SALTA
#------------------------------------------------------------------------------------------------------

JUMP = os.path.join(IMG_DIR, "Mario/MarioJump.png")
JUMP_WIDTH = 67
JUMP_HEIGHT = 78
JUMP_ORIGINAL = pygame.image.load(JUMP)
JUMP_REDIMENCIONADA = pygame.transform.scale(JUMP_ORIGINAL, (JUMP_WIDTH, JUMP_HEIGHT))

JUMP_SHIELD = os.path.join(IMG_DIR, "Mario/MarioShieldJump.png")
JUMP_SHIELD_WIDTH = 94
JUMP_SHIELD_HEIGHT = 102
JUMP_SHIELD_ORIGINAL = pygame.image.load(JUMP_SHIELD)
JUMP_SHIELD_REDIMENCIONADA = pygame.transform.scale(JUMP_SHIELD_ORIGINAL, (JUMP_SHIELD_WIDTH, JUMP_SHIELD_HEIGHT))

JUMP_GIGANT = os.path.join(IMG_DIR, "Mario/MarioGigantJump.png")
JUMP_GIGANT_WIDTH = 180
JUMP_GIGANT_HEIGHT = 320
JUMP_GIGANT_ORIGINAL = pygame.image.load(JUMP_GIGANT)
JUMP_GIGANT_REDIMENCIONADA = pygame.transform.scale(JUMP_GIGANT_ORIGINAL, (JUMP_GIGANT_WIDTH, JUMP_GIGANT_HEIGHT))

JUMP_YOSHI = os.path.join(IMG_DIR, "Mario/MarioYoshiJump.png")
JUMP_YOSHI_WIDTH = 116
JUMP_YOSHI_HEIGHT = 60
JUMP_YOSHI_ORIGINAL = pygame.image.load(JUMP_YOSHI)
JUMP_YOSHI_REDIMENCIONADA = pygame.transform.scale(JUMP_YOSHI_ORIGINAL, (JUMP_YOSHI_WIDTH, JUMP_YOSHI_HEIGHT))

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

CAR_WIDTH = 116
CAR_HEIGHT = 60

CAR_SHIELD_WIDTH = 146
CAR_SHIELD_HEIGHT = 75

CAR_GIGANT_WIDTH = 180
CAR_GIGANT_HEIGHT = 320

YOSHI_CAR_WIDTH = 116
YOSHI_CAR_HEIGHT = 60

CAR_ORIGINAL_1 = pygame.image.load(CAR_1)
CAR_ORIGINAL_2 = pygame.image.load(CAR_2)

CAR_SHIELD_ORIGINAL_1 = pygame.image.load(CAR_SHIELD_1)
CAR_SHIELD_ORIGINAL_2 = pygame.image.load(CAR_SHIELD_2)

CAR_GIGANT_ORIGINAL_1 = pygame.image.load(CAR_GIGANT_1)
CAR_GIGANT_ORIGINAL_2 = pygame.image.load(CAR_GIGANT_2)

CAR_YOSHI_ORIGINAL_1 = pygame.image.load(YOSHI_CAR_1)
CAR_YOSHI_ORIGINAL_2 = pygame.image.load(YOSHI_CAR_2)

CAR_REDIMENCIONADA_1 = pygame.transform.scale(CAR_ORIGINAL_1, (CAR_WIDTH, CAR_HEIGHT))
CAR_REDIMENCIONADA_2 = pygame.transform.scale(CAR_ORIGINAL_2, (CAR_WIDTH, CAR_HEIGHT))

CAR_SHIELD_REDIMENCIONADA_1 = pygame.transform.scale(CAR_SHIELD_ORIGINAL_1, (CAR_SHIELD_WIDTH, CAR_SHIELD_HEIGHT))
CAR_SHIELD_REDIMENCIONADA_2 = pygame.transform.scale(CAR_SHIELD_ORIGINAL_2, (CAR_SHIELD_WIDTH, CAR_SHIELD_HEIGHT))

CAR_GIGANT_REDIMENCIONADA_1 = pygame.transform.scale(CAR_GIGANT_ORIGINAL_1, (CAR_GIGANT_WIDTH, CAR_GIGANT_HEIGHT))
CAR_GIGANT_REDIMENCIONADA_2 = pygame.transform.scale(CAR_GIGANT_ORIGINAL_2, (CAR_GIGANT_WIDTH, CAR_GIGANT_HEIGHT))

CAR_YOSHI_REDIMENCIONADA_1 = pygame.transform.scale(CAR_YOSHI_ORIGINAL_1, (YOSHI_CAR_WIDTH, YOSHI_CAR_HEIGHT))
CAR_YOSHI_REDIMENCIONADA_2 = pygame.transform.scale(CAR_YOSHI_ORIGINAL_2, (YOSHI_CAR_WIDTH, YOSHI_CAR_HEIGHT))

DRIVING = [CAR_REDIMENCIONADA_1, CAR_REDIMENCIONADA_2]

DRIVING_SHIELD = [CAR_SHIELD_REDIMENCIONADA_1, CAR_SHIELD_REDIMENCIONADA_2]

DRIVING_GIGANT = [CAR_GIGANT_REDIMENCIONADA_1, CAR_GIGANT_REDIMENCIONADA_2]

DRIVING_YOSHI = [CAR_YOSHI_REDIMENCIONADA_1, CAR_YOSHI_REDIMENCIONADA_2]


########################################################################################################################################
MARIO_ANGEL_WIDTH = 84
MARIO_ANGEL__HEIGHT = 88

MARIO_ANGEL = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioAngel.png")), (MARIO_ANGEL_WIDTH, MARIO_ANGEL__HEIGHT))



