# Programmer: Bruce Provencher
# Date: 03 FEB 2019
# Project: Bouncing Balls wth Bounce Sound Effect

import pygame, random

# Define CONSTANTS
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

BALL_SIZE = 15

class Ball():
	"""Class that describes a generic ball."""
	def __init__(self):
		self.x = 0
		self.y = 0
		self.change_x = 0
		self.change_y = 0
		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		self.sound = pygame.mixer.Sound('beep.ogg')
		
		
def make_ball():
	
	ball = Ball()
	
	
	# Set starting position of ball, taking into account
	# size of ball so that it isn't drawn on the edge
	# of the screen or off the screen
	
	ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
	ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
	
	# Set ball speed and direction
	ball.change_x = random.randrange(-2, 10)
	ball.change_y = random.randrange(-2, 7)
	
	return ball
		
def main():
	# This is the main part of the script
	pygame.init()
	pygame.mixer.init()
	# Set screen dimensions
	size = [SCREEN_WIDTH, SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Bouncing Balls")
	
	#beep_sound = pygame.mixer.Sound('beep.ogg')
	zap_sound = pygame.mixer.Sound("zap13.ogg")
	
	# Play a sound effect when user hits SPACEBAR
	# zap_sound = pygame.mixer.Sound("zap13.ogg")
	
	pygame.mixer.music.load("born.ogg")
	pygame.mixer.music.play()
	
	# Loop until user clicks close button on drawing window
	done = False
	# Manage how quickly the screen is updated
	clock = pygame.time.Clock()
	
	# Create a list to hold the balls
	ball_list = []
	ball = make_ball() # Call the make_ball () function to make a starter ball
	
	ball_list.append(ball)
	
	# Main program loop (AKA game loop)
	while not done:
		# Handle the user events 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				# Use SPACEBAR to spawn a new ball
				if event.key == pygame.K_SPACE:
					zap_sound.play()
					
					# Call the make_ball( ) function (again!)
					ball = make_ball()
					ball_list.append(ball)
					
										
		for ball in ball_list:
			# Position the ball's center
			ball.x += ball.change_x
			ball.y += ball.change_y
			
			# Did the ball bounce off the top/bottom of screen?			
			if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
				ball.sound.play()
				ball.change_y *= -1
			
			# Did the ball bounce off the LEFT/RIGHT side of screen?	
			if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
				ball.sound.play()
				ball.change_x *= -1
				
		# Set background color for screen
		screen.fill(BLACK)
		
		
		# Draw the balls
		for ball in ball_list:
			
			pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)
			
		# Set frame speed for game
		clock.tick(60)
		# Update screen with what we've drawn
		pygame.display.flip()
		
	# Close everything down
	pygame.quit()
	
if __name__ == "__main__":
	main()
