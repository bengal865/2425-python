def find_max_value(numbers):
    if len(numbers) == 0:
        print('Sorry, but your list is empty!')
    else:
        return max(numbers)
    
def find_min_value(numbers):
    if len(numbers) == 0:
        print('Sorry, but your list is empty!')
    else:
        return min(numbers)
    
def find_sum(numbers):
    if len(numbers) == 0:
        print('Sorry, but your list is empty!')
    else:
        return sum(numbers)

# Finding the minimum value in the list
my_numbers = [20, 12, 18, 24, 36, 22]
min_value = find_min_value(my_numbers)
print(f"The minimum value in the list is: {min_value}")

# Finding the MAXIMUM value in the list
my_numbers = [20, 12, 18, 24, 36, 22]
max_value = find_max_value(my_numbers)
print(f"The maximum value is: {max_value}")

# Finding the SUM of all the values in the list
my_numbers = [20, 12, 18, 24, 36, 22]
sum_of_list_values = find_sum(my_numbers)
print(f"The sum of the numbers in the list is: {sum_of_list_values}")