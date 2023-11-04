import pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Menstrual Cycle Simulation")


class Hormone(pygame.sprite.Sprite):
    def __init__(self, image, rect, speed):
        super().__init__()
        self.image = image
        self.rect = rect
        self.mask = pygame.mask.from_surface(image)
        self.speed = speed