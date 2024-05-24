'''
Bruce Provencher
APR 28 2021
Pygame text project
'''

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

# Display settings
HEIGHT = 400
WIDTH = 700
# Store height and width in a tuple named 'size'
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Label Class Demo")


class Label():
    '''A label class that lets us quickly draw text onto a Pygame screen.'''
    
    def __init__(self, label_text, text_rect_x, text_rect_y, text_color, font_name, font_size):
        
        self.font_name = font_name
        self.font_size = font_size
        
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        
        self.label_text = label_text
        
        self.text_color = text_color
   
        # True means the font is anti-aliasied (so it doesn't appear as jasgged on the screen)
        self.text = self.font.render(self.label_text, True, self.text_color)
        
        # self.text_rect = self.text.get_rect()
        self.text_rect_x = text_rect_x
        self.text_rect_y = text_rect_y
        
    def draw_label(self):
        screen.blit(self.text, [self.text_rect_x, self.text_rect_y])
        
session_label = Label("WGP AM", 200, 200, BLUE, 'Helvetica', 50)

school_label = Label("Career Tech", 300, 250, RED, 'Georgia', 40)

# Create a flag variable that tells the WHILE
# loop to keep looping until the user clicks the 
# close button on the window (which then sets the flag 
# variable to False)

keep_looping = True

# Manage how often the screen is updated
clock = pygame.time.Clock()

# Frames per second (FPS) for screen refresh rate
FPS = 60

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
    screen.fill(WHITE)
    
    # Draw some lines or shapes below this comment
    session_label.draw_label()
    
    school_label.draw_label()
    
    
    
    # UPDATE the screen with what we've drawn
    pygame.display.flip()
    
    # Set screen refresh/redraw rate [frames per second]
    clock.tick(FPS)
    
# Close window and quit
pygame.quit()
sys.exit()
