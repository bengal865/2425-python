import sys
import time

def calc_product(num1, num2):

    my_product = num1 * num2
    return my_product
def calc_quotient(num1, num2):

    my_quotient = num1 / num2
    return my_quotient

def show_menu():
    menu_options = [1, 2]
    choice = 0
    print('1. Multiplication')
    print('2. Division')
    while True:
            choice = input("Please select a menu option (1 or 2):\n")
            try:
                choice = int(choice)
                
                if choice not in menu_options:
                    print('Invalid input! Enter 1 or 2 only, please!')
                    continue

                elif choice == 1:
                    print('You selected multiplication...')
                    time.sleep(1)

                elif choice == 2:
                    print('You selected division...')
                    time.sleep(1)
                
            except ValueError:
                print('Enter numbers only, please!')
                continue
            else:
                break
    return choice
   

def do_calculation(option, first_num, second_num):
    operation = ''
    if option == 1:
        answer = calc_product(first_num, second_num)
        operation = 'times'
        return f'{first_num} {operation} {second_num} is {answer}.'
    elif option == 2:
        answer = calc_quotient(first_num, second_num)
        operation = 'divided by'
        return f'{first_num} {operation} {second_num} is {answer}.'

def get_first_number():
    num1 = float(input('Enter a number: (Example: 4)\n'))
    return num1

def get_second_number():
    num2 = float(input('Enter another number: (Example: 2)\n'))
    return num2

def show_output(first_num, second_num, result):
    print(f'First number: {first_num}')
    print(f'Second number: {second_num}')
    print(f'{result}')

def play_again():
    affirmatives = ['y', 'yes']
    negatives = ['n', 'no']

    go_again = input('Do you want to run the calculator again? (y/n)\n').lower()

    if go_again in affirmatives:
        main()
    elif go_again in negatives:
        print('Thank you for using my calculator today!')
        time.sleep(2)
        print('Goodbye!')
        sys.exit()
    else:
        play_again()

def main():
  
    menu_choice = show_menu()
    first_number = get_first_number()
    second_number = get_second_number()
    calculated_answer = do_calculation(menu_choice, first_number, second_number)
    show_output(first_number, second_number, calculated_answer)

    play_again()

main()