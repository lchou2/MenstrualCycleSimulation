import pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Menstrual Cycle Simulation")
window.fill((255, 255, 255))

#Not yet functional.  Hormones will function similar to projectiles in our evil clutches game.
class Hormone(pygame.sprite.Sprite):
    def __init__(self, image, rect, speed):
        self.image = image
        self.rect = rect
        self.mask = pygame.mask.from_surface(image)
        self.speed = speed

#Not yet functional.  Beginning outline for moving the follicles.  Plan to make the sliders a sub class.
class Follicle(pygame.sprite.Sprite):
    def __init__(self,image,rect):
        self.image = image
        self.rect = rect
        self.mask = pygame.mask.from_surface(image)

# Dimensions of the sprites
CL_LARGE_WIDTH = 30

