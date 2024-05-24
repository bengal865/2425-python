import pygame, sys, os
 
running = True
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()



#create text label
font = pygame.font.Font(None, 24)
font_color = (255,255,255)
font_background = (0,0,0)
t = font.render("Hello World", True, font_color, font_background)
t_rect = t.get_rect()
t_rect.centerx, t_rect.centery = 100, 100
 
def update():

	#draw text to screen
	screen.blit(t, t_rect)
 
if __name__ == "__main__":
	while running:
		update()
		pygame.display.flip()
		clock.tick(30)
	pygame.quit()
	sys.exit()
