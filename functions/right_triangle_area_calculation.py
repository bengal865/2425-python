# Calculate Area of Right Triangle Using Functions

def get_base():
    '''Function that prompts user to enter length of base of a right triangle.'''
    base = float(input('Enter length of base (ft.):\n'))
    return base

def get_height():
    '''Function that prompts user to enter the height of a right triangle.'''
    height = float(input('Enter height of triangle (ft.):\n'))
    return height

def calc_triangle_area(base, height):
    '''Function that calculates the AREA of a right triangle.'''
    area = (0.5 * base) * height
    return area

def show_output(base, height, area):
     '''Function that displays the dimensions and the area of a right triangle.'''
     print(f'Triangle base (ft.): {base:,.2f}')
     print(f'Triangle height (ft.): {height:,.2f}')
     print(f'Triangle Area (sq. ft.): {area:,.2f}')

def main():
    '''Function that serves a container for the various function calls.'''
    triangle_base = get_base()
    triangle_height = get_height()
    triangle_area = calc_triangle_area(height=triangle_height, base=triangle_base)
    show_output(height=triangle_height, base=triangle_base, area=triangle_area)

main()