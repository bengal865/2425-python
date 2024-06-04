# Movie Night Picker

# Import the random module
import random

# Define list of movie genres
genres = ['comedy', 'action', 'romance', 'drama', 'thriller']

# Use the random.choice () method to select a genre at random from the genres list
genre = random.choice(genres)
print(f'The movie genre selected at random was: {genre}')

# Remove a genre from the list if the list isn't empty
if len(genre) > 0:
  print(f'Removed the genre {genre} from the genres list.')
else:
  print("Sorry, the genres list is empty!")
  print(f"Can't remove the selected genre -- {genre} -- from an empty list.")
  print("Goodbye!")
