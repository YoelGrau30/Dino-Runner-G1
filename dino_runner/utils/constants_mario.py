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

jump1 = os.path.join(IMG_DIR, "Mario/MarioRun1.png")
ancho = 87
alto = 98
jump_original1 = pygame.image.load(jump1)
imagen_jump = pygame.transform.scale(jump_original1, (ancho, alto))

JUMPING = imagen_jump

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
car1 = os.path.join(IMG_DIR, "Mario/MarioCar1.png")
car2 = os.path.join(IMG_DIR, "Mario/MarioCar2.png")
ancho = 116
alto = 60
car_original1 = pygame.image.load(car1)
car_original2 = pygame.image.load(car2)
car_redimensionada1 = pygame.transform.scale(car_original1, (ancho, alto))
car_redimensionada2 = pygame.transform.scale(car_original2, (ancho, alto))

DRIVING = [car_redimensionada1, car_redimensionada2]

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
#SMALL_TUNNEL = [
  #  pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel1.png")),
   # pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel2.png")),
   # pygame.image.load(os.path.join(IMG_DIR, "Tunnel/LargeTunnel3.png")),
#]
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