# Define the showCodeBlock function

def showCodeBlock():
    print ("\nProgrammer: Bruce Provencher")
    print ("Date: 15 MAY 2014")
    print ("Project: Celsius to Fahrenheit Converter\n")

def convertToFahrenheit(myTemp):

    fahrenheit = 9.0/5.0 * myTemp + 32
    return fahrenheit


showCodeBlock()

celTemp = float(input("Enter your temperature in degrees Celsius: \n\n"))



print ("Celsius", "\t\t", "Fahrenheit")
for celTemp in range (0, 101, 10):
    print (celTemp, "\t\t\t", convertToFahrenheit(celTemp))



  
