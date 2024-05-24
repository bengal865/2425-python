# Bruce Provencher
# 20 APR 2021
# Pygame Text & Sound Effects


# Import modules and initialize settings

import pygame
import sys

pygame.init()

# Some color CONSTANTS using RGB triads
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

# Display settings
# Tell Python the height and width of the window
HEIGHT = 400
WIDTH = 700
# Store height and width in a tuple named 'size'
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Screen Text & Sound Effects")


class Label():
	'''A label class that lets us quickly draw text on our Pygame screen.'''
	
	def __init__(self, label_text, text_rect_x, text_rect_y, text_color, bg_color, font_name, font_size):
		
		self.font_name = font_name
		self.font_size = font_size
		
		self.font = pygame.font.SysFont(self.font_name, self.font_size)
		
		self.label_text = label_text
		
		self.text_color = text_color
		self.bg_color = bg_color
		
		# True means the font is anti-aliasied (so the letters appear as smooth lines on the screen)
		self.text = self.font.render(self.label_text, True, self.text_color, self.bg_color)
		
			
		self.text_rect_x = text_rect_x
		self.text_rect_y = text_rect_y
		
	def draw_label(self):
		screen.blit(self.text, [self.text_rect_x, self.text_rect_y])
		
		
play_bgm_label = Label("Press p to play background music", 50, 50, BLACK, YELLOW, 'Helvetica', 20)	
pause_bgm_label = Label("Press s to pause background music", 50, 95, BLUE, WHITE, 'Helvetica', 20)
name_label = Label("Bruce Provencher", 275, 370, BLACK, WHITE, 'Helvetica', 20)


keep_looping = True

# Manage how often the screen is updated
clock = pygame.time.Clock()

# Frames per second (FPS) for screen refresh rate
FPS = 60

# Main action takes place inside the WHILE loop
while keep_looping:
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Capitalize QUIT!
			keep_looping = False
			
	
	# Set background color of drawing window to green using color CONSTANT
	screen.fill(WHITE)
	
	# Draw some lines or shapes below this comment...
	
	pause_bgm_label.draw_label()
	play_bgm_label.draw_label()
	name_label.draw_label()
		
	# UPDATE the screen with what we've drawn
	pygame.display.flip()
	
	# Set screen refresh/redraw rate [frames per second]
	clock.tick(FPS)
	
# Close window and quit
pygame.quit()
sys.exit()
