# Programmer: Bruce Provencher
# Date: 03 FEB 2019
# Project: Pygame Text / Using a Function

import pygame
import sys
import time
from pygame.locals import *

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600

FPS = 60

# Manage how quickly the screen is updated
clock = pygame.time.Clock()

# Set screen dimensions
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adding Text to Screen 1.0")

font_name = pygame.font.match_font('Arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    # Make text look less jagged on screen by setting
    # anti-aliasing to True
    text_surface = font.render(text, True, BLUE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


keep_looping = True

while keep_looping:

    # Main program loop (AKA game loop)

    # Handle the user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_looping = False
        elif event.type == pygame.KEYDOWN:
            # Use SPACEBAR to tell Python what to do next...
            if event.key == pygame.K_SPACE:
                pass

    # Set background color for screen
    screen.fill(GREEN)

    # Call the draw_text ( ) function
    draw_text(screen, "Hello, world!", 30, SCREEN_WIDTH / 2, 50)

    # Set frame speed for game
    clock.tick(FPS)
    # Update screen with what we've drawn
    pygame.display.flip()

pygame.quit()
