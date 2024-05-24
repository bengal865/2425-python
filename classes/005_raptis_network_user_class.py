#############################
# Progammer: Alexander Raptis
# Date: 22 JAN 2018
# Project: Network User Class
#############################

# Defining user class
class User():
	"""Describes a typical network user by first name, last name, sex and age"""
	# Constructor method
	def __init__(self,first_name,last_name,sex,age):
		self.fname = first_name.title()
		self.lname = last_name.title()
		self.sex = sex
		self.age = age
	# Describe user method
	def describe_user(self):
		print(f"My name is {self.fname} {self.lname}.")
		print(f"I am a {self.sex} who is {self.age} years old.\n")
	# Welcome user method
	def welcome_user(self):
		print(f"Hello {self.fname} {self.lname}, welcome to the game.\n")

# Creating two instances of user class	
usr1 = User("alexander","raptis","male",16)
usr2 = User("elizabeth","sowulewski","female",16)
usr3 = User("kane","clark","male",17)

# Using describe user method to describe users one, two, and three
usr1.describe_user()
usr2.describe_user()
usr3.describe_user()

# Using welcome user method to welcome users one, two, and three
usr1.welcome_user()
usr2.welcome_user()
usr3.welcome_user()
