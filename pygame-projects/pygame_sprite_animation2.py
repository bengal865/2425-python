# Programmer: Bruce Provencher
# Date: 22 FEB 2019
# Project: Sprite Animation
# Source: https://youtu.be/1w5jcAuZ820
# Part 2 of YT video

import pygame, sys
from pygame.locals import *
import blocks, random

def main():
	pygame.init()
	
	SCREEN_WIDTH = 600
	SCREEN_HEIGHT = 500
	BLOCK_WIDTH = 50
	BLOCK_HEIGHT = 50
	
	WHITE = (255, 255, 255)
	
	main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
	pygame.display.set_caption("Lots of Blocks!")
	# Lets you use certain methods on the entire sprite group, can also detect
	# collisions between sprites
	blocksGroup = pygame.sprite.Group()
	
	# Use FOR loop to create 10 sprites
	for x in range(10):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		
		my_block = blocks.Block(main_surface, (r, g, b), BLOCK_WIDTH, BLOCK_HEIGHT)
		# Set starting x and y value for each of the blocks
		my_block.rect.x = random.randrange(SCREEN_WIDTH - BLOCK_WIDTH)
		my_block.rect.y = random.randrange(SCREEN_WIDTH - BLOCK_HEIGHT)
		blocksGroup.add(my_block)
		
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		main_surface.fill(WHITE)
		
		for block in blocksGroup:
			blocksGroup.remove(block)
			block.collide(blocksGroup)
			blocksGroup.add(block)
		
		
		blocksGroup.update()
		blocksGroup.draw(main_surface)
		pygame.display.update()
		
# Call the main function
main()
