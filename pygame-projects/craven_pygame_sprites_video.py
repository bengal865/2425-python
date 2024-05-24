# Programmer: Bruce Provencher
# Date: 05 MAR 2019
# Project: Pygame Sprites
# Source: https://youtu.be/4W2AqUetBi4 (Craven book)

# (I)mport & (I)nitialize


import pygame, random
pygame.init()

# Some color CONSTANTS using RGB triads
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
ORANGE = (255, 127, 64)

class Block(pygame.sprite.Sprite):
	
	# Pass color, width and height values for block to constructor method
	def __init__(self, color, width, height):
		# Then call the constructor for the parent class (Sprite)
		# Call the parent class (Sprite) constructor
		
		super().__init__() # Parent constructor method
		
		# Create an image of the block and fill it with a color
		# Could also use an image loaded from your computer...
		
		#my_image = pygame.image.load('imagename.png').convert()
		#my_image.set_colorkey(WHITE)
		#self.image = my_image
		
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		
		# Get rectangle object that has the dimensions of the image
		
		self.rect = self.image.get_rect() # Has x, y, width and height values to specify size of rectangle
		
# Regular function for drawing text onto the screen
def draw_text(surf, text, size, x, y):
	
	
	font_name = pygame.font.match_font('Arial Bold')
	font = pygame.font.Font(font_name, size)
	
	
	# Make text look less jagged on screen by setting
	# anti-aliasing to True
	
	
	text_surface = font.render(text, True, BLACK)
	
	text_rect = text_surface.get_rect()
	
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)

# Frames per second
FPS = 60

# (D)isplay settings
# Give Python the height and width of the window
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700


# Store height and width in a tuple named 'size'
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Craven Tutorial/Sprites")

# Load sound files
sound_effect = pygame.mixer.Sound('beep.ogg')

# Load and play BACKGROUND MUSIC 
pygame.mixer.music.load('atomic_cat2.ogg')
pygame.mixer.music.play(-1, 0.0)

	
# Create a sprite group, so it's easier to manage all the sprites used in the game
# The block_list DOES NOT contain the player sprite
block_list = pygame.sprite.Group()

# Create a second list that contains ALL the sprites, including the player block
all_sprites_list = pygame.sprite.Group()

# Use a FOR loop to create 50 (green) blocks for the game
for i in range(55):
	# Block's width = 20, height = 15
	
	
	block = Block(GREEN, 20, 15)
	
	# Set a random location for each green block
	
	
	block.rect.x = random.randrange(SCREEN_WIDTH - 20)
	block.rect.y = random.randrange(SCREEN_HEIGHT - 15)
	
	# Add each block to my list of blocks and to the list of all sprites
	
	
	block_list.add(block)
	all_sprites_list.add(block)
	
	
# Create the player block...


player = Block (RED, 20, 15)
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

# Score variable
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
	screen.fill(BLUE)
	
	# Get x,y coordinates for mouse pointer, then set player
	# to same position on screen as mouse pointer
	# get_pos() returns a list of two values, one for x, the other for y
	
	
	pos = pygame.mouse.get_pos()
	
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	
	
	# Has the player block collided with anything else?
	# 'True' removes any block that collides with the player
	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
	
	# Check the list of collisions
	'''if len(blocks_hit_list) > 0:
		score += len(blocks_hit_list)
		#print(f"Your score: {score}")'''
		
	for block in blocks_hit_list:
		score += 1
		
		if score <= 25:
			
			sound_effect.play()
		else:
			
			pygame.mixer.music.stop()
		
	# Call the draw_text ( ) function
	draw_text(screen, "Mr. P's Score: " + str(score), 40, 125, 20)

	# Now draw ALL the sprites on the screen
	all_sprites_list.draw(screen)
	
	
	# UPDATE the screen with what we've drawn
	pygame.display.flip()
	
	# Set screen refresh/redraw rate [frames per second]
	clock.tick(FPS)
	
# Close window and quit
pygame.quit()
