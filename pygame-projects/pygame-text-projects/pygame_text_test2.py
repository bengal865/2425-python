# Programmer: Bruce Provencher
# Date: 22 FEB 2019
# Project: Using a Class to Draw Pygame Text

import pygame, sys

pygame.init()


WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600

FPS = 60

# Manage how quickly the screen is updated
clock = pygame.time.Clock()

# Set screen dimensions and caption
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Adding Text to Screen 2.0")

class Label():
	'''A label class that lets us quickly draw text on our screen.'''

	def __init__(self, label_text, centerx, centery, text_color, bg_color, font_name, font_size):
		
		self.font_name = font_name
		self.font_size = font_size
		
		self.font = pygame.font.SysFont(self.font_name, self.font_size)
		self.label_text = label_text
		self.text_color = text_color
		self.bg_color = bg_color
		# True means the font is anti-aliased (so it doesn't appear so jagged on screen)
		self.text = self.font.render(self.label_text, True, self.text_color, self.bg_color)
		
		self.text_rect = self.text.get_rect()
		self.text_rect.centerx = centerx
		self.text_rect.centery = centery
		
	def draw_label(self):
		screen.blit(self.text, self.text_rect)


keep_looping = True

while keep_looping:
	
# Main program loop (AKA game loop)

	# Handle the user events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_looping = False
		elif event.type == pygame.KEYDOWN:
			pass
			if event.key == pygame.K_SPACE:
				pass
						
	# Set background color for screen
	screen.fill(GREEN)
	
	# Create instances of the Label class
	my_label = Label("Hello, world!", 100, 150, RED, GREEN, "Arial", 20)	
	label2 = Label("Python rocks!", 400, 450, BLACK, YELLOW, "Times New Roman", 40)
	
	# Draw the text on the screen
	my_label.draw_label()
	label2.draw_label()
		
	# Set frame speed for game
	clock.tick(FPS)
	# Update screen with what we've drawn
	pygame.display.flip()
	
pygame.quit()
