#######################################
# Programmer: Alexander Raptis
# Date: 18 FEB 2019
# Project: Classes Bouncing Balls
#######################################

# Importing
import pygame as pyg
import random as r

# Defining constants
BLACK 			= (  0,  0,  0)
WHITE 			= (255,255,255)
RED				= (255,  0,  0)
SCREEN_WIDTH 	= 700
SCREEN_HEIGHT	= 500
BALL_SIZE		= 25

class Ball():
	""" Sets settings for a ball """
	def __init__(self):
		# Defining attributes
		self.x = 0 
		self.y = 0
		self.change_x = 0
		self.change_y = 0
		self.color = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
		
def make_ball():
	# Gives settings to ball object then returns the value of the object
	ball = Ball()
	
	ball.x = r.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
	ball.y = r.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
	ball.change_x = r.randint(-10,10)
	ball.change_y = r.randint(-10,10)
	
	return ball

def main():
	# Starting main function
	pyg.init() # Initializing pygame
	
	# Setting screen size
	size = [SCREEN_WIDTH,SCREEN_HEIGHT]
	screen = pyg.display.set_mode(size)
	
	# Setting window caption
	pyg.display.set_caption("Bouncing Balls (By Alex Raptis)")
	
	# Setting clock
	clock = pyg.time.Clock()
	
	# Setting fonts
	font_fps = pyg.font.SysFont('Arial',24,True,False)
	font_ball = pyg.font.SysFont('Arial',20,True,False)
	
	# Creating ball list
	ball_list = []
	
	# Creating one ball
	ball = make_ball()
	ball_list.append(ball)

	active = True
	
	while active:
		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				active = False
			elif event.type == pyg.KEYDOWN:
				# Creating new ball with space key
				if event.key == pyg.K_SPACE:
					ball = make_ball()
					ball_list.append(ball)
		
		# Bouncing balls off of screen axis		
		for ball in ball_list:
			ball.x += ball.change_x
			ball.y += ball.change_y
			
			if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
				ball.change_y *= -1
			if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
				ball.change_x *= -1
		
		# Drawing
		screen.fill(BLACK)
		
		for ball in ball_list:
			# Drawing balls
			pyg.draw.circle(screen,ball.color,[ball.x,ball.y],BALL_SIZE)
			
			# Drawing ball labels
			ball_text = font_ball.render("BALL",True,RED)
			screen.blit(ball_text,[ball.x-21,ball.y-13])
		
		# Drawing fps text
		fps_text = font_fps.render(f"FPS: {int(clock.get_fps())}",True,WHITE)
		screen.blit(fps_text,[0,0])
			
		# Setting fps
		clock.tick(60)
		
		# Flipping everything to screen
		pyg.display.flip()
		
	pyg.quit()

# Running main function
if __name__ == "__main__":
	main()
