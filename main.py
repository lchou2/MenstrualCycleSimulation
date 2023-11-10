import pygame
import random
pygame.init()

# Window dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Menstrual Cycle Simulation")
window.fill((255, 255, 255))

#Creating Main Simulation Image

backgroundimage = pygame.image.load("Background image.png")
backgroundimage_rect = backgroundimage.get_rect()

#Centuring the image
WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()
backgroundimage_x = (WINDOW_WIDTH - backgroundimage_rect.width) // 2
backgroundimage_y = (WINDOW_HEIGHT - backgroundimage_rect.height) // 2

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

    if event.type == MOUSEBUTTONDOWN:
        if follicle.collidepoint(event.pos):
            moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            follicle.move_ip(event.rel)

# Dimensions of the sprites
CL_LARGE_WIDTH = 30

def main():
    running = True
    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        window.blit(backgroundimage, (backgroundimage_x, backgroundimage_y))
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()