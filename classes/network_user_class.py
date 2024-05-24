#############################################################
# Programmer: Orren Sheets
# 1/23/2019
# Network user class
#############################################################

class User:
	""" Describes the user """
	def __init__(self, first_name, last_name, age, email):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
	
	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} years old. Their email is: {self.email}.")
		
	def welcome_user(self):
		print(f"Welcome back {self.first_name}. ")
		print("")
		
user1 = User("Robert", "Phillips", 43, "RobertPhillips@hotmail.com")
user2 = User("[REDACTED]", "Wallow", "[REDACTED]", "[DATA EXPONGED]")
user3 = User("Tommy", "Jenkins", 14, "CoolguyTommy@gmail.com")
	
user1.describe_user()
user1.welcome_user()

user2.describe_user()
user2.welcome_user()

user3.describe_user()
user3.welcome_user()
	
	
	
	
	
	
