import pygame
import os

# Global Constants
TITLE = "Super Mario"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "LogoMario.png"))

#RUNNING = [
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/MarioRun1.png")),
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/MarioRun2.png")),
#]
ruta_imagen1 = os.path.join(IMG_DIR, "Dino/MarioRun1.png")
ruta_imagen2 = os.path.join(IMG_DIR, "Dino/MarioRun2.png")
ancho_deseado = 87
alto_deseado = 98

imagen_original1 = pygame.image.load(ruta_imagen1)
imagen_redimensionada1 = pygame.transform.scale(imagen_original1, (ancho_deseado, alto_deseado))

imagen_original2 = pygame.image.load(ruta_imagen2)
imagen_redimensionada2 = pygame.transform.scale(imagen_original2, (ancho_deseado, alto_deseado))

RUNNING = [imagen_redimensionada1, imagen_redimensionada2]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

#JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
jump1 = os.path.join(IMG_DIR, "Dino/MarioRun1.png")
ancho = 87
alto = 98
jump_original1 = pygame.image.load(jump1)
imagen_jump = pygame.transform.scale(jump_original1, (ancho_deseado, alto_deseado))

JUMPING = imagen_jump

JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

car1 = os.path.join(IMG_DIR, "Dino/MarioCar1.png")
car2 = os.path.join(IMG_DIR, "Dino/MarioCar2.png")
ancho_deseado = 116
alto_deseado = 60
car_original1 = pygame.image.load(car1)
car_original2 = pygame.image.load(car2)
car_redimensionada1 = pygame.transform.scale(car_original1, (ancho_deseado, alto_deseado))
car_redimensionada2 = pygame.transform.scale(car_original2, (ancho_deseado, alto_deseado))

DUCKING = [car_redimensionada1, car_redimensionada2]
#DUCKING = [
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    #pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
#]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

#BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Base.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
