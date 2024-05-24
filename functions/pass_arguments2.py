# Passing Arguments to Functions (VER 2.0)

def get_width():
    '''Function that prompts the user for the width of a rectangle.'''
    width = float(input('Enter rectangle width (ft.)\n'))
    return width

def get_length():
    '''Function that prompts the user for the length of a rectangle.'''
    length = float(input('Enter rectangle length (ft.)\n'))
    return length

def calc_rect_area(width, length):
    '''Function that calculates the area of a rectangle.'''
    return width * length

def show_output(width, length, area):
    '''Function that displays the dimensions and area of a rectangle.'''
    print(f'Length of rectangle (ft.): {length:,.2f}')
    print(f'Width of rectangle (ft.): {width:,.2f}')
    print(f'Area of rectangle (sq. ft.): {area:,.2f}')

def main():
    '''Function that serves as a container for assorted function calls.'''
    width = get_width()
    length = get_length()
    area = calc_rect_area(width, length)
    show_output(width, length, area)

main()