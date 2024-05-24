#####################################
# Programmer: Alexander Raptis
# Date: 2 APR 2019
# Project: Pygame Rectangle Collision
#####################################

import pygame as pyg
import random as r

# Color constants
WHITE 	= (255,255,255)
BLACK	= (  0,  0,  0)
RED		= (255,  0,  0)
GREEN	= (  0,255,  0)
BLUE    = (  0,  0,255)
CYAN	= (  0,255,255)
YELLOW	= (255,255,  0)
MAGENTA	= (255,  0,255)

# Display constants
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

class Label():
	""" Creates a text label to draw to the screen """
	def __init__(self, label_text, centerx, centery, text_color, bg_color, font_name, font_size, bold, italic,anti_alias):
		# Creating attributes to create font
		self.font_name = font_name
		self.font_size = font_size
		self.bold = bold
		self.italic = italic
		
		# Creating font and setting attributes to render font
		self.font = pyg.font.SysFont(self.font_name, self.font_size,self.bold,self.italic)
		self.label_text = label_text
		self.text_color = text_color
		self.bg_color = bg_color
		self.anti_alias = anti_alias
		
		# Rendering font
		self.text = self.font.render(self.label_text,self.anti_alias,self.text_color,self.bg_color)
		
		# Setting border for font
		self.text_rect = self.text.get_rect()
		self.text_rect.centerx = centerx
		self.text_rect.centery = centery
	
	def draw(self,surf):
		# Draws font to surface
		surf.blit(self.text,self.text_rect)

class Block(pyg.sprite.Sprite):
	""" Creates a block sprite """
	def __init__(self,color,width,height,player):
		super().__init__()
		
		if player:
			# Creating player image from png
			self.image = pyg.image.load("player.png").convert()
			# Setting alpha key for png file
			self.image.set_colorkey((130,130,200))
		else:
			# Creating sprite image with custom width and height
			self.image = pyg.Surface([width,height])
			# Filling sprite with custom color
			self.image.fill(color)
			
		# Setting collision rectangle for sprite
		self.rect = self.image.get_rect()

def main():
	# Initializing pygame
	pyg.init()

	# Setting screen size and icon
	icon = pyg.image.load("icon.png")
	pyg.display.set_icon(icon)
	size = [SCREEN_WIDTH,SCREEN_HEIGHT]
	screen = pyg.display.set_mode(size)

	# Setting window caption
	pyg.display.set_caption("Sprite Scoring [by Alex Raptis]")
	
	# Creating sounds
	snd1 = pyg.mixer.Sound("zap13.ogg")
	bgm = pyg.mixer.Sound("mbox.ogg")
	
	# Creating pygame mixer channels
	chnl1 = pyg.mixer.Channel(0)
	chnl2 = pyg.mixer.Channel(1)
	
	# Creating background image
	bg = pyg.image.load("bg.jpg").convert()
	
	# Creating sprite groups
	block_list = pyg.sprite.Group()
	all_sprites_list = pyg.sprite.Group()
	
	# Setting variable to determine whether or not blocks will be generated randomly
	block_gen = True
	
	# Creating blocks with random colors and locations
	if block_gen:
		for blk in range(100):
			block = Block((r.randint(0,255),r.randint(0,255),r.randint(0,255)),25,25,False)
		
			block.rect.x = r.randrange(SCREEN_WIDTH-25)
			block.rect.y = r.randrange(SCREEN_HEIGHT-25)
		
			block_list.add(block)
			all_sprites_list.add(block)
	
	# Creating rectangle 
	block_rect = pyg.Rect((SCREEN_WIDTH/2)-25,(SCREEN_HEIGHT/2)-25,50,50)
	
	# Creating list of rectangles
	block_rects = [
		pyg.Rect(25,50,50,50),
		pyg.Rect(250,50,25,25),
		pyg.Rect(50,150,100,100),
		pyg.Rect(175,250,50,50)
	]
	
	# Creating player
	player = Block(RED,25,25,True)
	all_sprites_list.add(player)
	
	# Setting clock
	clock = pyg.time.Clock()
	
	# Making mouse invisible
	pyg.mouse.set_visible(False)
	
	# Misc. variables for game loop
	score = 0
	colors = []
	
	# Setting volume for channels
	chnl1.set_volume(0.5)
	chnl2.set_volume(1)
	
	# Starting background music
	chnl1.play(bgm,-1)
	
	# Setting flag for game loop
	active = True
	
	while active:
		# Looking for events
		for event in pyg.event.get():
			# Seeing is window is closed
			if event.type == pyg.QUIT:
				active = False
			elif event.type == pyg.KEYDOWN:
				if event.key == pyg.K_ESCAPE:
					active = False
			
			# Drawing background image
			screen.blit(bg,[0,0])
			
			# Drawing rectangles using rects from list
			for rects in range(len(block_rects)):
				# Generating colors
				for clr in range(len(block_rects)):
					colors.append((r.randint(0,255),r.randint(0,255),r.randint(0,255)))
				# Drawing rectangles
				pyg.draw.rect(screen,colors[rects],block_rects[rects])
			
			# Getting mouse position
			mpos = pyg.mouse.get_pos()
			# Setting player position as mouse position
			player.rect.x = mpos[0]
			player.rect.y = mpos[1]
			
			# Setting rectangle color
			rectangle_color = BLUE
			
			# Initializing collision flag variable
			collision = False
			
			# Creating a list for collisions with blocks
			block_collide_list = pyg.sprite.spritecollide(player,block_list,True)
			
			# Adding to score and playing sound when block
			# collision occurs
			for block in block_collide_list:
				score += 1
				chnl2.play(snd1)
			
			# Setting player rectangle
			player_rect = pyg.Rect(mpos[0],mpos[1],25,25)
			
			# Detecting rectangle collisions
			if player_rect.colliderect(block_rect):
				rectangle_color = RED
				collision = True
				
			# Detecting rectangle list collisions
			if player_rect.collidelist(block_rects) >= 0:
				collision = True
				
			# Drawing rectangles for collision
			pyg.draw.rect(screen,rectangle_color,block_rect)
			
			# Drawing all sprites to the screeen	
			all_sprites_list.draw(screen)
			
			# Creating and drawing score text
			score_text = Label(f"Score: {score}",SCREEN_WIDTH/2,25,WHITE,RED,'Verdana',20,True,False,True)
			score_text.draw(screen)
			
			# Drawing collision text if collision occurs
			if collision:
				if player_rect.collidelist(block_rects) >= 0:
					collide_text = Label(f"Collision occured with block #{player_rect.collidelist(block_rects)+1}.",SCREEN_WIDTH/2,(SCREEN_HEIGHT/2)-85,WHITE,MAGENTA,'Verdana',24,True,True,True)
					collide_text.draw(screen)
				else:
					collide_text = Label("Collision with this block has made it red!",SCREEN_WIDTH/2,(SCREEN_HEIGHT/2)-85,RED,BLUE,'Verdana',24,True,True,True)
					collide_text.draw(screen)
			
			# See if all blocks were collected
			if score == 100:
				winner_text1 = Label(f"You collected all {score} blocks, you win!",SCREEN_WIDTH/2,(SCREEN_HEIGHT/2)-50,WHITE,GREEN,'Verdana',24,True,True,True)
				winner_text2 = Label("Press the ESCAPE key to quit the game.",SCREEN_WIDTH/2,(SCREEN_HEIGHT/2)-15,WHITE,GREEN,'Verdana',24,True,True,True)
				winner_text1.draw(screen)
				winner_text2.draw(screen)
			
			# Setting fps
			clock.tick(60)
		
			# Drawing everything to screen
			pyg.display.flip()

# Starting main function
if __name__ == '__main__':
	main()
	
pyg.quit() # Quitting pygame
