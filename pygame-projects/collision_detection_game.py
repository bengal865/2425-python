#######################################
# Author: Bruce Provencher
# Project: Collision Detection Game
# Date: 12 APR 2013
#######################################

# Import the pygame, sys, and random modules

import pygame, sys, random
from pygame.locals import *


# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Build the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode ((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption ('Alien Cheez-Its Game')


# Initialize the movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Set the colors
BLACK = (0,0,0)
WHITE = (255,255,255,255)
RED = (255,0,0)
GREEN = (102, 204, 0)
BLUE = (0,0,255)
YELLOW = (255,195,0)

# Create the player and food data structures

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)

# Create an empty list named foods
foods = []

for i in range (20):
	foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
	
# Start the game loop
while True:
	# Check for events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
			
		if event.type == KEYDOWN:
			# Change the keyboard variables
			if event.key == K_LEFT or event.key == ord('a'):
				moveRight = False
				moveLeft = True
				
			if event.key == K_RIGHT or event.key == ord('d'):
				moveRight = True
				moveLeft = False
				
			if event.key == K_UP or event.key == ord('w'):
				moveDown = False
				moveUp = True
				
			if event.key == K_DOWN or event.key == ord('s'):
				moveUp = False
				moveDown = True
				
		if event.type == KEYUP:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

				if event.key == K_LEFT or event.key == ord ('a'):
					moveLeft = False
				
				if event.key == K_RIGHT or event.key == ord('d'):
					moveRight = False
				
				if event.key == K_UP or event.key == ord ('w'):
					moveUp = False
				
				if event.key == K_DOWN or event.key == ord('s'):
					moveDown = False
					
				if event.key == ord('x'):
					player.top = random.randint(0, WINDOWHEIGHT - player.height)
					player.left = random.randint(0, WINDOWWIDTH - player.width)
					
		if event.type == MOUSEBUTTONUP:
				foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
			
	foodCounter +=1
	
	if foodCounter >= NEWFOOD:
		# Add new food
		foodCounter = 0
		foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

	# Draw the blaci background onto the surface
	windowSurface.fill(BLACK)


	# Move the player
	if moveDown and player.bottom < WINDOWHEIGHT:
		player.top += MOVESPEED
		
	if moveUp and player.top > 0:
		player.top -= MOVESPEED
		
	if moveLeft and player.left > 0:
		player.left -= MOVESPEED
		
	if moveRight and player.right < WINDOWWIDTH:
		player.right += MOVESPEED
		
	# Draw the player onto the surface
	pygame.draw.rect(windowSurface, GREEN, player)
	
	# Check whether player has contacted any food squares
	
	for food in foods[:]:
		if player.colliderect(food):
			foods.remove(food)
			
	# Draw the food
	
	for i in range (len(foods)):
		pygame.draw.rect(windowSurface, YELLOW, foods[i])



	# Draw window onto the screen
	pygame.display.update()
	mainClock.tick(40)


			
