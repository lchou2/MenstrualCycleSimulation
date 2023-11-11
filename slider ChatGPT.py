import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Slider Constants
SLIDER_WIDTH = 200
SLIDER_HEIGHT = 20

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Slider")
clock = pygame.time.Clock()

# Slider properties
slider_x = (WIDTH - SLIDER_WIDTH) // 2
slider_y = HEIGHT // 2
slider_value = 0.5  # Initial value between 0 and 1

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is held
                # Update slider position based on mouse movement
                slider_x = max(0, min(WIDTH - SLIDER_WIDTH, slider_x + event.rel[0]))

    # Draw slider background
    pygame.draw.rect(screen, GRAY, (slider_x, slider_y, SLIDER_WIDTH, SLIDER_HEIGHT))

    # Draw slider handle
    handle_x = slider_x + int(slider_value * SLIDER_WIDTH)
    pygame.draw.rect(screen, BLACK, (handle_x, slider_y, 10, SLIDER_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
