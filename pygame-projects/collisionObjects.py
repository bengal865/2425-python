# Programmer: Bruce Provencher
# Date: 20 JAN 2019
# Project: Collision Objects / Express Line book
# pp. 257ff
# collisionObjects.py

import pygame
import random


PURPLE = (224, 55, 197)
YELLOW = (230, 241, 30)
WHITE = (255, 255, 255)
SKY_BLUE = (143, 231, 233)


class Square(pygame.sprite.Sprite):
    # Makes a box with random start position and specified color
    # To make a red square, use
    # red_square = Square((255, 0, 0), screen)

    # Need to define screen in advance and import
    # the random module

    def __init__(self, color, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = random.randrange(0, screen.get_width())
        self.rect.top = random.randrange(0, screen.get_height())


class Circle(pygame.sprite.Sprite):
    '''Makes a blue circle that follows the mouse.'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, PURPLE, (25, 25), 25, 0)
        self.rect = self.image.get_rect()
      
        

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Label(pygame.sprite.Sprite):
    '''Generates a label we can add to the screen.'''
    # Attributes
    # font = any Pygame font object
    # text = the text for the label itself
    # center = (x, y) coordinates for the center of the Label

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (320, 240)

    def update(self):
        self.image = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
