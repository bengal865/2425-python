# Simple Game Window in Pygame

import pygame
import random
import sys
import os
from labelmod import Label

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 700  
HEIGHT = 500 

pygame.init()
pygame.mixer.init()  

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("My Game Window")

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


clock = pygame.time.Clock()
FPS = 60 

basic_font = pygame.font.SysFont('Arial', 48)

msg1 = 'Game Over!'
my_sample_surf = basic_font.render(msg1, 1, WHITE)

msg2 = 'Programmer: Abraham Lincoln'
your_sample_surf = basic_font.render(msg2, 1, GREEN)

ctc_session = 'pm web & app dev'
session = Label(f"Session: {ctc_session.upper()}", screen.get_width() / 2, screen.get_height() / 2, RED,GREEN,'Arial', 42, False, True, True)



keep_looping = True
while keep_looping:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            keep_looping = False


    screen.fill(BLACK)


    screen.blit(my_sample_surf, [screen.get_width() / 2 - my_sample_surf.get_width() / 2, 50])
    screen.blit(your_sample_surf, [screen.get_width() / 2 - your_sample_surf.get_width() / 2, 175])
    session.draw(screen)
    
    pygame.display.flip()


pygame.quit()