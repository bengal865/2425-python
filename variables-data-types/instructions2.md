# Intro to Python Strings

## Objective

> - Students will learn how to assign a string to a Python variable
> - Students will use the `input ( )` function to get input from the user
> - Students will convert user input to integers and floats using the built-in Python `int( )` and `float(  )` functions
> - Students will convert strings to upper- and lowercase using the built-in Python `upper()` and `lower()` methods

## Submitting Your Work
- Create a GitHub repository: `strings-practice-python`
- Upload your script to your repo
- Submit the URL that points to your repo on Google Classroom

## General Specifications

- Add a comment block to your script
```python
# Abraham Lincoln
# 24 MAR 20XX
# Intro to Python Strings
```
- Use short, descriptive filenames
- Write your filenames in lowercase

## Resources & Examples

- [Python strings](https://www.w3schools.com/python/python_strings.asp)
- [How to concatenate strings in Python](https://www.w3schools.com/python/python_strings_concatenate.asp)
- [Converting strings to upper- and lowercase](https://www.programiz.com/python-programming/methods/string/upper)

## Writing Your Script

- Show you know how to *concatenate* strings
    - Assign your first and last name to two string variables
    - Create a third variable `full_name`
    - Use the concatenation operator (+) to assign your first and last names to the variable `full_name`
    - Then use concatenation to print your first name in a sentence, your last name in a sentence, and your full name in a sentence
- Show you know how to use the `input ()` function to get input from the user, i.e., prompt the user to enter information
    - Define a variable `city` and then use the input function to ask the user which city in Michigan they live in
    - Use concatenation to display a sentence that says which city the user lives in
    - Define a variable `hourly_wage` and use the `float()` and `input()` functions together to ask the user what their hourly wage is at Burger King; then use the `input()` function to get the user's first name; use concatenation to build a custom string that includes the user's first name and hourly wage
      > Example: Mikey earns $14.50 an hour at Burger King.
    - use the `int()` and `input()` functions together to ask the user to please enter their age; use concatenation to display a sentence similar to the following example:
      > Example: The user's age is 17.
    - Use the `input()` function to prompt the user to enter their last name **in all lowercase characters**; then apply the `upper()` method to convert the last name to uppercase; use the `print()` function to display the uppercase version of the user's last name
    - Use the `input()` function to prompt the user to enter the name of the city in which they reside **in all UPPERCASE characters**; then apply the `lower()` method to convert the city name to lowercase; use the `print()` function to display the lowercase version of the city name
