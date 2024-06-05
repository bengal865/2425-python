# Guessing Game with a Python List

secret_list = ["apple", "banana", "orange", "grape"]  

# This function checks your guess and provides clues about the content of the list
def guess_check(guess):
  if guess in secret_list:
    print("Yes! " + guess + " is in the list.")
  else:
    print("Nope, " + guess + " is not in the list.")
    # To help you guess, let's reveal the length of the list:", len(secret_list))

# Start guessing! Use the guess_check function to get clues about what's contained in the list

guess_check('hamburger')
guess_check('potato chips')

