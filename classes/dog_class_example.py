class Dog:

	has_ears = True 
	num_legs = 4
	animal_type = 'mammal'

	"""A simple attempt to model a dog."""  
  
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name 
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# Print some of the class-level attributes for each dog
print(f'My dog is named {my_dog.name} and he is a {my_dog.animal_type}.')

print(f'Your dog is named {your_dog.name} and he is a {your_dog.animal_type}.')
