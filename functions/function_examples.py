#########################################
# Name: Bruce Provencher
# Project: Miscellaneous Functions Demo
# Date: 21 JAN 2013
#########################################

# This project demonstrates some commonly used Python functions
# and the output they produce

# By itself, the input ( ) function will return a string
number = input("Please type in a number between 1 and 10: ")
print (type(number))

# Float () function is used to get a float or floating-point number, i.e. a number that
# contains a decimal point


number = float(input("Type in a different number: "))

# The int ( ) function will return an integer value, i.e. a numeric value with
# no decimal point

# Again, the input ( ) function by itself returns a string, so
# the string value must be converted to an integer and then
# assigned to the variable named 'integer' (in this example)
integer = int(input("Type in an integer: "))

# The input ( ) function returns a string
text = input("Type in a string: ")

# Display the value stored in the variable named 'number'
print("number =", number)

# Use the type ( ) function to display the data type of the variable named 'number'
print("number is a", type(number))

# Display the result of the value stored in the variable 'number' times two
print("number * 2 =", number * 2)

# Display the value stored in the variable named 'integer'
print("integer =", integer)

# Display the data type of the variable named 'integer'
print("integer is a", type(integer))

# Display the result of the value stored in the variable 'integer' times two
print("integer * 2 =", integer * 2)

# Display the value stored in the variable named 'text' 
print("text =", text)

# Display the data type of the variable named 'text'
print("text is a", type(text))

# Display the result of the value stored in the variable 'text' times two
print("text * 2 =", text * 2)

# Assign a integer value to a variable named 'exam_score'
# The input ( ) function returns a string value, but the eval ( ) function can be used
# to convert the string to an integer (assuming an integer is initially entered as the exam score)
# Print the student's exam score
exam_score = eval (input ("Please enter the student's exam score: "))
print(exam_score)
print(type (exam_score))

# Assign a floating-point number to a variable named 'exam_score'
# The input ( ) function returns a string value, but the eval ( ) function can be used
# to convert the string to FLOATING-POINT NUMBER (assuming a floating-point number is initially entered as the exam score)
# Print the student's exam score
exam_score = eval (input ("Please enter the student's exam score: "))
print (exam_score)
print (type (exam_score))

# Now print the length [the number of characters, including spaces] in a string
my_sentence = input ("Please enter a sentence containing three or more words: ")
# Use the len ( ) function to count the number of characters in the string the user entered
sentence_length = len(my_sentence)
# Display a message that tells the user how many characters the string s/he entered contained, spaces included
print ("The sentence you entered contains",str(sentence_length),"characters, spaces included.")

