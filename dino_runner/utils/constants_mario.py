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
CLOUD_ANCHO = 97
CLOUD_ALTO = 68
CLOUD = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud.png')), (CLOUD_ANCHO, CLOUD_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud1.png')), (CLOUD_ANCHO, CLOUD_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud2.png')), (CLOUD_ANCHO, CLOUD_ALTO)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Mario_Other/Cloud3.png')), (CLOUD_ANCHO, CLOUD_ALTO))
]
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
DINOSAUR = pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Dinosaur.png"))
FOSIL = pygame.image.load(os.path.join(IMG_DIR, "Mario_Other/Fosil.png"))

