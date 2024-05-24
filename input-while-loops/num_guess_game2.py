# Programmer: Bruce Provencher
# Date: 18 OCT 2018
# Number Guess Game 
# https://www.youtube.com/watch?v=Jk3az4ZXEKU

# Import Python's random module
import random, time

fname = input("Hello! What is your first name?\n")

# Generate a random number between 1 and 100
rand_number = random.randint(1,100)

# Greet user
time.sleep(2)
print(f"Well, {fname}, I'm thinking of a number between 1 and 100...")

guesses_made = 0

# Set up the game loop
while guesses_made < 5:
	guess = int(input("Enter your guess:\n"))
	guesses_made = guesses_made + 1
	if guess < rand_number:
		print("Too low! Try again!")
	elif guess > rand_number:
		print("Uhhh...that was too high!")
	else:
		break # Exit loop immediately
		
if guess == rand_number:
	print(f"Congratulations, {fname}! You guessed the number!")
	print(f"The number was {rand_number}.")
	print(f"It took you {guesses_made} to guess the mystery number.")
else:
	print(f"Sorry, {fname}.  You lose! Better luck next time!")
	print(f"The mystery number was {rand_number}, by the way.")
