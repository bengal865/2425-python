"""
 Simple graphics demo
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game module
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 100, 23)

# Set the height and width of the screen
WIDTH = 500
HEIGHT = 400
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Shapes & Text")
 

clock = pygame.time.Clock()

FPS = 60

# Loop as long as done is set to False
done = False
 
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag variable is changed to True so now we exit the WHILE loop
 
    # All drawing code happens after the for loop and but
    # inside the main/WHILE loop
 
    # Set the screen background color
    screen.fill(WHITE)
 
    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
 
    # Draw on the screen several lines from (0,10) to (100,110) using an offset value for spacing
    # Line is 5 pixels wide 
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
 
 
    # Draw a rectangle
    pygame.draw.rect(screen, PURPLE, [20, 20, 250, 100], 4)
 
    # Draw an ellipse, using a rectangle as the outside boundaries for the ellipse
    pygame.draw.ellipse(screen, ORANGE, [20, 20, 250, 100], 3)
 

    # Drawing a triangle using the polygon command
    pygame.draw.polygon(screen, BLUE, [[100, 100], [0, 200], [200, 200]], 5)
 
    # Select the font to use, font size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    # Black is the text color, yellow the text background color. This creates an image of the
    # letters, but does not actually add the text image to the screen
    text = font.render("My text", True, BLACK, YELLOW)
 
    # Put the image of the text on the screen at x, y of (60, 250)
    screen.blit(text, [60, 250])
 
    # Go ahead and update the screen with what we've drawn
    # This MUST happen after all the other drawing commands have been executed
    pygame.display.update()
 
    # This limits the while loop to a max of 60 times (frames) per second.
    clock.tick(FPS)
 
# Be IDLE-friendly
pygame.quit()
