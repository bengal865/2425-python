# Simple Example of Passing Arguments

def get_fahr_temperature():
    '''Function that prompts user for the current temperature in degrees Fahrenheit.'''
    fahr_temp = float(input('Enter the temperature in Fahrenheit: (Example: 75)\n'))
    return fahr_temp

def convert_to_celsius(my_temperature):
    '''Function to convert degrees Fahrenheit to degrees Celsius.'''
    celsius_temperature = (my_temperature - 32) * 5/9
    return celsius_temperature

def show_output(fahrenheit, celsius):
    '''Function that displays the temperature in Fahrenheit and its Celsius equivalent.'''
    print(f'{fahrenheit} degrees Fahrenheit is equivalent to {celsius} degrees Celsius.')

def main():
    '''Function that serves as a container for various function calls in this project.'''
    f_degrees = get_fahr_temperature()
    c_converted =  convert_to_celsius(f_degrees)
    show_output(f_degrees, c_converted)

main()