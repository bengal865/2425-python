# Programmer: Bruce Provencher
# Date: 20 JAN 2019										
# Project: 


import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
FPS = 60

# Background graphics
bg_position = [0,0]

bg_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)
 
pygame.display.set_caption("BG Image & Spaceship")

# Load sound and graphics files before main game loop
click_sound = pygame.mixer.Sound("zap13.ogg")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			click_sound.play()
 
	# --- Game logic should go here
 
	# --- Screen-clearing code goes here
 
	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
 
	# If you want a background image, replace this clear with blit'ing the
	# background image.
	# screen.fill(WHITE)
	screen.blit(bg_image, bg_position)
	
	# Get current mouse position, which is returned as
	# a list of two values
	player_position = pygame.mouse.get_pos()
	x = player_position[0]
	y = player_position[1]
 
	# Copy player image to screen
	screen.blit(player_image, [x,y])
 
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# --- Limit to 60 frames per second
	clock.tick(FPS)
 
# Close the window and quit.
pygame.quit()
