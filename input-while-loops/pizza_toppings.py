# Bruce Provencher
# 10 OCT 2022
# Pizza Toppings (7-4 PCC)

keep_looping = True

while keep_looping:
    topping = input('Please enter a pizza topping for your pizza:  (Type quit to quit!)\n').lower()
    if topping == 'quit':
        #break
        keep_looping = False # Flag variable
    else:
        print(f'Adding {topping} to your pizza now!')
print('Exited the WHILE loop...')
print('Done adding toppings to your pizza! Bon appetit!')
