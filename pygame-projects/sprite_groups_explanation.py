# Programmer: Bruce Provencher
# Date: 01 MAR 2019
# Project: Sprite Groups & Pygame
# Source: https://www.youtube.com/watch?v=xcZUusjTShc


# (I)mport & (I)nitialize
import pygame, sys, random, time
from pygame.locals import *
import random
#pygame.init()

# Some color CONSTANTS using RGB triads
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

FPS = 60

class Sphere(pygame.sprite.Sprite):
	'''This class creates spherical sprites when passed a color,
	a radius, and a starting location (x,y).
	
	new_sphere = Sphere(color, radius, location)
	
	Class also contains methods for moving the sprites and detecting collisions
	between the sprites.'''
	
	def __init__(self, color, radius, location):
		# Creates the basic sprite and defines the rectangle and initial
		# speed of the sprite
		pygame.sprite.Sprite.__init__(self)
		self.frame = pygame.Surface((radius * 2, radius * 2))
		self.frame.fill(WHITE)
		pygame.draw.circle(self.frame, color, (radius, radius), radius, 0)
		self.rect = self.frame.get_rect()
		self.rect.topleft = location
		self.speed = [2, 2]
		
	def move_spheres(self, window_size):
		
		# Defines the walls so the sprites are contained within the window
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > window_size[0]:
			self.speed[0] *= -1
		if self.rect.top < 0 or self.rect.bottom > window_size[1]:
			self.speed[1] *= -1
			
	def collide(self, group1):
		# Determines whether the sprite has collided with another sprite
		# in a different group
		# 'False' below means don't remove it from the sprite group
		if pygame.sprite.spritecollide(self, group1, False):
			self.speed[0] *= -1
			self.speed[1] *= -1
		
	



if __name__ == '__main__':
	pygame.init()
	window_size = (400, 400)
	pygame.display.set_caption('Colliding Spheres')
	screen = pygame.display.set_mode(window_size)
	screen.fill(WHITE)
	
	# Create a white background to cover the sprites as they are moved
	background = pygame.Surface(window_size)
	background.fill(WHITE)
	
	# Create a sprite group, which is easy to loop through later
	# Sprite group also needed to do collision detection
	spheres = pygame.sprite.Group()
	
	# List of initial locations (set up as tuples for each sprite)
	locations = [(100, 100), (250, 75), (75, 30), (300, 300)]
	
	# Loop to create the sprites, assign them a random color, and add them
	# to the sprite group
	for x in locations:
		color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
		radius = 25
		ball = Sphere(color, radius, x)
		spheres.add(ball)
		
# (E)nvironment
# Controlling your game environment with the 
# flag variable and the clock

# Create a flag variable that tells the WHILE
# loop to keep looping until the user clicks the 
# close button on the window (which then sets the flag 
# variable to False)
keep_looping = True

# Manage how often the screen is updated
clock = pygame.time.Clock()

# (A)ction takes place in the WHILE loop
while keep_looping:
	
	# Use FOR loop to check if the user DID something [event]
	# (such as close the drawing window)
	# Note how the code is indented in the WHILE and
	# FOR loops!
	for event in pygame.event.get():
		# IF user closed the window, then exit
		# the FOR loop
		if event.type == pygame.QUIT: # Capitalize QUIT!
			keep_looping = False
			
	screen.blit(background, (0, 0))
	
	for ball in spheres:
		ball.move_spheres(window_size)
		spheres.remove(ball) # Can't check for collision with itself
		ball.collide(spheres)
		spheres.add(ball)
		screen.blit(ball.frame, ball.rect)

	# Set screen refresh/redraw rate [frames per second]
	pygame.display.update()
	time.sleep(0.02) # Delay for smoother animation and so we can see it work
	clock.tick(FPS)
	
# Close window and quit
pygame.quit()
