# calculates a given rectangle area

def hello():
    print('\nHello!')
 
def area(width, height):
    return width * height
 
def print_welcome(name):
    print(f'Welcome, {name}!\n\n')
 
def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Dimension MUST be a positive number!')
        number = float(input(prompt))
    return number
 
name = input('Please enter your first name:\n')
hello()
print_welcome(name)
print()
print('To find the area of a rectangle,')
print('enter the rectangle\'s width and height below...')
print()
w = positive_input('Rectangle width:\n')
h = positive_input('Rectangle height:\n')
 
print('Rectangle Width =', w, ' Rectangle Height =', h, ' and Rectangle Area =', area(w, h))
