
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
AQUA  = (91, 229, 245)
PURPLE= (248, 38, 255)
BLUE  = (0, 50, 255)
YELLOW= (246, 255, 0)
ORANGE= (255, 157, 0)
PINK  = (255, 0, 162)
GREY  = (170, 174, 191)
LBLUE = (81, 172, 237)

SCREENHEIGHT = 600

class Car(pygame.sprite.Sprite):
    def __init__(self,color,width,height,speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x >= 390:
            self.rect.x -= pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x <= 35:
            self.rect.x += pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self,speed):
        self.rect.y -= self.speed * speed / 20
            
    def changeSpeed(self,speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

    


