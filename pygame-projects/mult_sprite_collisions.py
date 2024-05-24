# Programmer: Bruce Provencher
# Date: 20 JAN 2019
# Project: Multiple Sprite Collisions / Express Line book
# pp. 264ff
# mult_sprite_collisions.py

import pygame
import collisionObjects

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (107, 205, 47)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

FPS = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    pygame.display.set_caption("MULT Sprite Collisions")
    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)
    screen.blit(background, (0, 0))

    label_output = collisionObjects.Label()
    label_output.center = (100, 150)
    label_output.text = ""

    circle = collisionObjects.Circle()
    
    
    
    squares = []
    for i in range(10):
        square = collisionObjects.Square((255, 0, 0), screen)
        squares.append(square)

    basicSprites = pygame.sprite.Group(circle, label_output)
    squareGroup = pygame.sprite.Group(squares)

    clock = pygame.time.Clock()
    # Make mouse pointer invisible
    # pygame.mouse.set_visible(False)

    keep_going = True
    while keep_going:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
        # Boolean value 'False' [see below] for killing the collided sprite, which still exists
        # in memory, but is removed from its group so it is no longer
        # updated or displayed
        if pygame.sprite.spritecollide(circle, squareGroup, False):
            label_output.text = "Collision!!"
        else:
            label_output.text = "No collision!!"

        squareGroup.clear(screen, background)
        basicSprites.clear(screen, background)

        squareGroup.update()
        basicSprites.update()

        squareGroup.draw(screen)
        basicSprites.draw(screen)
        
        
        

        pygame.display.flip()

    # pygame.quit()


if __name__ == "__main__":
    main()
