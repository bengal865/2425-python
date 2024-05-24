# Currency Converter Program

def usd_to_euros():
	euros = dollars * 0.78
	print(dollars,"dollars is equivalent to",euros,"euros")
	
def usd_to_yen():
	yen = dollars * 94.037
	print(dollars,"dollars is equivalent to",yen,"yen")
	
def usd_to_rupees():
	rupees = dollars * 54.284
	print(dollars,"dollars is equivalent to",rupees,"rupees")

choice = None

while choice != 0:
	print("""
Welcome to my currency converter program!
	
1: Convert USD to European Euros
2: Convert USD to Japanese Yen
3: Convert USD to Indian Rupees
4: Quit Program
		""")
	choice = int(input("\nPlease enter your choice: "))

	if choice == 1:
		print ("\nYou hav selected Convert USD to European Euros")
		dollars = float(input("\nHow much USD would you like to convert: "))
		usd_to_euros()
		answer = input("\nWould you like to make another conversion: ")
		answer.lower()
		if answer == "no":
			choice = 0
			print("Goodbye!")
		elif answer == "yes":
			choice = 1			
	elif choice == 2:
		print ("\nYou hav selected Convert USD to Japanese Yen")
		dollars = float(input("\nHow much USD would you like to convert: "))
		usd_to_yen()
		answer = input("\nWould you like to make another conversion: ")
		answer.lower()
		if answer == "no":
			choice = 0
			print("Goodbye!")
		elif answer == "yes":
			choice = 1
	elif choice == 3:
		print ("\nYou hav selected Convert USD to Indian Rupees")
		dollars = float(input("\nHow much USD would you like to convert: "))
		usd_to_rupees()
		answer = input("\nWould you like to make another conversion: ")
		answer.lower()
		if answer == "no":
			choice = 0
			print("Goodbye!")
		elif answer == "yes":
			choice = 1
	elif choice == 4:
		choice = 0
		print("Goodbye!")
