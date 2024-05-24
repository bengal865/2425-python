# Bruce Provencher
# 20 MAY 2021
# Using Class to Calculate Area of Rectangle
# Source: https://www.sanfoundry.com/python-program-find-area-rectangle-using-classes/

class Rectangle():
    def __init__(self, width, length):
        '''Class that calculates the area of a rectangle.'''
        self.width = width
        self.length = length
        
    def calculate_area(self):
        return self.width * self.length
        
# Prompt user for length and width of each rectangle
rect1_w = float(input('Enter the width of rectangle #1:\n'))
rect1_l = float(input('Enter the length of rectangle #1:\n'))

rect2_w = float(input('Enter the width of rectangle #2:\n'))
rect2_l = float(input('Enter the length of rectangle #2:\n'))
        
# Create two instances of the Rectangle class
my_rect = Rectangle(rect1_w, rect1_l)
your_rect = Rectangle(rect2_w, rect2_l) 

# Display the area of each rectangle
print(f'Area of rectangle #1 (in sq. ft.): {my_rect.calculate_area():.2f}')
print(f'Area of rectangle #2 (in sq. ft.): {your_rect.calculate_area():.2f}')   
    
    
