import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draggable Object")

# Set up the object
object_size = 50
object_color = (255, 0, 0)
object_rect = pygame.Rect((width - object_size) // 2, (height - object_size) // 2, object_size, object_size)

dragging = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if object_rect.collidepoint(event.pos):
                dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                object_rect.x, object_rect.y = event.pos

    # Draw everything
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, object_color, object_rect)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
