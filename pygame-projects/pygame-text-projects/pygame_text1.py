import pygame   
pygame.init()
     
# use a (r, g, b) tuple for color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0) 
    
# create the basic window/screen and a title/caption
# default is a black background
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text adventures with Pygame")
def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	# pick a font you have and set its size
	myfont = pygame.font.SysFont(Textfont, Textsize)
	# apply it to text on a label
	label = myfont.render(txtText, 1, Textcolor)
	# put the label object on the screen at point Textx, Texty
	screen.blit(label, (Textx, Texty))
	# show the whole thing
	pygame.display.flip()
#printText(Text, Font, Size, X, Y, Color)
printText("Hello World", "MS Comic Sans", 30, 10, 10, red)
printText("Hello World", "MS Comic Sans", 30, 10, 30, green)
printText("Hello World", "MS Comic Sans", 30, 10, 50, blue)
printText("Hello World", "MS Comic Sans", 30, 10, 70, yellow)
