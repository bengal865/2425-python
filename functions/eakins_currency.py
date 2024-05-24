################################
#       Jeremy Eakins          #
#         04/15/13             #
#     Currency Converter       #
################################

def intro():
	print("Welcome to the Currency Converter.  We can convert three different currencies.")
	print("""
		USD >>> Euros    =    1
		USD >>> Yen      =    2
		USD >>> Rupees   =    3
		"""
		)
			
def usdeuro(usd):
	euro = usd * 0.78
	return euro
	
def usdyen(usd):
	yen = usd * 94.037
	return yen
	
def usdrupees(usd):
	rupees = usd * 54.284
	return rupees

def replay():
	continue_playing = input("Enter  'y', then hit ENTER to play again, or just hit ENTER to quit the program.\n")
	return continue_playing
	
def con(cat):
	print("You have $" + str(usd) + " dollars, which is equivalant to " + str(cat) + " Euros!")
	

	
play = "y"
while play == "y":
	intro()
	choice = input("Please select an option from the conversion menu: ")
	if choice == "1":
		usd = float(input(" How many USD do you have?: "))
		cat = usdeuro(usd)
		con(cat)
		
		play = replay()

		
	elif choice == "2":
		usd = float(input(" How many USD do you have?: "))
		yen = usdyen(usd)
		print("You have $",usd ," dollars, which is equivalant to", yen ," Japanese Yen!")
		play = replay()
		
	elif choice == "3":
		usd = float(input(" How many USD do you have?: "))
		rupees = usdrupees(usd)
		print("You have $",usd ," dollars, which is equivalant to", rupees ," Indian Rupees!")
		play = replay()
		
	else:
		print("Invalid selection!")
		print("Would you like to perform another currency conversion?")
		play = replay()
		
print("Thank you for using my Currency Converter!")
		
		
	
		
		
		
		



	
	
	


		
