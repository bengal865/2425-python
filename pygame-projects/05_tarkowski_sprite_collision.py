###############################
#Programmer: Alyssa Tarkowski
#Date: 1 April 2019
#Project: Sprite Collision
###############################

# Import a library of functions called 'pygame'
import pygame, random

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (191, 191, 191)
SEA_GREEN = (102, 255, 204)

# Add sounds
hit_sound = pygame.mixer.Sound("beep.ogg")
pygame.mixer.music.load("born.ogg")
#pygame.mixer.music.load("3dd_lmwig.ogg")
pygame.mixer.music.play()

# Create block class

class Block(pygame.sprite.Sprite):
	"""A class to represent a block
	It derives from the "Sprite" class in Pygame"""
	
	def __init__(self,color,width,height):
		#Call the parent class(Sprite) constructor
		super().__init__()
		
		self.image = pygame.Surface([width,height])
		self.image.fill(color)
		
		# Update position of this object
		self.rect = self.image.get_rect()
		
	def reset_pos(self):
		
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, screen_width)
		
	def update(self):
		#Called each frame
		
		self.rect.y += 1
		if self.rect.y > 410:
			self.reset_pos()
			
class Player(Block):
	"""Uses block class, but overrides the 'update' functionality with
	a new movement function that will move the block with the mouse"""
	
	def update(self):
		
		pos = pygame.mouse.get_pos()
		
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		
		
# Set the width and height of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Tarkowski Sprite Collision")

# Create block list
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
	block = Block(BLACK, 20, 15)
	
	block.rect.x = random.randrange(screen_width)
	block.rect.y = random.randrange(screen_height)
	
	block_list.add(block)
	all_sprites_list.add(block)
	
#Create player
player = Player(SEA_GREEN, 20, 15)
all_sprites_list.add(player)

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

#--------------------Main Program Loop------------------------
while done == False:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
		
			


	screen.fill(GREY)
	
	#Calls update() method on all sprites
	all_sprites_list.update()
	
	#Collision detection
	blocks_hit_list = pygame.sprite.spritecollide(player,block_list, False)
	
	for block in blocks_hit_list:
		hit_sound.play()
		score += 1
		print(score)
		
		block.reset_pos()
		
	all_sprites_list.draw(screen)

	font = pygame.font.SysFont('SF Sports', 35, True, False)
	text = font.render("Score: " + str(score), True, WHITE)
	screen.blit(text, [25, 25])
	
	
	# Limit to 20 frames per second
	clock.tick(20)
	
	pygame.display.flip()
	
pygame.quit()
