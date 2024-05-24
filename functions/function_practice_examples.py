def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")
	
greet_user("michelle")
print()
print()

def describe_pet(animal_type, pet_name):
	"""Function that displays info about a pet."""
	print(f"I have a(n) {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
	
	
describe_pet("cat", "rambo")
print()
print()


def show_city_info(city, country = "Canada"):
	"""Function that shows some info about a specific city."""
	print(f"{city.title()} is in {country.title()}.")
	
show_city_info("madrid", "spain")
show_city_info("halifax", "canada")
show_city_info("toronto")


print()
print()

def get_formatted_name(first_name, last_name):
	"""Return a full name, nicely formatted."""
	full_name = first_name + " " + last_name
	return full_name.title()
	
	
while True:
	print("Please tell me your name:\n")
	print("Enter 'q' at any time to quit the loop!")
	
	f_name = input("Enter your first name:\n")
	if f_name == "q":
		break

	l_name = input("Enter your last name:\n")
	if l_name == "q":
		break
	formatted_name = get_formatted_name(f_name, l_name)
	#print(f_name)
	#print(l_name)
	

print(f"Hello, {formatted_name}!")


