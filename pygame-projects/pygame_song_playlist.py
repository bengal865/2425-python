import pygame, sys

pygame.mixer.init()
pygame.display.init()

SCREENWIDTH = 320
SCREENHEIGHT = 240
size = (SCREENWIDTH, SCREENHEIGHT)

screen = pygame.display.set_mode (size)
  
my_sound = pygame.mixer.Sound("engine.ogg")  

keep_looping = True

volume = 1.0

while keep_looping:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_looping = False
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == ord ( "p" ):
				my_sound.play()
			elif event.key == ord ( "s" ):
				my_sound.stop()
			elif event.key == ord ( "f" ):
				my_sound.fadeout ( 2000 )
pygame.quit()
