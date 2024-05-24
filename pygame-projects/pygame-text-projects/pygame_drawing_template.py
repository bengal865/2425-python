# Your name here
# Add current date
# Pygame Drawing Template

# Import module and initialize settings


import pygame
import time
import sys

pygame.init()

# Some color CONSTANTS using RGB triads
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Display settings
# Tell Python the height and width of the window
HEIGHT = 400
WIDTH = 700
# Store height and width in a tuple named 'size'


size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pygame Drawing Template")

# Environment settings
# Controlling your game environment with the 
# flag variable and the clock

# Create a flag variable that tells the WHILE
# loop to keep looping until the user clicks the 
# close button on the window (which then sets the flag 
# variable to False)

keep_looping = True

# Manage how often the screen is updated
clock = pygame.time.Clock()

# Frames per second (FPS) for screen refresh rate
FPS = 60



def create_text_objects(text, font):
	text_surface = font.render(text, True, RED)
	return text_surface, text_surface.get_rect()


def display_my_text(text):
	# None means you're using the default system font
	large_text = pygame.font.Font(None, 120)
	text_surface, text_rect = create_text_objects(text, large_text)
	text_rect.center = (  ( WIDTH // 2), (HEIGHT // 2)  )
	screen.blit(text_surface, text_rect)
	pygame.display.update()


# Main action takes place inside the WHILE loop
while keep_looping:
	
	# Use FOR loop to check if the user DID something [check for an event]
	# such as close the drawing window
	# Note how the code is indented in the WHILE and
	# FOR loops!
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Capitalize QUIT!
			keep_looping = False
			
	
	# Set background color of drawing window to green using color CONSTANT
	screen.fill(GREEN)
	
	
	# Draw some lines or shapes below this comment...


	display_my_text('Hello!!!!!')



	
	# UPDATE the screen with what we've drawn
	pygame.display.flip()
	
	# Set screen refresh/redraw rate [frames per second]
	clock.tick(FPS)
	
# Close window and quit
pygame.quit()
sys.exit()

