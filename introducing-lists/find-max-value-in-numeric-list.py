# Find the maximum value in a list of numbers
def find_max_value(numbers):
    if len(numbers) == 0:
        print('Sorry, but your list is empty!')
    else:
        return max(numbers)

# Example usage:
my_numbers = [20, 12, 18, 24, 36, 22]
max_value = find_max_value(my_numbers)
print(f"The maximum value is: {max_value}")
