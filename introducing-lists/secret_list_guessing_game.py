# Guessing Game with a Python List

secret_list = ["apple", "banana", "orange", "grape"]  

# This function checks your guess and provides clues about the content of the list

'''
Start with broad guesses (e.g., "food") to narrow down the possibilities

Use the length information to your advantage. For example, if the length of the list is 4 and you guessed a fruit that wasn't in the list, there still might be 3 other fruits!

Refine your guess: Based on the clue, try to guess another item in the list. Keep guessing until you guess all the items 
in the list
'''

def guess_check(guess):
  if guess in secret_list:
    print("Yes! " + guess + " is in the list.")
  else:
    print("Nope, " + guess + " is not in the list.")
    print(f"To help you guess, let's reveal the length of the list: {len(secret_list)}")

# Start guessing! Use the guess_check function to get clues about what's contained in the list

guess_check('hamburger')
#guess_check('potato chips')


