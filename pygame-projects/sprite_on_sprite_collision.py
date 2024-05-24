# Programmer: Bruce Provencher
# Date: 20 JAN 2019
# Project: Sprite On Sprite Collisions / Express Line book
# pp. 262ff
# sprite_on_sprite_collision.py

import pygame
import collisionObjects

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (107, 205, 47)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

FPS = 30


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sprite on Sprite Collisions")

    background = pygame.Surface(screen.get_size())
    background.fill(GREEN)
    screen.blit(background, (0, 0))

    label_output = collisionObjects.Label()
    label_output.center = (100, 50)
    label_output.text = ""

    circle = collisionObjects.Circle()

    square = collisionObjects.Square((0, 0, 255), screen)

    allSprites = pygame.sprite.Group(circle, square, label_output)

    clock = pygame.time.Clock()
    # Make mouse pointer invisible
    pygame.mouse.set_visible(False)

    keep_going = True
    while keep_going:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        if circle.rect.colliderect(square.rect):
            label_output.text = "Collision!!"
        else:
            label_output.text = "No collision!!"

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

    pygame.mouse.set_visible(True)

    # pygame.quit()


if __name__ == "__main__":
    main()
