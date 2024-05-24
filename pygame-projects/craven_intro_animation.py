"""
 Pygame base template for opening a window
 Explanation video: http://youtu.be/vRB_983kUMc
"""
# Import the modules we'll need for this animation
import pygame, sys
 
# Define some color constants using RGB values
# Zero (0) means use none of a given color
# 255 means use as much of a given color as possible
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the pygame module
pygame.init()
 
# Use a Python TUPLE to set the width and height of the screen
# NOTE: Tuples use parentheses, whereas Python lists use square brackets [  ]
size = (700, 500)
# Set mode is used to remove the start menu, title bars, etc. and to
# transfer control of everything on the screen to the game
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Window Template")
 
# Loop until the user clicks the button to close the window
done = False

# Start position of our square
rect_x = 50
rect_y = 50

# Set speed and direction of square
rect_change_x = 5
rect_change_y = 5

# This code is used to control how fast the screen is updated
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while done ==False:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Code for clearing the screen goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased when the screen is cleared
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here 
    
       
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])

    pygame.draw.rect(screen, GREEN, [rect_x + 10, rect_y + 10, 30, 30])

    # Controls how fast the box moves on the screen
    rect_x += rect_change_x 
    rect_y += rect_change_y
    
    # Bounce square if needed
    # If square exits at top or bottom of screen, then reverse its direction
    
    
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
        
    # If square exits at left or right, then reverse its direction
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
        
    
    # --- Time to update the screen with what we've drawn
    
    pygame.display.flip()
 
    # --- Limiting how fast the loop runs (in this case, to 60 frames per second)
    clock.tick(60)
 
# Close the window and quit the pygame module
# Don't indent the next two lines of code!
pygame.quit()
sys.exit()
