# Practice:  Finding the MINIMUM Value in a Python List

## Overview
In this practice project, you'll:
- use the Python `min()` function to find the smallest number in a list of numbers
- use the Python `sum()` function to find the sum of all the numbers in a list of numbers

## Code Snippet
Check out the following code snippet.  Be prepared to explain in simple terms what the code
generally does or specific lines of code do.
```python
def find_max_value(numbers):
    if len(numbers) == 0:
        print('Sorry, but your list is empty!')
    else:
        return max(numbers)

# Example usage:
my_numbers = [20, 12, 18, 24, 36, 22]
max_value = find_max_value(my_numbers)
print(f"The maximum value is: {max_value}")
```

# Coding Challenge 1
- Create a new GitHub repo: ***list-stats-python***
- Add a ```main.py``` script to your repo
- Update the code snippet shown above so that Python uses the ```min()``` function to find the **lowest/smallest** quiz score in a list of quiz scores
- Print the smallest quiz score Python found for you
- Remember to rename your function (because you're no longer trying to find the maximum value in a list of numbers   

# Coding Challenge 2
- At the bottom of the script you wrote for Coding Challenge 1, write a Python function that:
    - takes one parameter named `numbers` (this parameter will 'catch' a list you pass to the function when you call the function)
    - makes sure the list you passed to the function was not an empty list
    - uses the Python `sum()` function to find the sum of all the numbers in the list you passed (sent) to the function
    - prints the sum of the numbers contained in your list
