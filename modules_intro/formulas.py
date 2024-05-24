# Kaylee Lemmien
# 11/14/22
# Area Functions Module

def circle(radius):
    '''Function that calculates the area of a circle.'''
    radius_squared = radius * radius
    area = 3.14 * radius_squared
    print(f'Radius Length: {radius}')
    print(f'Area: {area:,.2f}')


def right_triangle(base, height):
    '''Function that calculates the area of a right triangle.'''
    area = base * height / 2
    print(f'Base: {base}')
    print(f'Height: {height}')
    print(f'Area: {area:,.2f}')


def parallelogram(base, height):
    '''Function that calculates the area of a parallelogram.'''
    area = base * height
    print(f'Base: {base}')
    print(f'Height: {height}')
    print(f'Area: {area:,.2f}')
    

