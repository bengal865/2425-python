# Programmer: Bruce Provencher
# Date: 06 MAR 2019
# Project: Sprite That Uses an Image File

# (I)mport & (I)nitialize
import pygame
import random
pygame.init()

# Some color CONSTANTS using RGB triads
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

FPS = 60
# (D)isplay settings
# Give Python the height and width of the window
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700
# Store height and width in a tuple named 'size'
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sprite Using an Image File")

class Block(pygame.sprite.Sprite):
	def __init__(self, filename):
		
		super().__init__() # Constructor for the parent class (Sprite class)
		
		self.image = pygame.image.load(filename).convert()
		
		# NOTE: Change to WHITE if page background color is WHITE
		self.image.set_colorkey(WHITE)
		
		# Fetch the rectangle object that has the dimensions of the image
		# you're using
		# Update position of this object by changing the values for rect.x
		# and rect.y
		self.rect = self.image.get_rect()
		
# Create a list to store all the blocks (sprites)
# that are created for this project
block_list = pygame.sprite.Group()

# Another list that contains the player block as well as all the other
# sprites for this project
all_sprites_list = pygame.sprite.Group()

# Create the 50 blocks/sprites
for i in range(50):
	# This represents a block
	block = Block("alien.png")
	
	# Set random location for the block/alien
	block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
	block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)
	
	# Add the block to the list of blocks
	block_list.add(block)
	all_sprites_list.add(block)
	
# Create a RED player block
player = Block("ufo.png")
all_sprites_list.add(player)

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

score = 0

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
			
	
	# Set background color of the drawing window
	screen.fill(GREEN)
	
	
	# Get current mouse position (returned as list of x,y values)
	pos = pygame.mouse.get_pos()
	
	# Get the x and y values from the list 'pos'
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	
	# See if the player block has collided with any of the other blocks
	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
	
	# Check the list of collisions
	for block in blocks_hit_list:
		score += 1
		print(f"Score: {score}")
	
	# Draw all the sprites on the screen
	all_sprites_list.draw(screen)
	
	
	# UPDATE the screen with what we've drawn
	pygame.display.flip()
	
	# Set screen refresh/redraw rate [frames per second]
	clock.tick(FPS)
	
# Close window and quit
pygame.quit()
