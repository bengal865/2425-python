# Programmer: Bruce Provencher
# Date: 01 DEC 2018
# Project: Moving Sprites That Bounce
# Source: http://programarcadegames.com/python_examples/show_file.php?file=moving_sprites_bounce.py

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

# (D)isplay settings
# Give Python the height and width of the window
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700
# Store height and width in a tuple named 'size'
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving & Bouncing Sprites")

FPS = 60


class Block(pygame.sprite.Sprite):
	'''This class is a representation of a ball in the real world.'''
	
	def __init__(self, color, width, height):
		'''Pass in the color and its x and y value (for positioning on screen).'''
		
		# Call the parent class constructor method
		super().__init__()
		
		# Create an image of the block and fill it with a color
		# Could also use an image file instead of just a colored block
		
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		
		# Get the rectangle object that has the same dimensions as the 
		# image file you're using
		
		self.rect = self.image.get_rect()
		
		# Instance variables that control the boundaries of where the ball bounces
		self.left_boundary = 0
		self.right_boundary = 0
		self.top_boundary = 0
		self.bottom_boundary = 0
		
		# Instance variables for current speed and direction
		self.change_x = 0
		self.change_y = 0
		
	def update(self):
		# Update method is called each frame (frames/sec)
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		
		if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
			self.change_x *= -1
			
		if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
			self.change_y *= -1		
			
class Player(Block):
	# This Player class uses a new method that moves the block by following the mouse pointer
	# This update method overrides the method by the same name in the Block class
	def update(self):
		pos = pygame.mouse.get_pos()
		
		# Get the x and y values from the list 'pos'
		# Match the player's location on screen to the mouse position on the screen
		self.rect.x = pos[0]
		self.rect.y = pos[1]



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

# This is a list of 'sprites.' Each block in the program is
# added to this list. 
block_list = pygame.sprite.Group()
 
# This is a list of every sprite -- all the blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Create the 50 blocks using a FOR loop
for i in range(50):
	block = Block(BLACK, 20, 15)

	# Set a random location for the block
	block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
	block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)
 
	block.change_x = random.randrange(-3, 4)
	block.change_y = random.randrange(-3, 4)
	block.left_boundary = 0
	block.top_boundary = 0
	block.right_boundary = SCREEN_WIDTH
	block.bottom_boundary = SCREEN_HEIGHT
 
	# Add the block to the list of objects
	block_list.add(block)
	all_sprites_list.add(block)
	

# Create a red player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)


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
	
	
	# Call update ( ) method on every sprite in the list
	all_sprites_list.update()
	
	# Has the player block collided with any of the other sprites?
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
