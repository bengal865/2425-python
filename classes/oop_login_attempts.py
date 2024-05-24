# Programmer: Bruce Provencher
# Date: 14 JAN 2017
# Program: Login Attempts
# Source: Python Crash, p. 171

# Making a class called User
class User():
	"""A general description of a network user"""
	def __init__(self, first_name, last_name, gender, age, operating_system, school):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.age = age
		self.operating_system = operating_system
		self.school = school
		self.num_login_attempts = 25
		
	def describe_user(self):
		# A method to describe or list all the user's attributes
		print('Current user profile:')
		print("""
		First Name: {0}
		Last Name: {1}
		User Gender: {2}
		User Age: {3}
		User's OS: {4}
		Home School: {5}
		Previous Number of Login Attempts: {6}
		*** End of User Profile ***
		""".format(self.first_name, self.last_name, self.gender, self.age, self.operating_system, self.school, self.num_login_attempts))
		
	def increment_login_attempts(self):
		# A method that increments by 1 the number of login attempts
		self.num_login_attempts += 1
		
		
	def reset_login_attempts(self):
		# A method that resets to zero the number of login attempts
		self.num_login_attempts = 0
		
	def welcome_user(self):
		# This method welcomes the user to the network
		# after s/he has logged on
		print("Welcome, {0}! You have successfully logged on to the network!".format(self.first_name))
		
# Make an instance of the user class
user1 = User("Bill", "Gates", "male", 17, "MS Windows10", "Kingsley HS")
user1.describe_user()
print('Before today, the user attempted to log in to the network {0} times.'.format(user1.num_login_attempts))
# Incrementing the number of login attempts the user made
user1.increment_login_attempts()
user1.increment_login_attempts()
print('As of today, the user has attempted to log in to the network a total of {0} times.'.format(user1.num_login_attempts))
# Resetting number of login attempts to zero
user1.reset_login_attempts()
print('Now the number of login attempts for the user has been reset to ' + str(user1.num_login_attempts) + '.')

