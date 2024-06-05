# Print last three list elements only using FOR loop
ice_cream_flavors = ["Vanilla", "Chocolate Chip Cookie Dough", "Mint Chocolate Chip", "Strawberry", "Coffee"]

# Number of elements to print
num_to_print = 3

print('\nPrint last three list elements only using FOR loop')
# Loop from the end of the list for the specified number of times
for i in range(len(ice_cream_flavors) - num_to_print, len(ice_cream_flavors)):
  print(ice_cream_flavors[i])


colors = ["red", "green", "blue", "magenta", "light blue"]

print('\nPrint even-index elements only')
print('after converting them to UPPERCASE\n')
# Loop through the list using a FOR loop
for i in range(len(colors)):
  if i % 2 == 0:  # Check if the element's index number is even
    colors[i] = colors[i].upper()  # Convert even-indexed elements to uppercase

print(f"The modified list: {colors}")


numbers = [1, 2, 3, 4, 5]

# Initialize a variable to store the sum
grand_total = 0

print('\nCalculate and print the grand total of the numbers in a list')
# Loop through the list using a FOR loop
for num in numbers:
  grand_total += num  # Add each element to the sum
  # Could also write the equation as:
  # grand_total = grand_total + num

print(f"The sum of the numbers is: {grand_total}\n")
